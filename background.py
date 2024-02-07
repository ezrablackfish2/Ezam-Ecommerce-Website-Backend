import rembg
import os

def remove_background(input_path, output_dir):
    """
    Removes the background of an image using rembg and saves the result to the output directory.
    
    Args:
        input_path (str): Path to the input image file.
        output_dir (str): Directory where the output image with removed background will be saved.
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construct output file path
    input_filename = os.path.basename(input_path)
    output_filename = os.path.splitext(input_filename)[0] + "_removed.png"
    output_path = os.path.join(output_dir, output_filename)

    # Read input image data
    with open(input_path, "rb") as f_input:
        input_data = f_input.read()

    # Remove background using rembg
    with open(output_path, "wb") as f_output:
        f_output.write(rembg.remove(input_data))

    print(f"Background removed image saved to: {output_path}")

# Example usage:
input_path = "./order.jpeg"  # Provide the path to your input image
output_dir = "./"  # Provide the directory where the output image will be saved
remove_background(input_path, output_dir)

