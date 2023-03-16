#!/usr/bin/env bash
# 下载微信  Note: wget 和 curl 下载好像还不一样, 最初用 curl -O 下载后文件不全
wget http://archive.ubuntukylin.com/software/pool/partner/weixin_2.1.1_amd64.deb
# 安装
sudo dpkg -i weixin_2.1.1_amd64.deb

rm weixin_2.1.1_amd64.deb