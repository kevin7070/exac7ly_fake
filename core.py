import random
# import datetime

from PIL import Image
from PIL import ImageDraw

import functions.L1 as L1
import functions.L3 as L3
# import functions.L8 as L8
import functions.L40 as L40
# import functions.U1 as U1
# import functions.U8 as U8

d_hour = int(random.randrange(15, 19))
d_minute = int(random.randrange(10, 59))

# collect site number for eNB
enb = ""
while len(enb) < 3 or len(enb) > 4:
    enb = str(input(f"請輸入Site No.:"))
    continue
if len(enb) == 3:
    enb = "600" + enb
else:
    enb = "60" + enb

# bands pool
bands = {'L1', 'L3', 'L8', 'L40', 'U1', 'U8'}
# collect band
band = "default"
while band not in bands:
    band = str(input(
        """你想做邊個 Band？
L1  = LTE2100
L3  = LTE1800
L8  = LTE900
L40 = LTE2300
U1  = UMTS2100
U8  = UMTS900

請輸入代號："""
    ))
    continue


# number of sectors
sector_number = ""
while sector_number == "":
    sector_number = int(input(f"有幾多個 {band} Sector？"))
    continue


todo_list = []
for i in range(0, sector_number):
    battery = str(random.randrange(80, 87))
    d_second = int(random.randrange(10, 59))
    hms = f"{d_hour}:{d_minute}:{d_second}"

    input_cid = ""
    input_pci_psc = ""

    while input_cid == "":
        input_cid = str(input(f"請輸入Sector {i+1} CID："))
        continue
    while input_pci_psc == "":
        input_pci_psc = str(input(f"請輸入Sector {i+1} PCI/PSC："))
        continue

    d_minute = d_minute + int(random.randrange(1, 3))
    if d_minute >= 60:
        d_hour = d_hour + 1
        d_minute = d_minute - 60

    todo_list.append([
        str(battery),
        str(d_hour),
        str(d_minute),
        str(d_second),
        str(hms),
        enb,
        input_cid,
        input_pci_psc
    ])

if band == "L1":
    for (battery, hour, minute, second, hms, enb, cid, pci_psc) in todo_list:
        image = Image.open(f"{band}_Images/" + "PCI" + ".png")
        draw = ImageDraw.Draw(image)
        L1.battery_(battery, draw)
        L1.hour_(hour, draw)
        L1.min_(minute, draw)
        L1.enb_(enb, draw)
        L1.cid_(cid, draw)
        L1.pci_(pci_psc, draw)
        L1.rsrp_(draw)
        L1.rsrq_(draw)
        L1.snr_(draw)
        L1.rssi_(draw)
        L1.serving_(draw)
        L1.cellid_(enb, draw)
        L1.ci_(pci_psc, draw)
        L1.serTime_(hms, draw)
        L1.level_(draw)
        L1.qual_(draw)

        image.save(f"./Output/{band}-{hour}-{minute}-{second}.png")

        speed_test_image = Image.open(
            f"{band}_Images/" + str(random.randint(1, 10)) + ".png")
        speed_test_draw = ImageDraw.Draw(speed_test_image)
        L1.battery_(battery, speed_test_draw)
        L1.hour_(hour, speed_test_draw)
        L1.min_(minute, speed_test_draw)
        L1.speed_downlink_(speed_test_draw)
        L1.speed_uplink_(speed_test_draw)

        speed_test_image.save(f"./Output/{band}-{hour}-{minute}-{second}-CT.png")

elif band == "L3":
    for (battery, hour, minute, second, hms, enb, cid, pci_psc) in todo_list:
        image = Image.open(f"{band}_Images/" + "PCI" + ".png")
        draw = ImageDraw.Draw(image)
        L3.battery_(battery, draw)
        L3.hour_(hour, draw)
        L3.min_(minute, draw)
        L3.enb_(enb, draw)
        L3.cid_(cid, draw)
        L3.pci_(pci_psc, draw)
        L3.rsrp_(draw)
        L3.rsrq_(draw)
        L3.snr_(draw)
        L3.rssi_(draw)
        L3.serving_(draw)
        L3.cellid_(enb, draw)
        L3.ci_(pci_psc, draw)
        L3.serTime_(hms, draw)
        L3.level_(draw)
        L3.qual_(draw)

        L3.gps_acc_(draw)
        L3.hight_(draw)
        L3.altitude_(draw)
        L3.ul_(draw)
        L3.dl_(draw)
        L3.longitude_(draw)
        L3.latitude_(draw)

        image.save(f"./Output/{band}-{hour}-{minute}-{second}.png")

        speed_test_image = Image.open(
            f"{band}_Images/" + str(random.randint(1, 10)) + ".png")
        speed_test_draw = ImageDraw.Draw(speed_test_image)
        L3.battery_(battery, speed_test_draw)
        L3.hour_(hour, speed_test_draw)
        L3.min_(minute, speed_test_draw)
        L3.speed_downlink_(speed_test_draw)
        L3.speed_uplink_(speed_test_draw)

        speed_test_image.save(f"./Output/{band}-{hour}-{minute}-{second}-CT.png")

elif band == "L40":
    for (battery, hour, minute, second, hms, enb, cid, pci_psc) in todo_list:
        image = Image.open(f"{band}_Images/" + "PCI" + ".png")
        draw = ImageDraw.Draw(image)
        L40.battery_(battery, draw)
        L40.hour_(hour, draw)
        L40.min_(minute, draw)
        L40.enb_(enb, draw)
        L40.cid_(cid, draw)
        L40.pci_(pci_psc, draw)
        L40.rsrp_(draw)
        L40.rsrq_(draw)
        L40.snr_(draw)
        L40.rssi_(draw)
        L40.serving_(draw)
        L40.cellid_(enb, draw)
        L40.ci_(pci_psc, draw)
        L40.serTime_(hms, draw)
        L40.level_(draw)
        L40.qual_(draw)

        L40.gps_acc_(draw)
        L40.hight_(draw)
        L40.altitude_(draw)
        L40.ul_(draw)
        L40.dl_(draw)
        L40.longitude_(draw)
        L40.latitude_(draw)

        image.save(f"./Output/{band}-{hour}-{minute}-{second}.png")

        speed_test_image = Image.open(
            f"{band}_Images/" + str(random.randint(1, 10)) + ".png")
        speed_test_draw = ImageDraw.Draw(speed_test_image)
        L40.battery_(battery, speed_test_draw)
        L40.hour_(hour, speed_test_draw)
        L40.min_(minute, speed_test_draw)
        L40.speed_downlink_(speed_test_draw)
        L40.speed_uplink_(speed_test_draw)

        speed_test_image.save(f"./Output/{band}-{hour}-{minute}-{second}-CT.png")