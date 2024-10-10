#!/bin/bash
# mysql监控组件node_exporter和mysqld_exporter

# 下载，没找到国内下载源，下载速度很慢。建议用scp发送到其他机器。
wget -P "/opt" https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz
#scp "/opt/node_exporter-1.8.2.linux-amd64.tar.gz" root@"$target_ip":/opt/
# 解压
tar -zxvf /opt/node_exporter-1.8.2.linux-amd64.tar.gz -C /opt/
# 改名
mv /opt/node_exporter-1.8.2.linux-amd64 /opt/node_exporter
# 设置开机启动
cat > /etc/systemd/system/node_exporter.service << EOF
[Unit]
Description=node_exporter
After=network.target
[Service]
Type=simple
ExecStart=/opt/node_exporter/node_exporter
Restart=on-failure
[Install]
WantedBy=multi-user.target
EOF
# 启动
systemctl daemon-reload
systemctl start node_exporter
systemctl enable node_exporter

# 开放端口
firewall-cmd --permanent --add-port=9100/tcp
firewall-cmd --reload