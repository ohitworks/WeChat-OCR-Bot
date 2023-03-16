#!/usr/bin/env python3
"""Docstring for the __init__.py module.

@author ohitworks
@date   2023-03-16
基于 Python 语言, 使用模拟鼠标键盘控制, 在 docker 上使用 Ubuntu 运行 Kylin 版微信机器人.
此模块为其 Python 部分, 用于截屏, 数据分析, 模拟鼠标键盘控制 等等.

x_api: X 窗口的 api 支持

"""

from . import x_api
from .x_api import get_all_window_info

__all__ = [x_api]
