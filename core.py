import random
# import datetime

from PIL import Image
from PIL import ImageDraw

import functions.L1 as L1
# import functions.L3 as L3
# import functions.L8 as L8
# import functions.L40 as L40
# import functions.U1 as U1
# import functions.U8 as U8

# collect site number for eNB
enb = str(input(f"請輸入Site No.:"))
if len(enb) > 3:
    enb = "60" + enb
else:
    enb = "600" + enb

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
sector_number = int(input(f"有幾多個 {band} Sector？"))

todo_list = []
for i in range(0, sector_number):
    battery = str(random.randrange(80, 87))
    d_hour = int(random.randrange(15, 19))
    d_minute = int(random.randrange(10, 59))
    d_second = int(random.randrange(10, 59))
    hms = f"{d_hour}:{d_minute}:{d_second}"

    input_cid = str(input(f"請輸入Sector {i+1} CID："))
    input_pci_psc = str(input(f"請輸入第 {i+1} PCI/PSC："))

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

    default_seconds = str(random.randrange(10, 59))
    image.save(f"./Output/{band}-{hour}-{minute}-{second}.png")
