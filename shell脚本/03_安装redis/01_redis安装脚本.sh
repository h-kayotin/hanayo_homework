#!/bin/bash
# 安装redis，配置设置，该脚本默认安装文件已存在，安装版本是redis-7.0.0，请自行替换对应版本
# wget -P "/opt" https://download.redis.io/releases/redis-7.0.0.tar.gz

# 检查gcc是否已安装
if ! command -v gcc &> /dev/null; then
    echo "gcc未安装，将使用yum安装"

    # 使用yum安装gcc
    sudo yum install -y gcc
else
    echo "gcc已安装"
fi

# 解压Redis安装文件
tar -xzf /opt/redis-7.0.0.tar.gz -C /opt

# 进入Redis目录
# shellcheck disable=SC2164
cd /opt/redis-7.0.0

# 编译并安装Redis
make
sudo make install PREFIX=/usr/local/redis

# 创建配置文件
#Redis基础配置，配置文件保存在 /etc/redis.conf
grep -E -v "^$|^#" /opt/redis-7.0.0/redis.conf > /etc/redis.conf
sed -i "s/bind 127.0.0.1/bind 0.0.0.0/g" /etc/redis.conf
sed -i "s/protected-mode yes/protected-mode no/g" /etc/redis.conf
sed -i "s/daemonize no/daemonize yes/g" /etc/redis.conf
sed -i 's/logfile \"\"/logfile \"\/var\/log\/redis.log\"/g' /etc/redis.conf

#PATH配置
echo "export PATH=\$PATH:/usr/local/redis/bin" >>/etc/profile
source /etc/profile

#启动redis服务,配置开机启动
cp /opt/redis-7.0.0/utils/redis_init_script /etc/init.d/redis
sed -i 's/\/usr\/local\/bin\/redis-server/\/usr\/local\/redis\/bin\/redis-server/g' /etc/init.d/redis
sed -i 's/CLIEXEC=\/usr\/local\/bin\/redis-cli/CLIEXEC=\/usr\/local\/redis\/bin\/redis-cli/g' /etc/init.d/redis
# shellcheck disable=SC2016
sed -i 's/\/etc\/redis\/\${REDISPORT}.conf/\/etc\/redis.conf/g' /etc/init.d/redis
chkconfig redis on
/etc/init.d/redis start

#查看redis监听端口
netstat -anlp|grep redis

# 以下为可选配置
# sed -i "s/pidfile \/var\/run\/redis_6379.pid/pidfile \/usr\/local\/redis\/run\/redis_6379.pid/g
# dir指定数据目录
# sed -i "s/dir \.\//dir \/usr\/local\/redis\/data/g" /opt/redis-7.0.0/conf/redis_6379.conf
# 指定log文件目录
# sed -i "s/logfile \"\"/logfile \"\/opt\/local\/redis\/logs\/redis.log\"/g" /usr/local/redis/redis.conf
# 设置密码
# sed -i "s/^# masterauth.*/masterauth ${passwd}/" /usr/local/redis/redis.conf
