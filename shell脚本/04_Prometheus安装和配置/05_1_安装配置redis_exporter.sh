#!/bin/bash
#redis_exporter的安装配置

wget -P "/opt" https://github.com/oliver006/redis_exporter/releases/download/v1.63.0/redis_exporter-v1.63.0.linux-amd64.tar.gz

redis_pwd=Abc@1234

# 解压和安装
tar -zxf /opt/redis_exporter-v1.63.0.linux-amd64.tar.gz -C /opt/
mv /opt/redis_exporter-v1.63.0.linux-amd64 /opt/redis_exporter

# 开放端口，redis_exporter默认使用9121端口
firewall-cmd --permanent --add-port=9121/tcp
firewall-cmd --reload

# 准备配置文件
cat > /etc/systemd/system/redis_exporter.service << EOF
[Unit]
Description=redis_exporter
After=network.target
[Service]
Type=simple
ExecStart=/opt/redis_exporter/redis_exporter -redis.addr 127.0.0.1:6379  -redis.password $redis_pwd
Restart=on-failure
[Install]
WantedBy=multi-user.target
EOF

# 启动
systemctl daemon-reload
systemctl start redis_exporter
systemctl enable redis_exporter

# 写入Prometheus配置
    cat >> /opt/prometheus-2.54.1/prometheus.yml << EOF
  - job_name: 'redis_192.168.32.21'
    static_configs:
    - targets: ['192.168.32.21:9121']
EOF
# 重启Prometheus
systemctl restart prometheus