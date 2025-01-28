#!/bin/bash
# Shell script to run the generate_dataset.py script with configuration parameters in a conda environment

# Enable extended globbing
shopt -s extglob

# Set the number of API call cycles to run to go through enough data
N=87
SUBJECTS=(0)

# Define the arrays of dataset paths and output paths
DATASET_PATHS=("./data/GSM8K_train.jsonl")
OUTPUT_PATHS=("./GSM8K_generated_test_data")

# Set other parameters
MODEL_NAME="QWEN2.5-1.8B-Math"
NUMBER_OF_ROUNDS=1
INIT_PROMPT="You are a math expert. When you respond, respond only with the Solution of the final Problem, thinking step by step. At the end of the Solution, when you give your final answer, write it in the form 'I hope it is correct: #### \$answer\$'"
SELF_CORR_PROMPT="There might be an error in the solution above because of lack of understanding of the question. Please correct the error, if any, and rewrite the solution. Only output the final solution! At the end of the Solution, when you give your final answer, write it in the form 'I hope it is correct: #### \$answer\$'"
DATASET_FORMAT="jsonl"


# Navigate to the directory containing the Python scripts
cd ~/GenAI_Self_Corr-2 || exit

# Loop over the number of iterations
for ((i=1; i<=N; i++)); do
    # Loop over the subjects
    for j in "${SUBJECTS[@]}"; do
        # Get the corresponding dataset path and output path by index
        DATASET_PATH="${DATASET_PATHS[$j]}"
        OUTPUT_PATH="${OUTPUT_PATHS[$j]}"

        # Run the Python script with the parameters
        python GSM8K_gen_data.py --dataset_path "$DATASET_PATH" --model_name "$MODEL_NAME" --output_path "$OUTPUT_PATH" --number_of_rounds "$NUMBER_OF_ROUNDS" --init_prompt "$INIT_PROMPT" --self_corr_prompt "$SELF_CORR_PROMPT" --dataset_format "$DATASET_FORMAT"

        # Pause for 20 seconds to reset the API call limit
        sleep 20
    done
done

# Loop over output paths to generate plots
for j in "${SUBJECTS[@]}"; do
    # Get the corresponding output path by index
    OUTPUT_PATH="${OUTPUT_PATHS[$j]}"

    # Run the Python script to generate plots
    python GSM8K_check_self_corr.py --folder_path "$OUTPUT_PATH"

    # Pause for 1 second to allow the file to be saved
    sleep 1
done

# Deactivate the Anaconda environment
conda deactivate

echo "Done!"
