from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def enb_(text, draw):
    x, y = 59, 274
    y -= 8
    color = (0, 0, 0)
    font = ImageFont.truetype('font/arialn.ttf', 20)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )


image = Image.open("lmt/rtwp/lte/2021-08-11_143412.png")
draw = ImageDraw.Draw(image)

text = "14:33:44(459)"
enb_(text, draw)

image.save("Output/RTWP.png")