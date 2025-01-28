import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "Qwen/Qwen2-Math-1.5B"
model = None
tokenizer = None
device = None

def init_model(model_name=MODEL_NAME):
    global model, tokenizer, device
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

def huggingface_chat(prompt, model, temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    """
    Generate text completions using Hugging Face's transformers models.
    """

    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)
    prompt_length = inputs["input_ids"].shape[-1]

    # Generate completions
    outputs = []
    for _ in range(n):
        generated_ids = model.generate(
            inputs["input_ids"],
            max_new_tokens=200,
            temperature=temperature,
            do_sample=True,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )
        output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        
        # Handle stopping condition if stop tokens are provided
        if stop:
            for stop_token in stop:
                if stop_token in output:
                    output = output.split(stop_token)[0]
                    break

        outputs.append(output)
    return outputs

def huggingface_gpt(prompt, temperature=0.7, max_tokens=200, n=1, stop=None) -> list:
    """
    Wrapper function to match the gpt() interface style.
    """
    return huggingface_chat(prompt, model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)

