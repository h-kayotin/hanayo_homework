#!/bin/sh
# 安装OpenJDK的脚本
# wget -P /opt/ https://download.java.net/java/GA/jdk22.0.2/c9ecb94cd31b495da20a27d4581645e8/9/GPL/openjdk-22.0.2_linux-x64_bin.tar.gz
live=1
#判断自带JDK
rpm -qa|grep java


#创建jdk安装路径
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo "创建jdk安装路径/opt/jdk"
mkdir -p /opt/jdk
tar -zxf /opt/openjdk-22.0.2_linux-x64_bin.tar.gz -C /opt/jdk/
if [ $? == 0 ]
	then
	 echo '解压成功'
	else
	 echo '解压失败'
	 live=0
	 exit 0
fi

#配置环境变量
# shellcheck disable=SC2112
function setJdk(){
  if [ live == 0 ];then
	  exit 0
	else
    echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    echo "配置环境变量"
    echo "#设置环境变量" >> /etc/profile
    echo "export JAVA_HOME=/opt/jdk/jdk-22.0.2" >> /etc/profile
    echo "export CLASSPATH=\$CLASSPATH:\$JAVA_HOME/lib/:\$JAVA_HOME/jre/lib" >> /etc/profile
    echo "export PATH=\$JAVA_HOME/bin:\$JAVA_HOME/jre/bin:\$PATH:\$HOMR" >> /etc/profile
  fi
}
setJdk

#重新加载配置文件
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo "重新加载配置文件"
source /etc/profile
echo JAVA_HOME=$JAVA_HOME
echo CLASSPATH=$CLASSPATH

#查询java安装信息
echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
echo 查询java安装信息
java --version