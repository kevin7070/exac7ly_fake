import decimal
import random
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

battery_ = "80"  # range from 70-87
hour_, min_ = "11", "30"
enb_ = "601111"
cid_, pci_ = "3", "1"

speed_downlink_ = str(float(decimal.Decimal(random.randrange(300, 400)) / 10))
speed_uplink_ = str(float(decimal.Decimal(random.randrange(200, 230)) / 10))

image = Image.open("L1_Images/" + "PCI" + ".png")
draw = ImageDraw.Draw(image)

speed_test_image = Image.open(
    "L1_Images/" + str(random.randint(1, 10)) + ".png")
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


def enb(text):
    x, y = 91, 282  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("eNB = Success")


def cid(text):
    x, y = 332, 282  # object position "command + T" in photoshop
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


def pci(text):
    x, y = 475, 282  # object position "command + T" in photoshop
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


def rsrq(text):
    x, y = 342, 331  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("RSRQ = Success")


def snr(text):
    x, y = 552, 331  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("SNR = Success")


def rssi(text):
    x, y = 991, 331  # object position "command + T" in photoshop
    y -= 8
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("RSSI = Success")


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


def qual(text):
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

    return print("Time = Success")


# ramdom
rsrp_ = str(random.randrange(-68, -50))
rsrp(rsrp_)

rsrq_ = str(random.randrange(-11, -5))
rsrq(rsrq_)

snr_ = str(round(random.randrange(201, 294) * 0.1, 2))
snr(snr_)

rssi_ = str(random.randrange(-69, -61))
rssi(rssi_)

serving_ = str(random.randrange(10, 20))
serving(serving_)

time_ = f"{hour_}:{min_}:{str(random.randrange(10, 59))}"
serTime(time_)

level_ = str(random.randrange(-60, -42))
level(level_)

qual_ = str(random.randrange(-9, -6))
qual(qual_)

# LTE Only
sector_number = cid_[-1]

if len(cid_) == 1:
    cid_ = cid_ + "   "

if len(pci_) == 2:
    pci_ = pci_ + "   "

if len(pci_) == 1:
    pci_ = pci_ + "      "

battery(battery_)
hour(hour_)
min(min_)
enb(enb_)
cid(cid_)
cellid(enb_)
pci(pci_)
ci(pci_)

speed_downlink(speed_downlink_)
speed_uplink(speed_uplink_)

image.save(f"./Output/L1_S{sector_number}.png")
time.sleep(2)
speed_test_image.save(f"./Output/L1_S{sector_number}_Speedtest.png")
