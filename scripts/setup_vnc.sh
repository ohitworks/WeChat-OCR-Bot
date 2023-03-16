#!/usr/bin/env bash

mkdir ~/.vnc
# Set password for VNC access
vncpasswd -f < ~/vnc_password.txt > ~/.vnc/passwd
chown -R weixin:weixin ~/.vnc
chmod 0600 ~/.vnc/passwd

echo -e '#!/bin/sh \nunset SESSION_MANAGER \nunset DBUS_SESSION_BUS_ADDRESS \nexec startxfce4' > ~/.vnc/xstartup

chmod u+x ~/.vnc/xstartup

# Start vncserver
#vncserver :1 -geometry 1280x800 -depth 24
