import os
import subprocess
from termcolor import colored

def save_image(filename, content):
    """Saves binary content as an image file."""
    with open(filename, "wb") as img_file:
        img_file.write(content)
    print(colored(f"Image saved as {filename}.", "green"))

    # Open the image with the default application
    open_image(filename)

def open_image(filename):
    """Opens the given image file with the default application."""
    if os.name == "nt":  # Windows
        os.startfile(filename)
    elif os.uname().sysname == "Darwin":  # macOS
        subprocess.call(["open", filename])
    else:  # Linux and others
        subprocess.call(["xdg-open", filename])