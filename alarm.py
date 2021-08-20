import datetime
import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

sl_default_ = datetime.timedelta(hours=8, minutes=0, seconds=0)
sl_new = sl_default_ - datetime.timedelta(hours=0, minutes=random.randint(1,10), seconds=random.randint(1,59))
session_lifetime_ = "Session Lifetime: 0"+str(sl_new)

sit_default_ = datetime.timedelta(hours=0, minutes=8, seconds=0)
sit_new = sit_default_ - datetime.timedelta(hours=0, minutes=0, seconds=random.randint(28,82))
session_idle_timeout_ = "Session Idle Timeout: 0"+str(sit_new)


########## 改 ##########
ne_time_ = 'NE Time: {dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'.format(dt = datetime.datetime.now())
########## 改 ##########
enb_ = "600698"
########## 改 ##########
guln_ = "GULN"


time_and_session_ = ne_time_ +"  "+ session_lifetime_ +"  "+ session_idle_timeout_

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


def guln(text):
    x, y = 338, 133
    y -= 13
    color = (255, 255, 255)
    font = ImageFont.truetype('font/ArialNova-Bold.ttf', 58)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("guln = success")


def tas(text):
    x, y = 337, 218
    y -= 4
    color = (255, 255, 255)
    font = ImageFont.truetype('font/microsoft-sans-serif/Microsoft-Sans-Serif-Regular-font.ttf', 18)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("guln = success")


enb(enb_)
guln(guln_)
tas(time_and_session_)

image.save("Output/Alarm.png")
