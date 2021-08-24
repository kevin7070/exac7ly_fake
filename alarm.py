import datetime
import random

from PIL import Image
from PIL import ImageDraw


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








enb(enb_)
guln(guln_)
tas(time_and_session_)

image.save("Output/Alarm.png")
