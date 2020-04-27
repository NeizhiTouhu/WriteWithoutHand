from PIL import Image, ImageFont
import setuptools, wheel, pytest
from handright import Template, handwrite
try:
    file_object = open('text.txt', encoding='utf-8', errors='ignore')
    text = file_object.read()
except FileNotFoundError:
    print("没有找到text.txt，请将要手写的内容写入text.txt并将其放置在与exe程序相同的目录下")
else:
    words = text.rstrip()
    num_words = len(words)
    if num_words == 0:
        print("text.txt无内容，请将要手写的内容写入text.txt并保！存！")
    else:
        template = Template(
            background=Image.new(mode="1", size=(3000, 5000), color=1),
            font_size=100,
            font=ImageFont.truetype("handwrite.ttf"),
            line_spacing=110,
            fill=0,  # 字体“颜色”
            left_margin=100,
            top_margin=100,
            right_margin=100,
            bottom_margin=100,
            word_spacing=-15,
            line_spacing_sigma=2,  # 行间距随机扰动
            font_size_sigma=2,  # 字体大小随机扰动
            word_spacing_sigma=2,  # 字间距随机扰动
            end_chars="，。.,abcdefghigklmnopqrstuvwxyz",  # 防止特定字符因排版算法的自动换行而出现在行首
            perturb_x_sigma=2,  # 笔画横向偏移随机扰动
            perturb_y_sigma=2,  # 笔画纵向偏移随机扰动
            perturb_theta_sigma=0.05,  # 笔画旋转偏移随机扰动
        )
        images = handwrite(text, template)
        for i, im in enumerate(images):
            assert isinstance(im, Image.Image)
            im.show()
            im.save("{}.png".format(i))