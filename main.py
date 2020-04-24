from PIL import Image, ImageFont

from handright import Template, handwrite


file_object = open('text.txt', encoding='utf-8', errors='ignore')
text = file_object.read()

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