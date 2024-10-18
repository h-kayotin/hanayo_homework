#!/bin/bash
# 设置ntp服务

# 检查是否安装了ntp
if ! command -v ntpd &> /dev/null; then
    # 如果未安装ntp，则进行yum安装
    sudo yum install -y ntp
fi

# 设置服务器为ntp.aliyun.com
sudo sed -i 's/^server 0.centos.pool.ntp.org iburst/server ntp.aliyun.com/g' /etc/ntp.conf
sudo sed -i 's/^server 1.centos.pool.ntp.org iburst/server ntp1.aliyun.com/g' /etc/ntp.conf
sudo sed -i 's/^server 2.centos.pool.ntp.org iburst/server ntp1.aliyun.com/g' /etc/ntp.conf
sudo sed -i 's/^server 3.centos.pool.ntp.org iburst/server ntp1.aliyun.com/g' /etc/ntp.conf

# 启动ntp服务
sudo systemctl start ntpd
# 设置ntp服务开机启动
sudo systemctl enable ntpd

# 硬件时钟设置为UTC
timedatectl set-local-rtc 0
# 设置本地时区，显示本地时间
timedatectl set-timezone Asia/Shanghai
# 设置硬件时钟
hwclock --systohc
# 查看时钟配置
timedatectl

# 进行一次时间同步
ntpdate -u ntp.aliyun.com
