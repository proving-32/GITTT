from PIL import Image
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. Error: {e}")
        return
    
    image = resize_image(image, new_width)
    image = grayify(image)
    
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index+img_width)] for index in range(0, ascii_str_len, img_width)])
    
    return ascii_img

def main(image_path, new_width=100):
    ascii_image = convert_image_to_ascii(image_path, new_width)
    if ascii_image:
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
        print("ASCII image saved to ascii_image.txt")


image_path = r"C:\Users\pro\Documents\terget\from"
main(image_path)
