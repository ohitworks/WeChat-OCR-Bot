#!/usr/bin/env python3
"""Docstring for the setup.py module.

@author ohitworks
@date   2023-03-16

构建 python 包

"""

import setuptools

setuptools.setup(
    name="WeChat_OCR_Bot",
    version="0.1.0",
    author="ohitworks",
    author_email="oooohitworks@outlook.com",
    description="基于 Python 语言, 使用模拟鼠标键盘控制, 在 docker 上使用 Ubuntu 运行 Kylin 版微信机器人. 此模块为其 Python 部分.",
    url="https://github.com/ohitworks/WeChat-OCR-Bot",
    packages=setuptools.find_packages(),

    # 安装过程中，需要安装的静态文件
    data_files=[

    ],
    # 希望被打包的文件
    package_data={

    }
)
