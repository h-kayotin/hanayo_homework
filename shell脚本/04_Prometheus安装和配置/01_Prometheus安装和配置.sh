#!/bin/bash
#Prometheus安装和配置脚本

#下载
wget -P "/opt" https://mirrors.tuna.tsinghua.edu.cn/github-release/prometheus/prometheus/2.54.1%20_%202024-08-27/prometheus-2.54.1.linux-amd64.tar.gz

# 解压
tar -zxf /opt/prometheus-2.54.1.linux-amd64.tar.gz -C /opt/
mv /opt/prometheus-2.54.1.linux-amd64 /opt/prometheus-2.54.1
# 创建用户和组
# groupadd prometheus
# useradd -g prometheus -s /sbin/nologin prometheus

# 创建目录
mkdir -p /opt/prometheus-2.54.1/data

# 修改权限
# chown -R prometheus:prometheus /opt/prometheus-2.54.1/

# 配置开机启动
cat > /etc/systemd/system/prometheus.service << EOF
[Unit]
Description=Prometheus
Documentation=https://prometheus.io
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=root
Group=root
ExecStart=/opt/prometheus-2.54.1/prometheus \
--config.file=/opt/prometheus-2.54.1/prometheus.yml \
--storage.tsdb.path=/opt/prometheus-2.54.1/data

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl start prometheus
systemctl status prometheus
systemctl enable prometheus