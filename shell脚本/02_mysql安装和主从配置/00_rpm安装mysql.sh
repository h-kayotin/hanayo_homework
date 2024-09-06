#!/bin/bash
# 安装mysql8

# 下载rpm文件
wget https://repo.mysql.com//mysql80-community-release-el7-3.noarch.rpm -P /opt/

# 导入License
rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2023

# 安装mysql
yum -y install /opt/mysql80-community-release-el7-3.noarch.rpm
yum -y install mysql-community-server

# 启动mysql
systemctl start mysqld

init_pw=$(grep 'temporary password' /var/log/mysqld.log | awk '{print $NF}')
new_pw="Abc@1234"

# 设置root密码,会有一个warning，但是修改成功了
mysqladmin -uroot -p"$init_pw" password $new_pw


# 配置允许远程登录
sed -i 's/bind-address/#bind-address/g' /etc/my.cnf

# 更新用户主机
mysql -uroot -p"$new_pw" -e "use mysql;update user set user.Host='%' where user.User='root';flush privileges;"
sleep 2
mysql -uroot -p"$new_pw" -e "ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'Abc@1234';flush privileges;"

# 重启mysql
systemctl restart mysqld

# 开启3306端口
firewall-cmd --zone=public --add-port=3306/tcp --permanent
# 重启一下防火墙服务
firewall-cmd --reload
