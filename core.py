import random
import datetime

from PIL import Image
from PIL import ImageDraw

import functions.L1 as L1
import functions.L3 as L3
import functions.L8 as L8
import functions.L40 as L40
import functions.U1 as U1
import functions.U8 as U8
import functions.Alarm as A
import functions.Rtwp as R
import functions.U_Rtwp as UR
import functions.N1 as N1

d_hour = int(random.randrange(15, 19))
d_minute = int(random.randrange(10, 59))
d_y = int(input(f"請輸入日期 YYYY："))
d_m = int(input(f"請輸入日期 MM  ："))
d_d = int(input(f"請輸入日期 DD  ："))
default_date = datetime.date(d_y, d_m, d_d)

# collect site number for eNB
site_number = ""
while len(site_number) < 3 or len(site_number) > 4:
    input_site_num = str(input(f"請輸入Site No.\n："))
    site_number = input_site_num.strip()
    continue
if len(site_number) == 3:
    enb = "600" + site_number
else:
    enb = "60" + site_number

# emtpy band list todo
band_list = []

while True:
    # bands pool
    bands = ['L1', 'L3', 'L8', 'L40', 'U8', 'U1', 'N1']
    # collect band
    band = "default"
    while band not in bands:
        band = str.upper(input(
            """你想做邊個 Band？
    L1  = LTE 2100
    L3  = LTE 1800
    L8  = LTE 900
    L40 = LTE 2300
    U8  = UMTS 900
    U1  = UMTS 2100
    N1  = NR 2100

    請輸入代號\n："""
        ))
        continue

    # add band list
    band_list.append(band)

    # number of sectors
    sector_number = ""
    while sector_number == "":
        sector_number = int(input(f"{band}有幾多個Sector？\n："))
        continue

    todo_list = []
    for i in range(1, sector_number + 1):
        if band[0] != 'N':
            battery = str(random.randrange(80, 87))
            d_second = int(random.randrange(10, 59))
            hms = f"{d_hour}:{d_minute}:{d_second}"

            input_cid = ""
            input_pci_psc = ""

            while input_cid == "":
                input_cid = str(input(f"請輸入S{i}的CID\n："))
                continue
            while input_pci_psc == "":
                input_pci_psc = str(input(f"請輸入S{i}的PCI 或PSC\n："))
                continue

            d_minute = d_minute + int(random.randrange(2, 4))
            if d_minute >= 60:
                d_hour = d_hour + 1
                d_minute = d_minute - 50

            todo_list.append([
                str(battery),
                str(d_hour),
                str(d_minute),
                str(d_second),
                str(hms),
                enb,
                input_cid,
                input_pci_psc,
                str(i)
            ])
        else:
            d_minute = d_minute + int(random.randrange(2, 4))
            d_second = int(random.randrange(10, 59))
            hm = str(f"{d_hour}:{d_minute}")

            input_pci = ""
            while input_pci == "":
                input_pci = str(input(f"請輸入S{i} 的PCI\n："))
                continue

            d_minute = d_minute + int(random.randrange(2, 4))
            if d_minute >= 60:
                d_hour = d_hour + 1
                d_minute = d_minute - 50

            todo_list.append([
                str(d_hour),
                str(d_minute),
                str(d_second),
                str(hm),
                input_pci,
                str(i)
            ])

    if band == "L1":
        for (battery, hour, minute, second, hms, enb, cid, pci_psc, i) in todo_list:

            image = Image.open(f"images/{band}_Images/" + "PCI" + ".png")
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

            image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}.png")
            print()

            speed_test_image = Image.open(
                f"images/{band}_Images/" + str(random.randint(1, 10)) + ".png")
            speed_test_draw = ImageDraw.Draw(speed_test_image)
            L1.battery_(battery, speed_test_draw)
            L1.hour_(hour, speed_test_draw)
            L1.min_(minute, speed_test_draw)
            L1.speed_downlink_(speed_test_draw)
            L1.speed_uplink_(speed_test_draw)

            speed_test_image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}-CT.png")

            # RTWP
            lte_image_name = random.randint(1, 20)
            image = Image.open(f"images/rtwp/L/RTWP ({lte_image_name}).png")
            draw = ImageDraw.Draw(image)

            R.enb_(enb, draw)
            local_cell_id = int(cid) - 1

            pd_1_bg = Image.open("images/rtwp/pd_1_bg.png")
            image.paste(pd_1_bg, (134, 58))
            R.pd_1(local_cell_id, i, draw)

            pd_2_bg = Image.open("images/rtwp/pd_2_bg.png")
            image.paste(pd_2_bg, (35, 85))
            R.pd_2(local_cell_id, i, draw)

            R.time_(hour, minute, draw)

            # Table value for Cell ID, 1-1, and 1-3
            one_one = 50
            one_three = 10
            R.other_(local_cell_id, one_one, one_three, draw)

            image.save(f"./Output/{local_cell_id}.png")

    elif band == "L3":
        for (battery, hour, minute, second, hms, enb, cid, pci_psc, i) in todo_list:

            image = Image.open(f"images/{band}_Images/" + "PCI" + ".png")
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

            image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}.png")

            speed_test_image = Image.open(
                f"images/{band}_Images/" + str(random.randint(1, 10)) + ".png")
            speed_test_draw = ImageDraw.Draw(speed_test_image)
            L3.battery_(battery, speed_test_draw)
            L3.hour_(hour, speed_test_draw)
            L3.min_(minute, speed_test_draw)
            L3.speed_downlink_(speed_test_draw)
            L3.speed_uplink_(speed_test_draw)

            speed_test_image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}-CT.png")

            # RTWP
            lte_image_name = random.randint(1, 20)
            image = Image.open(f"images/rtwp/L/RTWP ({lte_image_name}).png")
            draw = ImageDraw.Draw(image)

            R.enb_(enb, draw)
            local_cell_id = int(cid) - 1

            pd_1_bg = Image.open("images/rtwp/pd_1_bg.png")
            image.paste(pd_1_bg, (134, 58))
            R.pd_1(local_cell_id, i, draw)

            pd_2_bg = Image.open("images/rtwp/pd_2_bg.png")
            image.paste(pd_2_bg, (35, 85))
            R.pd_2(local_cell_id, i, draw)

            R.time_(hour, minute, draw)

            # Table value for Cell ID, 1-1, and 1-3
            one_one = 50
            one_three = 8
            R.other_(local_cell_id, one_one, one_three, draw)

            image.save(f"./Output/{local_cell_id}.png")

    elif band == "L40":
        for (battery, hour, minute, second, hms, enb, cid, pci_psc, i) in todo_list:

            image = Image.open(f"images/{band}_Images/" + "PCI" + ".png")
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

            image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}.png")

            speed_test_image = Image.open(
                f"images/{band}_Images/" + str(random.randint(1, 10)) + ".png")
            speed_test_draw = ImageDraw.Draw(speed_test_image)
            L40.battery_(battery, speed_test_draw)
            L40.hour_(hour, speed_test_draw)
            L40.min_(minute, speed_test_draw)
            L40.speed_downlink_(speed_test_draw)
            L40.speed_uplink_(speed_test_draw)

            speed_test_image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}-CT.png")

            # RTWP
            lte_image_name = random.randint(1, 20)
            image = Image.open(f"images/rtwp/L/RTWP ({lte_image_name}).png")
            draw = ImageDraw.Draw(image)

            R.enb_(enb, draw)
            local_cell_id = int(cid) - 1

            pd_1_bg = Image.open("images/rtwp/pd_1_bg.png")
            image.paste(pd_1_bg, (134, 58))
            R.pd_1(local_cell_id, i, draw)

            pd_2_bg = Image.open("images/rtwp/pd_2_bg.png")
            image.paste(pd_2_bg, (35, 85))
            R.pd_2(local_cell_id, i, draw)

            R.time_(hour, minute, draw)

            # Table value for Cell ID, 1-1, and 1-3
            one_one = 100
            one_three = 18
            R.other_(local_cell_id, one_one, one_three, draw)

            image.save(f"./Output/{local_cell_id}.png")

    elif band == "L8":
        for (battery, hour, minute, second, hms, enb, cid, pci_psc, i) in todo_list:

            image = Image.open(f"images/{band}_Images/" + "PCI" + ".png")
            draw = ImageDraw.Draw(image)
            L8.battery_(battery, draw)
            L8.hour_(hour, draw)
            L8.min_(minute, draw)
            L8.enb_(enb, draw)
            L8.cid_(cid, draw)
            L8.pci_(pci_psc, draw)
            L8.rsrp_(draw)
            L8.rsrq_(draw)
            L8.snr_(draw)
            L8.rssi_(draw)
            L8.serving_(draw)
            L8.cellid_(enb, draw)
            L8.ci_(pci_psc, draw)
            L8.serTime_(hms, draw)
            L8.level_(draw)
            L8.qual_(draw)
            L8.gps_acc_(draw)
            L8.hight_(draw)
            L8.altitude_(draw)
            L8.ul_(draw)
            L8.dl_(draw)
            L8.longitude_(draw)
            L8.latitude_(draw)

            image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}.png")

            speed_test_image = Image.open(
                f"images/{band}_Images/" + str(random.randint(1, 10)) + ".png")
            speed_test_draw = ImageDraw.Draw(speed_test_image)
            L8.battery_(battery, speed_test_draw)
            L8.hour_(hour, speed_test_draw)
            L8.min_(minute, speed_test_draw)
            L8.speed_downlink_(speed_test_draw)
            L8.speed_uplink_(speed_test_draw)

            speed_test_image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}-CT.png")

            # RTWP
            lte_image_name = random.randint(1, 20)
            image = Image.open(f"images/rtwp/L/RTWP ({lte_image_name}).png")
            draw = ImageDraw.Draw(image)

            R.enb_(enb, draw)
            local_cell_id = int(cid) - 1

            pd_1_bg = Image.open("images/rtwp/pd_1_bg.png")
            image.paste(pd_1_bg, (134, 58))
            R.pd_1(local_cell_id, i, draw)

            pd_2_bg = Image.open("images/rtwp/pd_2_bg.png")
            image.paste(pd_2_bg, (35, 85))
            R.pd_2(local_cell_id, i, draw)

            R.time_(hour, minute, draw)

            # Table value for Cell ID, 1-1, and 1-3
            one_one = 25
            one_three = 6
            R.other_(local_cell_id, one_one, one_three, draw)

            image.save(f"./Output/{local_cell_id}.png")

    elif band == "U8":
        for (battery, hour, minute, second, hms, enb, cid, pci_psc, i) in todo_list:

            image = Image.open(f"images/{band}_Images/" + "PSC" + ".png")
            draw = ImageDraw.Draw(image)
            U8.battery_(battery, draw)
            U8.hour_(hour, draw)
            U8.min_(minute, draw)
            U8.cid_(cid, draw)
            U8.psc_(pci_psc, draw)
            U8.rsrp_(draw)
            U8.gps_acc_(draw)
            U8.hight_(draw)
            U8.altitude_(draw)
            U8.serving_(draw)
            U8.longitude_(draw)
            U8.latitude_(draw)
            U8.cellid_(enb, draw)
            U8.ci_(pci_psc, draw)
            U8.serTime_(hms, draw)
            U8.rnc_(draw)
            U8.level_(draw)

            image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}.png")

            speed_test_image = Image.open(
                f"images/{band}_Images/" + str(random.randint(1, 10)) + ".png")
            speed_test_draw = ImageDraw.Draw(speed_test_image)
            U8.battery_(battery, speed_test_draw)
            U8.hour_(hour, speed_test_draw)
            U8.min_(minute, speed_test_draw)
            U8.speed_downlink_(speed_test_draw)
            U8.speed_uplink_(speed_test_draw)

            speed_test_image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}-CT.png")

            # U_RTWP
            umts_image_name = random.randint(1, 20)
            image = Image.open(f"images/rtwp/U/RTWP ({umts_image_name}).png")
            draw = ImageDraw.Draw(image)

            UR.enb_(enb, draw)

            u_pd_1_bg = Image.open("images/rtwp/u_pd_1_bg.png")
            image.paste(u_pd_1_bg, (134, 58))
            UR.pd_1(cid, i, draw)

            u_pd_2_bg = Image.open("images/rtwp/u_pd_2_bg.png")
            image.paste(u_pd_2_bg, (35, 85))
            UR.pd_2(cid, i, draw)

            UR.time_(hour, minute, draw)

            UR.other_(cid, draw)

            image.save(f"./Output/{cid}.png")

    elif band == "U1":
        for (battery, hour, minute, second, hms, enb, cid, pci_psc, i) in todo_list:

            image = Image.open(f"images/{band}_Images/" + "PSC" + ".png")
            draw = ImageDraw.Draw(image)
            U1.battery_(battery, draw)
            U1.hour_(hour, draw)
            U1.min_(minute, draw)
            U1.cid_(cid, draw)
            U1.psc_(pci_psc, draw)
            U1.rsrp_(draw)
            U1.gps_acc_(draw)
            U1.hight_(draw)
            U1.altitude_(draw)
            U1.ul_(draw)
            U1.dl_(draw)
            U1.serving_(draw)
            U1.longitude_(draw)
            U1.latitude_(draw)
            U1.cellid_(enb, draw)
            U1.ci_(pci_psc, draw)
            U1.serTime_(hms, draw)
            U1.rnc_(draw)
            U1.level_(draw)

            image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}.png")

            speed_test_image = Image.open(
                f"images/{band}_Images/" + str(random.randint(1, 10)) + ".png")
            speed_test_draw = ImageDraw.Draw(speed_test_image)
            U1.battery_(battery, speed_test_draw)
            U1.hour_(hour, speed_test_draw)
            U1.min_(minute, speed_test_draw)
            U1.speed_downlink_(speed_test_draw)
            U1.speed_uplink_(speed_test_draw)

            speed_test_image.save(
                f"./Output/S{str(int(i)+1)}-{band}-{hour}-{minute}-{second}-CT.png")

            # U_RTWP
            umts_image_name = random.randint(1, 20)
            image = Image.open(f"images/rtwp/U/RTWP ({umts_image_name}).png")
            draw = ImageDraw.Draw(image)

            UR.enb_(enb, draw)

            u_pd_1_bg = Image.open("images/rtwp/u_pd_1_bg.png")
            image.paste(u_pd_1_bg, (134, 58))
            UR.pd_1(cid, i, draw)

            u_pd_2_bg = Image.open("images/rtwp/u_pd_2_bg.png")
            image.paste(u_pd_2_bg, (35, 85))
            UR.pd_2(cid, i, draw)

            UR.time_(hour, minute, draw)

            UR.other_(cid, draw)

            image.save(f"./Output/{cid}.png")

    elif band == "N1":
        for (hour, minute, second, hm, pci, i) in todo_list:
            latitude = "22.3184" + str(random.randint(10, 99))
            longitude = "114.1695" + str(random.randint(10, 99))

            # N1 pci
            pci_img = Image.open(f"images/nr/n1pci.jpg")
            pci_draw = ImageDraw.Draw(pci_img)
            nrtopbar = Image.open("images/nr/nrtopbar.png")
            pci_img.paste(nrtopbar, (0, 0))

            N1.time_(hm, pci_draw)
            N1.n1pci_(pci, latitude, longitude, pci_draw)
            pci_img.save(
                f"./Output/S{str(int(i)+1)}-{band}-NRPCI-{hour}-{minute}-{second}.jpg")

            # N1 lte pci
            lte_img = Image.open(f"images/nr/n1lte.jpg")
            lte_draw = ImageDraw.Draw(lte_img)
            lte_img.paste(nrtopbar, (0, 0))

            N1.time_(hm, lte_draw)
            lte_900 = "L8"
            lte_1800 = "L3"
            if (lte_900 and lte_1800) in band_list:
                N1.n1ltepci_(pci, latitude, longitude, lte_draw)
            else:
                N1.n1ltepci_900_(pci, latitude, longitude, lte_draw)

            lte_img.save(
                f"./Output/S{str(int(i)+1)}-{band}-NRLTEPCI-{hour}-{minute}-{second}.jpg")

            # N1 speedtest
            rand_img = random.randint(1, 14)
            speed_img = Image.open(f"images/nr/calltest/nr ({rand_img}).jpg")
            speed_draw = ImageDraw.Draw(speed_img)
            speed_img.paste(nrtopbar, (0, 0))

            N1.time_(hm, speed_draw)
            N1.n1speed_(speed_draw)
            speed_img.save(
                f"./Output/S{str(int(i)+1)}-{band}-SPEED-{hour}-{minute}-{second}.jpg")

    if input(f"S{site_number}，仲有其他Band要做？(y/n)\n：").strip().upper() != 'Y':
        break

# Alarm
image = Image.open("images/alarm/default.png")
draw = ImageDraw.Draw(image)

a = "U1"
b = "U8"
c = "L1"
d = "L3"
e = "L8"
f = "L40"
g = "N1"
h = "N78"

guln_list = []
if a or b in band_list:
    guln_list.append("U")
if c or d or e or f in band_list:
    guln_list.append("L")
if g or h in band_list:
    guln_list.append("N")

guln = ""
for i in guln_list:
    guln = guln + i

A.enb_(enb, draw)
A.guln_(guln, draw)
A.tas_(hour, minute, second, default_date, draw)
image.save("Output/Alarm.png")
