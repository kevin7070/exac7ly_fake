import random
from PIL import ImageFont


def time_(text, draw):
    x, y = 1041, 76
    y -= 8
    color = (229, 229, 229)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 38)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def n1pci_(text, la, lo, draw):
    x, y = 304, 1726
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w + 40, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # la
    text = la
    x, y = 963, 932
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # lo
    text = lo
    x, y = 963, 1034
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # rsrp
    text = str(round(random.uniform(-55.55, -65.65), 2))
    x, y = 304, 2101
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # rsrq
    text = str(round(random.uniform(-10.01, -10.99), 2))
    x, y = 304, 2176
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # sinr
    text = str(round(random.uniform(36.01, 37.99), 2))
    x, y = 303, 2251
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def n1ltepci_(text, la, lo, draw):
    x, y = 303, 1651
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w + 40, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # la
    text = la
    x, y = 963, 932
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # lo
    text = lo
    x, y = 963, 1034
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # rsrp
    text = str(round(random.uniform(-55.55, -65.65), 2))
    x, y = 303, 1726
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # rsrq
    text = str(round(random.uniform(-3.01, -3.99), 2))
    x, y = 303, 1801
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # rssi
    text = str(round(random.uniform(-13.01, -13.99), 2))
    x, y = 303, 1876
    y -= 8
    color = (117, 117, 117)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 34)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def n1speed_(draw):
    # downlink
    text = str(random.randint(135, 175))
    x, y = 382, 313
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Gauge-Mono-Regular.ttf', 134)

    bg_color = (26, 27, 47)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # uplink
    text = str(round(random.uniform(55.55, 75.75), 1))
    x, y = 691, 314
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Gauge-Mono-Regular.ttf', 134)

    bg_color = (26, 27, 47)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )
