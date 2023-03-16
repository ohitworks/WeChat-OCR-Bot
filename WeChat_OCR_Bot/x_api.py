#!/usr/bin/env python3
"""Docstring for the x_api.py module.

@author ohitworks
@date   2023-03-16

X 窗口支持

"""
import re
import subprocess
import collections


class WindowInfo:
    """
    窗口信息类, 其实是 WindowInfo.WindowInfo 类 (一个 nametuple 实例) 的构造器.

    为啥不用 dataclasses 呢, 因为我不太会用这个库.
    """
    RE_WINDOW_INFO = re.compile("(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+?) +(.+)")
    WindowInfo = collections.namedtuple(
        "WindowInfo",
        ("window_id", "desktop_number", "x", "y", "width", "height", "client_machine_name", "title"))

    def __new__(cls, string):
        text_value = cls.RE_WINDOW_INFO.match(string).groups()
        args = list(text_value)

        for i in range(2, 6):
            args[i] = int(args[i])

        return cls.WindowInfo(*args)


def get_all_window_info() -> list[WindowInfo.WindowInfo]:
    """
    返回窗口信息
    :return:
    """
    # https://manpages.ubuntu.com/manpages/focal/en/man1/wmctrl.1.html
    out = subprocess.check_output(['wmctrl', '-lG']).decode()
    lines = out.splitlines()

    return [WindowInfo(line) for line in lines]
