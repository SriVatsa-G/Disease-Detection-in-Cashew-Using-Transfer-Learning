import os
import shutil
import numpy as np
from PIL import Image

# Set the base path to the dataset
base_path = '/mnt/c/SV-Desktop/FALL SEMESTER 2024-25/Dissertation 1/Implementation/Dataset/Dataset for Crop Pest and Disease Detection/Raw Data/CCMT Dataset/Cashew'

# Set train, validation, and test split ratios
train_split = 0.7
val_split = 0.15
test_split = 0.15

# Set image height and width (optional, can be removed if you don't resize images)
IMG_HEIGHT = 224
IMG_WIDTH = 224

# List of categories/classes
categories = ['anthracnose','healthy','leaf miner','red rust']

# Function to copy images to the target directory
def copy_images(source_path, destination_path):
    shutil.copy(source_path, destination_path)  # Copy the image to the destination path

# Function to split dataset into train, validation, and test directories
def split_data(base_path, category, train_split, val_split):
    category_path = os.path.join(base_path, category)  # Path for the specific category
    images = os.listdir(category_path)  # List all images in the category directory

    # Shuffle images to ensure random distribution
    np.random.seed(42)  # Set seed to ensure consistent splitting
    np.random.shuffle(images)

    # Calculate the number of images for each dataset split
    train_size = int(len(images) * train_split)
    val_size = int(len(images) * val_split)

    # Split images into train, validation, and test sets
    train_images = images[:train_size]
    val_images = images[train_size:train_size + val_size]
    test_images = images[train_size + val_size:]

    # Create directories for train, val, and test if they don't exist
    for split in ['train', 'val', 'test']:
        split_dir = os.path.join(base_path, split, category)
        if not os.path.exists(split_dir):
            os.makedirs(split_dir)

    # Copy images to train directory
    for img in train_images:
        copy_images(os.path.join(category_path, img), os.path.join(base_path, 'train', category, img))

    # Copy images to validation directory
    for img in val_images:
        copy_images(os.path.join(category_path, img), os.path.join(base_path, 'val', category, img))

    # Copy images to test directory
    for img in test_images:
        copy_images(os.path.join(category_path, img), os.path.join(base_path, 'test', category, img))

# Apply split for each category
for category in categories:
    split_data(base_path, category, train_split, val_split)

# Function to verify the split
def verify_dataset_split(base_path, categories):
    total_count = 0
    for split in ['train', 'val', 'test']:
        split_count = 0
        for category in categories:
            path = os.path.join(base_path, split, category)
            count = len(os.listdir(path))
            split_count += count
            print(f"{split.capitalize()} - {category}: {count} images")
        print(f"Total in {split}: {split_count} images")
        total_count += split_count
    print(f"Overall total images: {total_count}")

# Verify the dataset split
verify_dataset_split(base_path, categories)
