#!/bin/bash
#在指定范围主机上，批量安装node_exporter。需要准备好配置文件和安装文件
# wget -P "/opt/" https://github.com/prometheus/mysqld_exporter/releases/download/v0.15.1/mysqld_exporter-0.15.1.linux-amd64.tar.gz

# 准备配置文件，用来指定mysql的用户，建议是建一个专门的监控用户
cat > /opt/mysqld_exporter.cnf << EOF
[client]
user=root
password=Abc@1234
# host=127.0.0.1:3306
EOF

# 准备开机启动的配置文件
cat > /opt/mysqld_exporter.service << EOF
[Unit]
Description=mysqld_exporter
After=network.target
[Service]
Type=simple
ExecStart=/opt/mysqld_exporter/mysqld_exporter \
  --config.my-cnf /etc/mysqld_exporter.cnf \
  --collect.slave_status \
  --collect.slave_hosts \
  --log.level=error \
  --collect.info_schema.processlist \
  --collect.info_schema.innodb_metrics \
  --collect.info_schema.innodb_tablespaces \
  --collect.info_schema.innodb_cmp \
  --collect.info_schema.innodb_cmpmem
Restart=on-failure
[Install]
WantedBy=multi-user.target
EOF

# 指定ip范围
start_ip=22
end_ip=23
network="192.168.32"

# 在指定主机上分别配置
for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    scp "/opt/mysqld_exporter-0.15.1.linux-amd64.tar.gz" root@"$target_ip":/opt/
    scp "/opt/mysqld_exporter.cnf" root@"$target_ip":/etc/
    scp "/opt/mysqld_exporter.service" root@"$target_ip":/etc/systemd/system/
    echo "正在 ${target_ip} 安装mysqld_exporter..."
    ssh root@"$target_ip" << EOF
    tar -zxf /opt/mysqld_exporter-0.15.1.linux-amd64.tar.gz -C /opt/
    mv /opt/mysqld_exporter-0.15.1.linux-amd64 /opt/mysqld_exporter
    systemctl daemon-reload
    systemctl start mysqld_exporter
    systemctl enable mysqld_exporter
    # 开放端口
    firewall-cmd --permanent --add-port=9104/tcp
    firewall-cmd --reload
EOF
    echo "正在写入$target_ip的配置"
    cat >> /opt/prometheus-2.54.1/prometheus.yml << EOF
  - job_name: 'mysql$ip'
    static_configs:
    - targets: ['$target_ip:9104']
EOF
done

# 重启服务
systemctl stop prometheus.service
systemctl start prometheus.service
systemctl status prometheus.service