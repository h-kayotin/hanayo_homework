#!/bin/bash
# 修改主机名和IP

# 获取用户输入的IP地址和主机名，-r参数用于禁用反斜杠的转义功能
read -rep "请输入新的IP地址，例如192.168.32.31/24: " ip_address
read -rep "请输入新的主机名: " hostname

# 获取当前网卡信息
interface=$(ip route | awk '/default/ { print $5 }')

# 修改主机名
hostnamectl set-hostname "$hostname"

# 使用nmcli命令修改指定网卡的IP地址
nmcli connection modify "$interface" ipv4.addresses "$ip_address"

echo "主机名和IP地址已成功修改！"

# 查看当前系统版本
cat /etc/centos-release

nmcli connection reload
nmcli connection up "$interface"