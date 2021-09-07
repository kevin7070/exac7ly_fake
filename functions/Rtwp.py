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


def time_(hour, minute, draw):
    x, y = 39, 180
    y -= 2
    color = (51, 51, 51)
    font = ImageFont.truetype('font/arial.ttf', 12)

    second_of_time = random.randint(10, 40)
    suffix = random.randint(100, 800)

    for i in range(16):
        text = f"{hour}:{minute}:{second_of_time}({suffix})"  # 14:33:44(459)

        bg_color = (255, 255, 255)
        w, h = font.getsize(text)
        draw.rectangle((x, y, x + w, y + h), fill=bg_color)

        draw.text(
            (x, y), text, color, font=font
        )

        second_of_time += 1
        internal_suffix = suffix
        suffix = internal_suffix - random.randint(1, 15)
        y += 21
