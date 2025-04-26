#!/bin/bash
# 备份博客的mysql数据库

pwd="Abc@1234"
# 备份数据库
current_date=$(date +%Y%m%d)
current_time=$(date +%H%M)
backup_name="backup_${current_date}_${current_time}.sql"
mysqldump -uroot -p$pwd --all-databases > "/opt/$backup_name"



# 使用 tar 压缩备份文件
tar -zcvf "wordpress0426.tar.gz" "wordpress"

# 下载备份文件到本地，然后上传到服务器解压
tar -zxvf "ordpress.tar.gz" -C /opt

# 还原mysql数据库
mysql -uroot -pAbc@1234 < /opt/backup_20250426_0959.sql

# 拉镜像
docker pull wordpress

# 启动
docker run -it --name wordpress_new --log-opt max-size=10m --log-opt max-file=3 -p 80:80 -v /opt/wordpress:/var/www/html -d wordpress

# 修改数据库配置，数据库ip 用户和密码等 注意关闭ssl访问
vim /opt/wordpress/wp-config.php

# 修改ip wp_options表中的siteurl和home，改回ip访问
