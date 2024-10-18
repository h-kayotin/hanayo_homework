#!/bin/bash

# 关闭SELinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

# 停止并禁用防火墙
systemctl stop firewalld
systemctl disable firewalld

echo "SELinux和防火墙已成功关闭！"