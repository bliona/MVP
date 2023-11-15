from PIL import Image

def compress_image(input_path, output_path, quality=85):
    """
    Compresses an image.

    Parameters:
    - input_path (str): The path to the input image file.
    - output_path (str): The path to save the compressed image.
    - quality (int): The image quality, a value between 0 (worst) and 100 (best).

    Returns:
    - None
    """
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Save the compressed image
            img.save(output_path, quality=quality)
            print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_image_path = "input_image.jpg"  # Provide the path to your input image
output_image_path = "compressed_image.jpg"  # Output path for the compressed image

compress_image(input_image_path, output_image_path)
