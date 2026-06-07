from PIL import Image
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

def process_images(input_dir, output_dir):
    input = Path(f"{input_dir}")
    output = Path(f"{output_dir}")
    output.mkdir(exist_ok=True)
    error = False
    for ppm_img in input.glob("*.ppm"):
        try:
            with Image.open(ppm_img) as img:
                png_img = output / f"{ppm_img.stem}.png"
                img.save(png_img, "PNG")
                print(f"Successfully converted: {ppm_img.name}")
        except Exception as e:
            print(e)
            error = True
    return error

def main():
    left_in = Path(os.getenv("left_input_path"))
    left_out = Path(os.getenv("left_output_path"))
    right_in = Path(os.getenv("right_input_path"))
    right_out = Path(os.getenv("right_output_path"))
    left_error = process_images(left_in, left_out)
    right_error = process_images(right_in, right_out)
    if not left_error and not right_error:
        print("All images successfully processed")
    else:
        print("Image processing unsuccessful")

if __name__ == '__main__':
    main()


