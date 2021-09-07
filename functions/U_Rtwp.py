import random
from PIL import ImageFont


def enb_(text, draw):
    x, y = 188, 7
    y -= 6
    color = (0, 0, 0)
    font = ImageFont.truetype('font/Segoe-UI-Historic.ttf', 13)

    bg_color = (255, 255, 255)
    w, h = font.getsize(text)
    draw.rectangle((x, y, x + w, y + h), fill=bg_color)

    draw.text(
        (x, y), text, color, font=font
    )


def pd_1(text, i, draw):
    text = f"Cell RTWP({i})-[Logic Cell ID:{text}]"
    x, y = 135, 60
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)

    draw.text(
        (x, y), text, color, font=font
    )


def pd_2(text, i, draw):
    text = f"Cell RTWP({i})-[Logic Cell ID:{text}]"
    x, y = 33, 92
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)

    draw.text(
        (x, y), text, color, font=font
    )


def time_(hour, minute, draw):
    x, y = 54, 174
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)

    second_of_time = random.randint(10, 40)

    for i in range(17):
        text = f"{hour}:{minute}:{second_of_time}"

        bg_color = (255, 255, 255)
        w, h = font.getsize(text)
        draw.rectangle((x, y + 2, x + w, y + h), fill=bg_color)

        draw.text(
            (x, y), text, color, font=font
        )

        second_of_time += 1
        y += 21


def other_(cid, draw):
    # Cell ID
    text = str(cid)
    x, y = 446, 570
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)
    bg_color = (255, 255, 255)
    w, h = font.getsize(text)

    for i in range(3):
        draw.rectangle((x - 25, y - 2, x + w, y + h), fill=bg_color)
        draw.text(
            (x, y), text, color, anchor="ma", font=font
        )
        y += 21
