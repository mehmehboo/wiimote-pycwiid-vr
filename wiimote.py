import cwiid
from time import sleep
from subprocess import call
from math import *

def connectRemotes(amount):##untested
    remotes = []
    for j in range(amount):
        DRIVE_A="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0102"
        DRIVE_B="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0103"
        COAST_A="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=01020000"
        COAST_B="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=01030000"
        BREAK_A="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0002"
        BREAK_B="gatttool -b 00:07:80:7F:28:E1 -i hci0 --char-write --handle=0x0025 --value=0003"

        print('Press 1+2 on your Wiimote now...')
        wm = None
        i=1
        while not wm:
            try:
                wm=cwiid.Wiimote()
            except RuntimeError:
                if(i>5):
                    print("cannot create connection")
                    quit()
                print("Error opening wiimote connection")
                print("attempt " + str(i))
                i += 1

        wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_MOTIONPLUS | cwiid.RPT_IR

        wm.led=15
        wm.rumble=True
        sleep(0.5)
        wm.rumble=False
        wm.led=0
        sleep(1.5)
        remotes.append(wm)


