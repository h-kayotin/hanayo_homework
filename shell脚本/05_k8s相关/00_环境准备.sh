#!/bin/bash
# 安装k8s前的环境准备
# 1 关闭防火墙和SElinux
# 2 设置时间同步和信任关系
# 3 关闭swap分区
# 4 修改内核配置

# 配置host
cat >> /etc/hosts << EOF
192.168.32.31 node31
192.168.32.32 node32
192.168.32.33 node33
EOF

# 建立信任关系 略
# 配置时间同步 略

# 关闭SELinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

# 停止并禁用防火墙
systemctl stop firewalld
systemctl disable firewalld

# 检查当前swap分区设置
sudo swapon --show

# 关闭所有swap分区
sudo swapoff -a

# 备份fstab文件
sudo cp /etc/fstab /etc/fstab.bak

# 注释掉fstab文件中的swap分区
sudo sed -i '/swap/s/^/#/' /etc/fstab

# 加载模块，修改内核参数网络配置
modprobe br_netfilter
echo "modprobe br_netfilter" >> /etc/profile
tee /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
# 加载配置
sysctl -p /etc/sysctl.d/k8s.conf

