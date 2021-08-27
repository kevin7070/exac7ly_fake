from PIL import ImageFont

def enb_(text, draw):
    x, y = 301, 11
    y -= 5
    color = (0, 0, 0)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 20)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )