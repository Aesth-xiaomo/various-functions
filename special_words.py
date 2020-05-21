'''
依赖，需要安装Pillow
pip install Pillow
'''
from PIL import Image, ImageDraw, ImageFont
import sys  # 判断参数个数，可以不要
import os  # 判断文件是否存在，可以不要

image_path = "2.jpg"
font_path = "1.TTF"
text = "你若盛开，清风自来！"
font_size = 8

###########这几个判断用来支持命令行参数#######
if len(sys.argv) > 1:
    path = sys.argv[1]
    if os.path.exists(path):
        image_path = path

if len(sys.argv) > 2:
    path = sys.argv[2]
    if os.path.exists(path):
        font_path = path

if len(sys.argv) > 3:
    text = sys.argv[3]

if len(sys.argv) > 4:
    if sys.argv[4].isdigit():
        font_size = int(sys.argv[4])


#############################################

def generator_new_image(image_path, font_path, text, font_size):
    img_origin = Image.open(image_path)
    img_array = img_origin.load()
    img_new = Image.new("RGB", img_origin.size, (0, 0, 0))
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype(font_path, font_size)

    index = 0
    for y in range(0, img_origin.size[1], font_size):
        for x in range(0, img_origin.size[0], font_size):
            index = index % len(text)
            draw.text((x, y), text[index], font=font, fill=img_array[x, y], direction=None)
            index = index + 1

    img_new.convert("RGB").save("4.jpg")


generator_new_image(image_path, font_path, text, font_size)
