import random
import datetime

from PIL import ImageFont


def enb_(text, draw):
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


def guln_(text, draw):
    x, y = 338, 133
    y -= 13
    color = (255, 255, 255)
    font = ImageFont.truetype('font/ArialNova-Bold.ttf', 58)

    draw.text(
        (x, y), text, color, font=font
    )


def tas_(hour, minute, second, default_date, draw):
    sl_default_ = datetime.timedelta(hours=8, minutes=0, seconds=0)
    sl_new = sl_default_ - \
        datetime.timedelta(hours=0, minutes=random.randint(
            1, 10), seconds=random.randint(1, 59))
    session_lifetime_ = "Session Lifetime: 0" + str(sl_new)
    sit_default_ = datetime.timedelta(hours=0, minutes=8, seconds=0)

    sit_new = sit_default_ - \
        datetime.timedelta(hours=0, minutes=0, seconds=random.randint(28, 82))
    session_idle_timeout_ = "Session Idle Timeout: 0" + str(sit_new)

    default_ne_time_ = 'NE Time: {dt.year}-{dt.month}-{dt.day} '.format(
        dt=default_date)
    ne_time_ = default_ne_time_ + f"{hour}:{minute}:{second}"

    text = ne_time_ + "  " + session_lifetime_ + "  " + session_idle_timeout_

    x, y = 337, 218
    y -= 4
    color = (255, 255, 255)
    font = ImageFont.truetype(
        'font/microsoft-sans-serif/Microsoft-Sans-Serif-Regular-font.ttf', 18)

    draw.text(
        (x, y), text, color, font=font
    )
