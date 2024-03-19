# Image Converter to WebP

This is a simple Flask application that converts images in a specified folder to the WebP format if they exceed a certain file size.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
   ```pip install -r requirements.txt```

# Usage
1. Place your images in the input folder.
2. Run the Flask application: ```python app.py```
3. Open your web browser
4. The images exceeding the specified file size will be converted to WebP format and saved in the output folder.

# Configuration
You can configure the following parameters in the app.py file:

* input_folder: Path to the folder containing input images.
* output_folder: Path to the folder where converted images will be saved.
* max_file_size: Maximum file size in bytes. Images exceeding this size will be converted to WebP format.
