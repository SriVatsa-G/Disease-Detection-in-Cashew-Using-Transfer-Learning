import os
from PIL import Image

def resize_images_in_directory(base_path, target_size=(224, 224)):
    """
    Resize images in a given directory to the target size.

    Args:
    - base_path (str): The path to the directory containing subdirectories of images.
    - target_size (tuple): The target size of the images as (width, height).
    """
    # Iterate over all directories within the base path
    for subdir in os.listdir(base_path):
        subdir_path = os.path.join(base_path, subdir)
        if os.path.isdir(subdir_path):  # Check if it is a directory
            # Iterate over all files in the subdirectory
            for filename in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, filename)
                # Check if the file is an image
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    try:
                        # Open an image file
                        with Image.open(file_path) as img:
                            # Resize the image
                            img_resized = img.resize(target_size, Image.LANCZOS)
                            # Save the resized image back to the same location
                            img_resized.save(file_path)
                            print(f"Resized and saved: {file_path}")
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")

# Define the base path to your dataset
base_path = r'C:\SV-Desktop\FALL SEMESTER 2024-25\Dissertation 1\Implementation\Dataset\Dataset for Crop Pest and Disease Detection\Raw Data\CCMT Dataset\Cashew'

# Call the function to resize images
resize_images_in_directory(base_path)



