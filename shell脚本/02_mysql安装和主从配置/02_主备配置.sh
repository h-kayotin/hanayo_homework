#!/bin/bash
# 备份主数据库数据，还原到备份数据库，配置主从

pwd="Abc@1234"
# 备份数据库
current_date=$(date +%Y%m%d)
current_time=$(date +%H%M)
backup_name="backup_${current_date}_${current_time}.sql"
mysqldump -uroot -p$pwd --all-databases > "/opt/$backup_name"

# 目标主机 IP 范围
network="192.168.32"
start_ip=22
end_ip=23

# 还原数据库
for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    echo "正在复制sql文件到 ${target_ip}..."
    scp "/opt/$backup_name" root@"$target_ip":/opt/
    echo "正在还原数据库到 ${target_ip}..."
    ssh root@"$target_ip" "mysql -uroot -p$pwd < /opt/$backup_name"
    # 创建slave用户,授权给从数据库使用
    mysql -uroot -p"$pwd" -e "use mysql;create user 'slave'@'$target_ip' identified by '$pwd';
    grant replication slave on *.* to 'slave'@'$target_ip';flush privileges;"
done

#主库配置
echo "log_bin=mysql-bin" >> /etc/my.cnf
echo "server_id=1" >> /etc/my.cnf
# 重启mysql服务
systemctl restart mysqld

# 查看主库状态
mysql -uroot -p"$pwd" -e 'show master status;'
master_file=$(mysql -uroot -p"$pwd" -e 'show master status;' | awk 'NR==2{print $1}')
master_pos=$(mysql -uroot -p"$pwd" -e 'show master status;' | awk 'NR==2{print $2}')
master_ip="192.168.32.21"


# 从库配置
salve_id=2
for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    echo "正在配置从库 ${target_ip}..."
    ssh root@"$target_ip" "echo 'server_id=$salve_id' >> /etc/my.cnf"
    ssh root@"$target_ip" "echo 'relay-log=mysql-relay-bin' >> /etc/my.cnf;systemctl restart mysqld"
    sql_txt="change master to master_host='$master_ip',master_user='slave',
             master_password='$pwd',master_log_file='$master_file',GET_MASTER_PUBLIC_KEY=1,
             master_log_pos=$master_pos;start slave;"

    ssh root@"$target_ip" "mysql -uroot -p$pwd -e \"$sql_txt\""
    ((salve_id++))
done