# windows python3
from datetime import datetime as a
import time
import winsound
hour = a.now().time().hour
minute = a.now().time().minute
second = a.now().time().second

timer = int(input("Set Timer for seconds: ?"))
time.sleep(timer)
winsound.PlaySound("SystemExit",winsound.SND_ALIAS)
print("Done")