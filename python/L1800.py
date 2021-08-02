from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import random

image = Image.open("L8_test.png")
draw = ImageDraw.Draw(image)


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
    x, y = 329, 282  # object position "command + T" in photoshop
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
    x, y = 487, 282  # object position "command + T" in photoshop
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
    x, y = 343, 331  # object position "command + T" in photoshop
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
    x, y = 268, 526  # object position "command + T" in photoshop
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
    x, y = 768, 526  # object position "command + T" in photoshop
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

def longitude(text):
    x, y = 271, 380  # object position "command + T" in photoshop
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
    x, y = 784, 380  # object position "command + T" in photoshop
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

# def cellid(text):
#     x, y = 784, 374  # object postition "command + T" in photoshop
#     y -= 3
#     color = (184, 184, 184)
#     font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

#     bg_color = (16, 16, 16)
#     w, h = font.getsize(text)
#     draw.rectangle((x, y, x + w, y + h), fill=bg_color)

#     draw.text(
#         (x, y), text, color, font=font
#     )

#     # image.save("output.png")

#     return print("CELLID = Success")


# def ci(text):
#     x, y = 601, 1060  # object postition "command + T" in photoshop
#     y -= 3
#     color = (184, 184, 184)
#     font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

#     bg_color = (16, 16, 16)
#     w, h = font.getsize(text)
#     draw.rectangle((x, y, x + w, y + h), fill=bg_color)

#     draw.text(
#         (x, y), text, color, font=font
#     )

#     # image.save("output.png")

#     return print("CI = Success")

battery_ = "73"
hour_ = "15"
min_ = "56"
enb_ = "602938"
cid_ = "1"
pci_ = "11"

# ramdom
rsrp_ = str(random.randrange(-68, -50))
rsrp(rsrp_)

rsrq_ = str(random.randrange(-11, -5))
rsrq(rsrq_)

snr_ = str(round(random.randrange(101, 114)*0.1, 2))
snr(snr_)

rssi_ = str(random.randrange(-69, -61))
rssi(rssi_)

gps_acc_ = str(random.randrange(3, 9)) + "m"
gps_acc(gps_acc_)

hight_and_altitude = str(round(random.randint(200, 400)))
hight(hight_and_altitude)
altitude(hight_and_altitude)

ul_ = str(random.randrange(3, 9))
ul(ul_)
dl_ = str(random.randrange(100, 200))
dl(dl_)

# LTE Only
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
# cellid(enb_ + "..")
pci(pci_)
# ci(pci_)

image.save("output.png")
