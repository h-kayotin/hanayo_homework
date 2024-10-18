#!/bin/bash
# 删除原yum仓库
rm -rf /etc/yum.repos.d/*

# 下载阿里云的repo
# curl命令下载: curl [options] [url]
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

# 清除yum缓存
yum clean all

# 缓存阿里云镜像
yum makecache

touch /etc/yum.repos.d/kubernetes.repo
cat >> /etc/yum.repos.d/kubernetes.repo << EOF
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=0
EOF

# 确认yum源
yum repolist