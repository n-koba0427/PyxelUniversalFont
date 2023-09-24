from PIL import Image, ImageDraw, ImageFont
import numpy as np

import os

def list_font_files(directory):
    result = []
    with os.scandir(directory) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                if entry.name.endswith('.ttf') or entry.name.endswith('.otf'):
                    result.append(entry.name.split(".")[0])
    return result

def get_pixel_representation(
        text, 
        font_path, 
        font_size,
        font_color=0,
        background_color=7,
        show_image=False,
    ):
    font = ImageFont.truetype(font_path, font_size)
    image = Image.new('RGB', (font_size*len(text), font_size), color="white")
    draw = ImageDraw.Draw(image)

    draw.text((0, 0), text, font=font, fill='black')

    pixels = np.array(image.getdata())
    
    pixels = np.where(pixels.sum(axis=-1) < (255*3/2), font_color, background_color)
    pixels = pixels.reshape((font_size, font_size*len(text)))
    
    if show_image:
        image.show()
    
    return pixels

if __name__ == "__main__":
    get_pixel_representation(
        text="テスト/試験運用",
        font_path="fonts/IPA_Gothic.ttf",
        font_size=48,
        show_image=True
    )