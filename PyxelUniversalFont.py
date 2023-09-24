import pyxel
import os
import platform
import subprocess
import sys

from src.utils import get_pixel_representation, list_font_files

class Writer:
    def __init__(self, font_name) -> None:
        self.font_path = f'fonts/{font_name}.ttf'
        print(self.font_path)
        self.lib = dict()
        
    def draw(self, x, y, text, font_size=16, font_color=0, background_color=7):
        if not text in self.lib:
            pixels = get_pixel_representation(
                text = text,
                font_path = self.font_path,
                font_size = font_size,
                font_color = font_color,
                background_color = background_color,
            )
            self.lib[text] = pixels
        else:
            pixels = self.lib[text]
        for y_number, raw in enumerate(pixels):
            for x_number, pixel_color in enumerate(raw):
                pyxel.pset(
                    x = x + x_number,
                    y = y + y_number,
                    col = pixel_color,
                )

def get_available_fonts():
    return list_font_files("fonts")
        
def get_writers():
    writers = dict()
    for font_name in get_available_fonts():
        writers[font_name] = Writer(
            font_name=font_name,
        )
    return writers

def edit_fonts(path="fonts"):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.run(["open", path])
    elif platform.system() == "Linux":
        subprocess.run(["xdg-open", path])
    else:
        raise ValueError("Unsupported OS")
    
if __name__ == "__main__":
    if sys.argv[1] == "edit":
        edit_fonts()