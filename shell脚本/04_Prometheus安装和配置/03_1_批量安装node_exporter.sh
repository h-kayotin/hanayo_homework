#!/bin/bash
#在指定范围主机上，批量安装node_exporter。需要准备好配置文件和安装文件

start_ip=22
end_ip=24
network="192.168.32"

for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    scp "/opt/node_exporter-1.8.2.linux-amd64.tar.gz" root@"$target_ip":/opt/
    scp "/etc/systemd/system/node_exporter.service" root@"$target_ip":/etc/systemd/system/
    echo "正在 ${target_ip} 安装node_exporter..."
    ssh root@"$target_ip" << EOF
        tar -zxf /opt/node_exporter-1.8.2.linux-amd64.tar.gz -C /opt/
        mv /opt/node_exporter-1.8.2.linux-amd64 /opt/node_exporter
        systemctl daemon-reload
        systemctl start node_exporter
        systemctl enable node_exporter
        # 开放端口
        firewall-cmd --permanent --add-port=9100/tcp
        firewall-cmd --reload
EOF
    echo "${target_ip} 上的node_exporter配置完成..."
done