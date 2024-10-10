#!/bin/bash
#在指定主机范围安装redis_exporter,默认本机上已经有安装文件和service文件


# 指定ip范围
start_ip=23
end_ip=24
network="192.168.32"

# 在指定主机上分别配置
for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    scp "/opt/redis_exporter-v1.63.0.linux-amd64.tar.gz" root@"$target_ip":/opt/
    scp "/etc/systemd/system/redis_exporter.service" root@"$target_ip":/etc/systemd/system/
    echo "正在 ${target_ip} 安装redis_exporter..."
    ssh root@"$target_ip" << EOF
    tar -zxf /opt/redis_exporter-v1.63.0.linux-amd64.tar.gz -C /opt/
    mv /opt/redis_exporter-v1.63.0.linux-amd64 /opt/redis_exporter
    systemctl daemon-reload
    systemctl start redis_exporter
    systemctl enable redis_exporter
    # 开放端口
    firewall-cmd --permanent --add-port=9121/tcp
    firewall-cmd --reload
EOF
    echo "正在写入$target_ip的redis配置"
    cat >> /opt/prometheus-2.54.1/prometheus.yml << EOF
  - job_name: 'redis_$ip'
    static_configs:
    - targets: ['$target_ip:9121']
EOF
done

# 重启服务
systemctl stop prometheus.service
systemctl start prometheus.service
systemctl status prometheus.service