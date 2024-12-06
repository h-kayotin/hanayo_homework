#!/bin/bash
# 安装tomcat

echo "下载tomcat9"
wget -P /opt/ https://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.97/bin/apache-tomcat-9.0.97.tar.gz
mkdir /opt/tomcat9
if [ -f /opt/apache-tomcat-9.0.97.tar.gz ];then
        tar -xzf /opt/apache-tomcat-9.0.97.tar.gz -C /opt/tomcat9 --strip-components 1
        echo "解压成功"
else
        echo "解压出错"
        exit;
fi
echo "安装路径：/opt/tomcat9"

# 防火墙开启8080端口
firewall-cmd --zone=public --add-port=8080/tcp --permanent
# reload防火墙
firewall-cmd --reload


#