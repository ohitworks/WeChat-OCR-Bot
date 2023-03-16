# WeChat-OCR-Bot

基于 Python 语言, 使用模拟鼠标键盘控制, 在 docker 上使用 Ubuntu 运行 Kylin 版微信机器人。

## How to use

下载项目: `git clone https://github.com/ohitworks/WeChat-OCR-Bot.git`

切换到项目目录并构建镜像: `cd WeChat-OCR-Bot && docker build -t ohitworks/WeChat-OCR-Bot .`

启动: `docker run  -itd --name wechat -p 5901:5901 ohitworks/WeChat-OCR-Bot`

接下来需要手动启动 `VNC`: 
- 首先进入命令行: `docker exec -it wechat bash`
- 在容器内部启动 vnc 服务器: `vncserver`

退出容器, 打开 `VNC Viewer`, 连接 `localhost:1`, 输入密码(默认密码是 `password`)

[配置 VNC 界面的终端](https://blog.csdn.net/weixin_42912498/article/details/107162983)后,
在Xfce终端运行 `weixin --no-sandbox` 即可启动微信

**目前项目就写了这些**

## Configs

VNC 登录密码存储在文件 `config/vnc_password.txt`, 默认为 `password`. 
修改此文件并执行 docker build 可以更改 VNC 密码配置

## Doing

- [x] 技术验证: 成功在 Win10 环境下使用 Docker + Xfce + Vnc 运行并登录了 Kylin 微信
- [x] 编写 dockerfile
- [x] 定位微信窗口位置
- [ ] 找出用户名截图

## Bugs

- [ ] dockerfile 构建后仍需手动配置, 待完成自启动脚本
