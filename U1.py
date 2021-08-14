import decimal
import random
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

battery_ = "80"  # range from 70-87
hour_, min_ = "15", "17"
sector_number = "1"
cid_, psc_ = "45821", "226"

speed_downlink_ = str(float(decimal.Decimal(random.randrange(50, 80)) / 10))
speed_uplink_ = str(float(decimal.Decimal(random.randrange(3, 50)) / 10))

image = Image.open("U1_Images/" + "PSC" + ".png")
draw = ImageDraw.Draw(image)

speed_test_image = Image.open(
    "U1_Images/" + str(random.randint(1, 10)) + ".png")
speed_test_draw = ImageDraw.Draw(speed_test_image)


def speed_uplink(text):
    x, y = 624, 230  # object position "command + T" in photoshop
    y -= 2
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Gauge-Mono-Regular.ttf', 120)

    bg_color = (26, 27, 46)
    w, h = font.getsize(text)

    speed_test_draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    speed_test_draw.text(
        (x, y), text, color, font=font
    )

    return print("speed_uplink = Success")


def speed_downlink(text):
    x, y = 341, 230  # object position "command + T" in photoshop
    y -= 2
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Gauge-Mono-Regular.ttf', 120)

    bg_color = (26, 27, 46)
    w, h = font.getsize(text)

    speed_test_draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    speed_test_draw.text(
        (x, y), text, color, font=font
    )

    return print("speed_downlink = Success")


def battery(text):
    x, y = 808, 22  # object position "command + T" in photoshop
    y -= 9
    color = (204, 204, 204)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 40)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )

    speed_test_draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    speed_test_draw.text(
        (x, y), text, color, font=font
    )

    return print("Battery = Success")


def hour(text):
    x, y = 929, 21  # object position "command + T" in photoshop
    y -= 9
    color = (204, 204, 204)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 42)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )

    speed_test_draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    speed_test_draw.text(
        (x, y), text, color, font=font
    )

    return print("Hour = Success")


def min(text):
    x, y = 986, 21  # object position "command + T" in photoshop
    y -= 9
    color = (204, 204, 204)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 42)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)

    draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    draw.text(
        (x, y), text, color, font=font
    )

    speed_test_draw.rectangle((x, y, x + w, y + h), fill=bg_color)
    speed_test_draw.text(
        (x, y), text, color, font=font
    )

    return print("Min = Success")


def rnc(text):
    x, y = 95, 282  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("RNC = Success")


def cid(text):
    x, y = 274, 282  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("CID = Success")


def psc(text):
    x, y = 533, 282  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("PCI = Success")


def rsrp(text):
    x, y = 112, 331  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("RSRP = Success")


def gps_acc(text):
    x, y = 988, 429  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("GPS Acc = Success")


def hight(text):
    x, y = 130, 478  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("Hight = Success")


def altitude(text):
    x, y = 561, 478  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("Altitude = Success")


def ul(text):
    x, y = 254, 526  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("UL = Success")


def dl(text):
    x, y = 781, 526  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("DL = Success")


def serving(text):
    x, y = 592, 623  # object position "command + T" in photoshop
    y -= 7
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 31)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("UL = Success")


def longitude(text):
    x, y = 345, 380  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("longitude = Success")


longitude_prefix = "114.25"
longitude_last_two_numbers = random.randrange(10, 99, 3)
longitude(longitude_prefix + str(longitude_last_two_numbers))


def latitude(text):
    x, y = 857, 380  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (72, 72, 72)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("latitude = Success")


latitude_prefix = "22.323"
latitude_last_two_numbers = random.randrange(10, 99, 3)
latitude(latitude_prefix + str(latitude_last_two_numbers))


def cellid(text):
    x, y = 327, 716  # object postition "command + T" in photoshop
    y -= 4
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("CELLID = Success")


def ci(text):
    x, y = 453, 716  # object postition "command + T" in photoshop
    y -= 4
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("CI = Success")


def serTime(text):
    x, y = 10, 716  # object postition "command + T" in photoshop
    y -= 4
    color = (184, 184, 184)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 22)

    bg_color = (16, 16, 16)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("Time = Success")


def level(text):
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

    return print("Time = Success")


# ramdom
rnc_ = str(random.randrange(1, 9))
rnc(rnc_)

rsrp_ = str(random.randrange(-68, -50))
rsrp(rsrp_)

gps_acc_ = str(random.randrange(3, 9)) + "m"
gps_acc(gps_acc_)

serving_ = str(random.randrange(10, 20))
serving(serving_)

hight_and_altitude = str(round(random.randint(20, 40)))
hight(hight_and_altitude)
altitude(hight_and_altitude)

ul_ = str(random.randrange(10, 20))
ul(ul_)

dl_ = str(random.randrange(10, 20))
dl(dl_)

time_ = f"{hour_}:{min_}:{str(random.randrange(10, 59))}"
serTime(time_)

level_ = str(random.randrange(-60, -42))
level(level_)

# LTE Only

if len(cid_) == 1:
    cid_ = cid_ + "   "

if len(psc_) == 2:
    psc_ = psc_ + "   "

if len(psc_) == 1:
    psc_ = psc_ + "      "

battery(battery_)
hour(hour_)
min(min_)
cid(cid_)
cellid_ = cid_ + "-" + rnc_
cellid(cellid_)
psc(psc_)
ci(psc_)

speed_downlink(speed_downlink_)
speed_uplink(speed_uplink_)

image.save(f"./Output/U1_S{sector_number}.png")
time.sleep(2)
speed_test_image.save(f"./Output/U1_S{sector_number}_Speedtest.png")
