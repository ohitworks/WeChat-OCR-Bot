FROM ubuntu:focal

# apt
# -- 换源
RUN sed -i 's/archive.ubuntu.com/mirrors.cloud.tencent.com/g' /etc/apt/sources.list && \
    sed -i 's/security.ubuntu.com/mirrors.cloud.tencent.com/g' /etc/apt/sources.list
RUN apt-get update
# -- 安装所需包
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    xfce4 xfce4-goodies
RUN apt-get install -y \
    tightvncserver
RUN apt-get install -y sudo wget && \
    rm -rf /var/lib/apt/lists/*

# 添加用户, 设置为免密码
RUN useradd -ms /bin/bash weixin && echo "weixin ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/weixin && chmod 0440 /etc/sudoers.d/weixin

# 上传初始化 vncserver 的脚本
ADD scripts/setup_vnc.sh /home/weixin/setup_vnc.sh
ADD config/vnc_password.txt /home/weixin/vnc_password.txt
RUN chmod +x /home/weixin/setup_vnc.sh

# 上传微信安装脚本
ADD scripts/install_weichat.sh /home/weixin/install_weichat.sh
RUN chmod +x /home/weixin/install_weichat.sh

# 上传启动脚本
ADD scripts/setup.sh /home/weixin/setup.sh
RUN chmod +x /home/weixin/setup.sh

# 登录用户
USER weixin
WORKDIR /home/weixin

# 安装 和 初始化
# -- 初始化 venc
RUN ~/setup_vnc.sh
# -- 安装微信
RUN ~/install_weichat.sh

# 等测试完再改成运行启动脚本
CMD ["/bin/bash"]