#!/usr/bin/env bash
# 启动脚本

# 安装和初始化
# -- 初始化 venc
~/setup_vnc.sh
# -- 安装微信
~/install_weichat.sh

# 启动 vnc
vncserver :1 -geometry 1280x800 -depth 24

# 启动微信
weixin --no-sandbox
