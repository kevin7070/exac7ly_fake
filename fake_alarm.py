from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

enb_ = "600698"

image = Image.open("lmt/alarm/default.png")
draw = ImageDraw.Draw(image)


def enb(text):
    x, y = 34, 88
    y -= 8
    color = (0, 0, 0)
    font = ImageFont.truetype('font/Segoe-UI-Historic.ttf', 20)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )

    return print("enb = success")


enb(enb_)

image.save("Output/Alarm.png")
