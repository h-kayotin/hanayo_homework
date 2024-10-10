#!/bin/bash
#redis主从配置

master_ip="192.168.32.21"
master_pwd="Abc@1234"
start_ip=23
end_ip=24
network="192.168.32"
redis_port=6379
sentinel_port=26379

# 配置主节点
echo "requirepass $master_pwd" >> /etc/redis.conf
echo "masterauth $master_pwd" >> /etc/redis.conf
systemctl restart redis

# 开启6379端口，用于主从间的通信
firewall-cmd --zone=public --add-port=$redis_port/tcp --permanent
# 开放26379，用于哨兵的主从切换
firewall-cmd --zone=public --add-port=$sentinel_port/tcp --permanent
# 重启一下防火墙服务
firewall-cmd --reload

# 配置从节点
for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    echo "正在进行 ${target_ip} 的redis设置..."
    ssh root@"$target_ip" << EOF
        echo "replicaof $master_ip $redis_port" >> /etc/redis.conf
        echo "requirepass $master_pwd" >> /etc/redis.conf
        echo "masterauth $master_pwd" >> /etc/redis.conf
        redis-cli -a Abc@1234 shutdown
        /etc/init.d/redis start
        firewall-cmd --zone=public --add-port=$redis_port/tcp --permanent
        firewall-cmd --zone=public --add-port=$sentinel_port/tcp --permanent
        firewall-cmd --reload
EOF
done

