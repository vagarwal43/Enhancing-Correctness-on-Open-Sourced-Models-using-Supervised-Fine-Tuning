import os
import matplotlib.pyplot as plt

def collect_data(directory):
    folder_paths = []
    first_accuracies = []
    second_accuracies = []

    for file_name in os.listdir(directory):
        if file_name.endswith("_Base.txt"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                folder_path = file_name.split("_")[0]  # Adjusted to differentiate groups
                first_accuracy = float(lines[1].split(": ")[1].strip())
                second_accuracy = float(lines[2].split(": ")[1].strip())

                folder_paths.append(folder_path)
                first_accuracies.append(first_accuracy)
                second_accuracies.append(second_accuracy)

    return folder_paths, first_accuracies, second_accuracies

def rename_groups(folder_paths):
    """
    Rename folder paths to desired group names.
    Args:
        folder_paths (list): List of original folder path names.
    Returns:
        list: List of renamed group names.
    """
    # Define your mapping from original names to new names
    name_mapping = {
        "Math": "Math",
        "GSM8K": "GSM8K",
        # Add more mappings as needed
    }
    
    # Apply the mapping to rename the folder paths
    renamed_paths = [name_mapping.get(folder, folder) for folder in folder_paths]
    return renamed_paths

def plot_accuracies(folder_paths, first_accuracies, second_accuracies):
    x = range(len(folder_paths))  # Create positions for the bars

    fig, ax = plt.subplots(figsize=(6,8))
    bar_width = 0.25

    color_round_one = '#A2C5E7'  # Faint shade of dark blue
    color_round_two = '#FDE59C'

    # Plot the bars for First and Second Accuracies
    bar1 = plt.bar(x, first_accuracies, bar_width, label='First Accuracy', color=color_round_one)
    bar2 = plt.bar([p + bar_width for p in x], second_accuracies, bar_width, label='Second Accuracy', color=color_round_two)

    # Add labels, title, and legend
    plt.xlabel('Dataset and Model', fontsize=12)
    plt.ylabel('Accuracy', fontsize=12)
    ax.set_title('Test Split Accuracies for Qwen2.5-MATH-1.8B Base', fontsize=14)
    plt.yticks(fontsize=12)
    plt.xticks([p + bar_width / 2 for p in x], fontsize=12)
    ax.set_xticklabels(folder_paths, rotation=45, ha="right", fontsize=12)
    ax.legend(fontsize=12, loc='upper right')

    # Add data labels showing the differences above the bars
    for i in x:
        difference = second_accuracies[i] - first_accuracies[i]
        # Display the difference above the taller bar
        max_height = max(first_accuracies[i], second_accuracies[i])
        text_y_position = max_height + 0.05 * max(max(first_accuracies), max(second_accuracies))  # Position text slightly above the bar
        if difference > 0:
            plt.text(i + bar_width / 2, text_y_position, f'+{difference:.2f}%', ha='center', fontsize=16, color='green')
        else:
            plt.text(i + bar_width / 2, text_y_position, f'{difference:.2f}%', ha='center', fontsize=16, color='red')

    # Adjust the y-axis limit
    max_value = max(max(first_accuracies), max(second_accuracies))
    plt.ylim(0, max_value * 1.3)  # Add 30% padding to the maximum value

    # Adjust layout and save the plot
    plt.tight_layout()
    plt.savefig('accuracy_plot_fixed.png')  # Save the plot to a PNG file
    plt.show()  # Display the plot

if __name__ == "__main__":
    directory = "./bar_plot_results"  # Change this to your directory path
    folder_paths, first_accuracies, second_accuracies = collect_data(directory)
    
    # Rename the groups
    folder_paths = rename_groups(folder_paths)
    
    # Plot with renamed group names
    plot_accuracies(folder_paths, first_accuracies, second_accuracies)
