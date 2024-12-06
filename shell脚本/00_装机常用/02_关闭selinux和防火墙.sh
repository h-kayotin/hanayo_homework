#!/bin/bash

# 关闭SELinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

# 停止并禁用防火墙
systemctl stop firewalld
systemctl disable firewalld

echo "SELinux和防火墙已成功关闭！"

# 动静分离
yum install libevent -y
yum install memcached  -y
# 当前nginx服务器ip
memcached -d -m 128m -p 11211 -l 192.168.32.17 -u root -P /opt/mempid
pgrep memcached
