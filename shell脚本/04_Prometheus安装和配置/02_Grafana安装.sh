#!/bin/bash
# Grafana安装配置

# 下载
wget -P "/opt" https://mirrors.tuna.tsinghua.edu.cn/grafana/yum/rpm/Package/grafana-enterprise-10.1.0-1.x86_64.rpm
yum localinstall /opt/grafana-enterprise-10.1.0-1.x86_64.rpm -y

# 设置开机启动
systemctl enable grafana-server
# 启动
systemctl start grafana-server

# 开放端口
firewall-cmd --permanent --add-port=3000/tcp
firewall-cmd --reload