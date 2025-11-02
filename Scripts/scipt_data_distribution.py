import os
import matplotlib.pyplot as plt

def count_images_in_directory(base_dir, categories):
    data_distribution = {}
    for category in categories:
        train_dir = os.path.join(base_dir, 'train', category)
        val_dir = os.path.join(base_dir, 'val', category)
        test_dir = os.path.join(base_dir, 'test', category)

        train_count = len(os.listdir(train_dir))
        val_count = len(os.listdir(val_dir))
        test_count = len(os.listdir(test_dir))

        data_distribution[category] = {
            'train': train_count,
            'val': val_count,
            'test': test_count
        }

    return data_distribution

def plot_data_distribution(data_distribution):
    categories = list(data_distribution.keys())
    train_counts = [data_distribution[cat]['train'] for cat in categories]
    val_counts = [data_distribution[cat]['val'] for cat in categories]
    test_counts = [data_distribution[cat]['test'] for cat in categories]

    plt.figure(figsize=(10, 6))
    width = 0.3
    bar1 = plt.bar([x - width for x in range(len(categories))], train_counts, width, label='Train')
    bar2 = plt.bar(range(len(categories)), val_counts, width, label='Validation')
    bar3 = plt.bar([x + width for x in range(len(categories))], test_counts, width, label='Test')

    plt.xlabel('Categories')
    plt.ylabel('Number of Images')
    plt.title('Data Distribution Across Train, Validation, and Test Sets')
    plt.xticks(range(len(categories)), categories, rotation=45)
    plt.legend()

    for bar in bar1 + bar2 + bar3:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# Define the categories
categories = ['anthracnose','healthy','leaf miner','red rust']

# Define the base path to the dataset (Windows path or WSL path)
base_path = r'/mnt/c/SV-Desktop/FALL SEMESTER 2024-25/Dissertation 1/Implementation/Dataset/Dataset for Crop Pest and Disease Detection/Raw Data/CCMT Dataset/Cashew'

# Calculate and print the data distribution
data_distribution = count_images_in_directory(base_path, categories)

# Print the results in a structured way
print("Data Distribution:")
for category, counts in data_distribution.items():
    print(f"{category}: Train={counts['train']}, Val={counts['val']}, Test={counts['test']}")

# Plot the data distribution
plot_data_distribution(data_distribution)

