#!/usr/bin/env bash
# Set password for VNC access
echo "password123" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

echo -e "#\!/bin/sh \nunset SESSION_MANAGER \nunset DBUS_SESSION_BUS_ADDRESS \nexec startxfce4" > ~/.vnc/xstartup
chmod u+x ~/.vnc/xstartup

# Start vncserver
#vncserver :1 -geometry 1280x800 -depth 24
