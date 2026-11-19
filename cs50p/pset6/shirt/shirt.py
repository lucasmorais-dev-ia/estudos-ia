import os
import sys

from PIL import Image, ImageOps

def main():
    try:
        photo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_name, input_ext = os.path.splitext(sys.argv[1])
    output_name, output_ext = os.path.splitext(sys.argv[2])

    valid = [".jpg", ".jpeg", ".png"]
    if input_ext.lower() not in valid:
        sys.exit("Invalid input")
    if output_ext.lower() not in valid:
        sys.exit("Invalid output")
    if input_ext.lower() != output_ext.lower():
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()