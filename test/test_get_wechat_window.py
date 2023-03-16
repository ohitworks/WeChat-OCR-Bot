"""
测试能不能通过 wmctrl 获取正确的窗口位置
"""
import os
from datetime import datetime

from PIL import Image
from WeChat_OCR_Bot.x_api import WindowInfo

FAKE_SCREENSHOT_PATH = r"test/src/garb_1.jpg"
FAKE_WINDOW_INFO_PATH = r"test/src/window_info_1.txt"


def get_window_info_from_file(path):
    with open(path) as fp:
        lines = fp.read().splitlines()
    return [WindowInfo(line) for line in lines]


def test_get_wechat_window():
    img = Image.open(FAKE_SCREENSHOT_PATH)

    all_window_info = get_window_info_from_file(FAKE_WINDOW_INFO_PATH)

    for wechat in all_window_info:
        if "weixin" in wechat.title:
            break
    else:
        raise

    box = (wechat.x, wechat.y, wechat.width, wechat.height)

    img = img.crop(box)
    filename = os.path.basename(__file__)
    img.save(f"test/out/{filename}{datetime.now().date()}.jpg")


if __name__ == "__main__":
    test_get_wechat_window()
