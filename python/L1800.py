from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import random

image = Image.open("L8_test.png")
draw = ImageDraw.Draw(image)

def time(text):
    x, y = 929, 15  # object position "command + T" in photoshop
    y -= 3
    color = (204, 204, 204)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 42)

    bg_color = (0, 0, 0)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    return print("Time = Success")


def enb(text):
    x, y = 90, 277  # object position "command + T" in photoshop
    y -= 3
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
    x, y = 328, 277  # object position "command + T" in photoshop
    y -= 3
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
    x, y = 485, 277  # object position "command + T" in photoshop
    y -= 3
    color = (255, 255, 255)
    font = ImageFont.truetype('font/Roboto/Roboto-Regular.ttf', 36)

    bg_color = (40, 40, 40)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )

    # image.save("output.png")

    return print("PCI = Success")


def longitude(text):
    x, y = 269, 375  # object position "command + T" in photoshop
    y -= 3
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
    x, y = 783, 375  # object position "command + T" in photoshop
    y -= 3
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


time_ = "15:56"
enb_ = "602938"
cid_ = "1"
pci_ = "11"

# LTE Only
if len(cid_) == 1:
    cid_ = cid_ + "   "

if len(pci_) == 2:
    pci_ = pci_ + "   "
    if len(pci_) == 1:
        pci_ = pci_ + "      "

time(time_)
enb(enb_)
cid(cid_)
# cellid(enb_ + "..")
pci(pci_)
# ci(pci_)

image.save("output.png")
