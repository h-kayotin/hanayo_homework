#!/bin/bash
#redis哨兵配置

master_ip="192.168.32.21"
sentinel_ip="192.168.32.22"
redis_port=6379
sentinel_port=26379
redis_password="Abc@1234"

# 在哨兵节点上配置sentinel
ssh root@$sentinel_ip << EOF
    # 安装redis时默认设置了开机启动，所以先关闭服务
    chkconfig redis off
    redis-cli shutdown

    # 将哨兵的配置文件复制一份在/etc下面
    grep -E -v "^$|^#" /opt/redis-7.0.0/sentinel.conf > /etc/sentinel.conf
    # 修改配置文件
    # 后台启动服务
    sed -i "s/daemonize no/daemonize yes/g" /etc/sentinel.conf
    # 设置log
    sed -i "s/logfile \"\"/logfile \/var\/log\/sentinel.log/g" /etc/sentinel.conf
    # 指定监控的mater 的ip，默认2是指有2台哨兵认为master死了就切换
    sed -i "s/monitor mymaster 127.0.0.1 6379 2/monitor mymaster $master_ip $redis_port 2/g" /etc/sentinel.conf
    # 默认是30000ms无响应，就认为挂了，我们设置为10s，方便测试
    sed -i "s/down-after-milliseconds mymaster 30000/down-after-milliseconds mymaster 10000/g" /etc/sentinel.conf

    # 设置密码
    echo "sentinel auth-pass mymaster $redis_password" >> /etc/sentinel.conf
    #
    echo "bind 0.0.0.0" >> /etc/sentinel.conf

    # 防火墙开放端口
    firewall-cmd --zone=public --add-port=$sentinel_port/tcp --permanent
    firewall-cmd --reload

    # 启动哨兵
    redis-sentinel /etc/sentinel.conf

EOF

echo "Redis哨兵配置完成"