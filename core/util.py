import os

def tap(x0, y0):
    cmdTap = 'adb shell input tap {x1} {y1}'.format(
        x1=x0,
        y1=y0
    )
    print(cmdTap)
    os.system(cmdTap)


def swipe(x0, y0, x1, y1, delay0):
    cmdSwipe = 'adb shell input swipe {x2} {y2} {x3} {y3} {delay1}'.format(
        x2=x0,
        y2=y0,
        x3=x1,
        y3=y1,
        delay1=delay0
    )
    print(cmdSwipe)
    os.system(cmdSwipe)


def screenshot():
    os.system('adb shell screencap -p /sdcard/sh.png')
    os.system('adb pull /sdcard/sh.png .')
    return "sh.png"
