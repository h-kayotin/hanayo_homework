#!/bin/bash
# 安装nginx

yum install yum-utils -y
rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

# 查看所有可安装nginx版本
yum --showduplicates list available nginx
yum install nginx-1.24.0 -y
systemctl enable nginx

# 防火墙开启80端口
firewall-cmd --zone=public --add-port=80/tcp --permanent
# reload防火墙
firewall-cmd --reload
# 查看当前开了哪些端口
firewall-cmd --list-all
# 启动nginx
systemctl start nginx
# 查看是否开机启动
systemctl is-enabled nginx

# nginx的reload命令
nginx -s reload