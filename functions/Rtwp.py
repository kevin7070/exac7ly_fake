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


def pd_1(text, i, draw):
    text = f"Cell Performance Monitoring({i})-[Detect Interference Local Cell ID:{text}]"
    x, y = 203, 90
    y -= 4
    color = (82, 82, 82)
    font = ImageFont.truetype('font/arial.ttf', 18)

    bg_color = (238, 238, 238)
    w, h = font.getsize(text)
    draw.rectangle((x, y + 4, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def pd_2(text, i, draw):
    text = f"Cell Performance Monitoring({i})-[Detect Interference Local Cell ID:{text}]"
    x, y = 50, 138
    y -= 4
    color = (82, 82, 82)
    font = ImageFont.truetype('font/arial.ttf', 18)

    draw.text(
        (x, y), text, color, font=font
    )