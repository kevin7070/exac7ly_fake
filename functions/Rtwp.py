from PIL import ImageFont

def enb_(text, draw):
    x, y = 188, 7
    y -= 3
    color = (51, 51, 51)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 12)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def pd_1(text, i, draw):
    text = f"Cell Performance Monitoring({i})-[Detect Interference Local Cell ID:{text}]"
    x, y = 135, 60
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)

    draw.text(
        (x, y), text, color, font=font
    )


def pd_2(text, i, draw):
    text = f"Cell Performance Monitoring({i})-[Detect Interference Local Cell ID:{text}]"
    x, y = 33, 92
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)

    draw.text(
        (x, y), text, color, font=font
    )


def time_(draw):
    text = "14:33:44(459)"
    x, y = 39, 180
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )