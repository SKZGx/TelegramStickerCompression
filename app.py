from flask import Flask
import os
import imageio
from pathlib import Path

app = Flask(__name__)

input_folder = 'input'
output_folder = 'output'
max_file_size = 511 * 1024  # 511 KB in bytes

def convert_to_webp(input_file, output_file):
    img = imageio.imread(input_file)
    # Save the image in WebP format without losing quality
    imageio.imwrite(output_file, img, format='webp', quality=100)

@app.route('/')
def convert_images_to_webp():
    # Create folders if they don't exist
    Path(input_folder).mkdir(parents=True, exist_ok=True)
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Loop through image files in the input folder
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")

        # Check if the file is larger than 511 KB
        if os.path.getsize(input_file_path) > max_file_size:
            # Convert the image to WebP
            convert_to_webp(input_file_path, output_file_path)

    return "Images converted to WebP successfully!"

if __name__ == '__main__':
    app.run(debug=True)
