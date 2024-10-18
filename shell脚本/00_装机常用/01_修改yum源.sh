#!/bin/bash
# 修改为阿里云的yum仓库,

# 删除原yum仓库
rm -rf /etc/yum.repos.d/*

# 下载阿里云的repo
# curl命令下载: curl [options] [url]
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

# 清除yum缓存
yum clean all

# 缓存阿里云镜像
yum makecache

# 确认yum源
yum repolist