#!/bin/bash
# 安装指定版本docker

# 安装依赖
yum install -y yum-utils device-mapper-persistent-data lvm2
# 指定阿里云的repo，国外的镜像很慢
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# 查看可用的版本
yum list docker-ce --showduplicates | sort -r
# 安装指定版本docker
sudo yum install -y docker-ce-24.0.6-1.el7 docker-ce-cli-24.0.6-1.el7 containerd.io docker-buildx-plugin docker-compose-plugin


# docker的systemd配置，代理配置
cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": [
    "https://docker.m.daocloud.io",
    "https://registry.aliyuncs.com",
    "https://registry.docker-cn.com",
    "https://docker.mirrors.ustc.edu.cn"
    ],
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
EOF

# 查看版本
docker --version
# 启动docker
systemctl start docker
# 设置开机启动
systemctl enable docker
systemctl status docker

# 如需重启刷新配置，使用如下命令
sudo systemctl daemon-reload