import os
from cv2 import cv2
import random
import numpy as np
from PIL import Image
import logging
from pytesseract import image_to_string
import subprocess
import os

# ADB related #note 先開啟adb以免載import時imco
os.system('adb kill-server')
os.system('adb start-server')


def tap(crd: (int, int)):
    cmdTap = 'adb shell input tap {x} {y}'.format(
        x=crd[0],
        y=crd[1]
    )
    logging.info(cmdTap)
    os.system(cmdTap)


def swipe(org: (int, int), tar: (int, int), delay):
    cmdSwipe = 'adb shell input swipe {x1} {y1} {x2} {y2} {delay1}'.format(
        x1=org[0],
        y1=org[1],
        x2=tar[0],
        y2=tar[1],
        delay1=int(delay*1000)
    )
    logging.info(cmdSwipe)
    os.system(cmdSwipe)


# nouse 舊版截圖
"""def screenshot() -> str:
    os.system('adb shell screencap -p /sdcard/sh.png')
    os.system('adb pull /sdcard/sh.png .')
    return "sh.png""""


# helper function
def shifter(ord: (int, int), i: int = 10, j: int = 10) -> (int, int):
    return (ord[0] + random.randint(-i, i), ord[1] + random.randint(-j, j))


def split(path: str, edge: (int, int)):
    img = Image.open(path)
    out = img.crop((edge[0], edge[1], edge[0]+1920, edge[1]+1080))
    out.save("tmp.png")


def get_sh(edge: (int, int)) -> str:
    # screenshot()
    #split(img, edge)
    img = screencap()
    PIL_img = Image.fromarray(img)
    out = PIL_img.crop((edge[0], edge[1], edge[0]+1920, edge[1]+1080))
    out_array = np.array(out)
    return out_array


def screencap():
    pipe = subprocess.Popen("adb shell screencap -p",
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    # 基於bluestacks android7,如果用的是android5版的bluestacks的話要改成image_bytes = pipe.stdout.read().replace(b'\r\r\n', b'\n')
    image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
    image = cv2.imdecode(np.frombuffer(
        image_bytes, dtype='uint8'), cv2.IMREAD_COLOR)
    return image

# OpenCV related


# note 輸入分別為(從get_sh中處理完的圖片陣列,模板圖片名稱,準確度)
def standby(images=get_sh((0, 0)), tmp: str = None, threshold: float = 0.85) -> bool:
    img = images
    template = cv2.imread(tmp)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(res)  # note改取得最相似之座標 res[0]為最小相似度的座標,res[1]為最大相似度的座標
    if (res[1] >= threshold):
        return True
    return False


def check_color(sh: str, tmp: str, threshold: float = 0.8) -> bool:
    img = cv2.imread(sh, cv2.IMREAD_COLOR)
    template = cv2.imread(tmp, cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    if (res >= threshold).any():
        return True
    return False


def get_crd(imges, tmp: str, threshold: float = 0.85) -> [(int, int)]:
    img = imges
    template = cv2.imread(tmp)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    pos = []
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        pos.append(pt)
    return pos


def get_battle_id(img_path: str):
    img = Image.open(img_path)
    region = img.crop((1286, 15, 1378, 62))
    THRESHOLD = 200
    BINARY_TABLE = [0 if i < THRESHOLD else 1 for i in range(256)]
    text = image_to_string(
        region.convert('L').point(BINARY_TABLE, '1'), config='--psm 7 --oem 3 -c tessedit_char_whitelist=/1234')
    print(text)
    try:
        x = int(text[0])
    except IndexError:
        print("Failed to recognize battle id.")
        return 0
    except ValueError:
        print("Failed to recognize battle id.")
        return 0
    else:
        return x


def split_cards(img):
    im = Image.open(img)
    img_size = im.size
    x = img_size[0] // 5
    y = img_size[1] // 2 - 50
    for i in range(5):
        left = i*x
        up = y
        right = left + x
        low = up + y
        region = im.crop((left, up, right, low))
        region.save(f"./temp/{i}.png")


# prepare for servant reo
# currently not used
def split_servant(img: str, i: int):
    im = Image.open(img)
    size = (138, 144, 238, 226)
    region = im.crop(size)
    region.save(f"./temp/_s{i}.png")
