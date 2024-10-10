#!/bin/bash
#修改配置文件，添加被监控主机

# 目标主机 IP 范围
network="192.168.32"
start_ip=22
end_ip=24


for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    echo "正在写入$target_ip的配置"
    cat >> /opt/prometheus-2.54.1/prometheus.yml << EOF
  - job_name: '$target_ip'      # 给被监控主机取个名字，我这里直接填的IP
    static_configs:
    - targets: ['$target_ip:9100']      # 被监控主机的IP和端口
EOF

done

# 重启服务
systemctl stop prometheus.service
systemctl start prometheus.service
systemctl status prometheus.service

