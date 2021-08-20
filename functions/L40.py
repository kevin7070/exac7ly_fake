import random
import decimal

from PIL import ImageFont


def speed_uplink_(draw):
    text = str(float(decimal.Decimal(random.randrange(90, 110)) / 10))
    x, y = 624, 230
    y -= 2
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Gauge-Mono-Regular.ttf', 120)

    bg_color = (26, 27, 46)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )


def speed_downlink_(draw):
    text = str(float(decimal.Decimal(random.randrange(850, 990)) / 10))
    x, y = 341, 230
    y -= 2
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Gauge-Mono-Regular.ttf', 120)

    bg_color = (26, 27, 46)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )


def battery_(text, draw):
    x, y = 808, 22
    y -= 9
    color = (204, 204, 204)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 40)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )


def hour_(text, draw):
    x, y = 929, 21
    y -= 9
    color = (204, 204, 204)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 42)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )


def min_(text, draw):
    x, y = 986, 21
    y -= 9
    color = (204, 204, 204)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 42)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )


def enb_(text, draw):
    x, y = 91, 282
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def cid_(text, draw):
    x, y = 329, 282
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def pci_(text, draw):
    x, y = 475, 282
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def rsrp_(draw):
    text = str(random.randrange(-68, -50))
    x, y = 112, 331
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def rsrq_(draw):
    text = str(random.randrange(-11, -5))
    x, y = 343, 331
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def snr_(draw):
    text = str(round(random.randrange(201, 294) * 0.1, 2))
    x, y = 552, 331
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def rssi_(draw):
    text = str(random.randrange(-69, -61))
    x, y = 991, 331
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def gps_acc_(draw):
    text = str(random.randrange(3, 9)) + "m"
    x, y = 988, 429
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def hight_(draw):
    text = str(round(random.randint(200, 400)))
    x, y = 130, 478
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def altitude_(draw):
    text = str(round(random.randint(200, 400)))
    x, y = 561, 478
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def ul_(draw):
    text = str(random.randrange(100, 160))
    x, y = 239, 526
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def dl_(draw):
    text = str(random.randrange(1000, 1600))
    x, y = 753, 526
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def serving_(draw):
    text = str(random.randrange(10, 20))
    x, y = 592, 623
    y -= 7
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 31)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def longitude_(draw):
    longitude_prefix = "114.25"
    longitude_last_two_numbers = random.randrange(10, 99, 3)
    text = longitude_prefix + str(longitude_last_two_numbers)
    x, y = 271, 380
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def latitude_(draw):
    latitude_prefix = "22.323"
    latitude_last_two_numbers = random.randrange(10, 99, 3)
    text = latitude_prefix + str(latitude_last_two_numbers)
    x, y = 784, 380
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def cellid_(text, draw):
    x, y = 327, 716
    y -= 4
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def ci_(text, draw):
    x, y = 471, 716
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x - 25, y - 2, x + w + 10, y + h - 2), fill=bg_color)

    draw.text(
        (x, y), text, color, anchor="mt", font=font
    )


def serTime_(text, draw):
    x, y = 10, 716
    y -= 4
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def level_(draw):
    text = str(random.randrange(-60, -42))
    x, y = 665, 716  # object postition "command + T" in photoshop
    y -= 4
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def qual_(draw):
    text = str(random.randrange(-9, -6))
    x, y = 777, 716  # object postition "command + T" in photoshop
    y -= 4
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )
