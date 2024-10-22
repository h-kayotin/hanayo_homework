

# 安装kubectl/kubelet/kubeadm 在master节点上
yum install -y kubelet-1.20.9 kubeadm-1.20.9 kubectl-1.20.9
# 启动kubelet服务
systemctl enable kubelet && systemctl start kubelet

# 安装kubeadm、kubelet 在worker节点上
yum install -y kubelet-1.20.9 kubeadm-1.20.9
systemctl enable kubelet && systemctl start kubelet

# docker的systemd配置，按需
cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": [
    "https://docker.m.daocloud.io",
    "https://registry.aliyuncs.com",
    "https://registry.docker-cn.com",
    "https://docker.mirrors.ustc.edu.cn"
    ],
  "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF

systemctl restart docker
systemctl status docker


# 常用命令

# 初始化
kubeadm init \
--apiserver-advertise-address=192.168.32.31 \
--control-plane-endpoint=cluster-endpoint \
--image-repository  registry.cn-hangzhou.aliyuncs.com/google_containers \
--kubernetes-version v1.20.9 \
--service-cidr=10.96.0.0/12 \
--pod-network-cidr=192.168.0.0/16

# 加入集群
kubeadm join cluster-endpoint --token xxxxxx \
# 查看token
kubeadm token list
# 生产新token
kubeadm token create --print-join-command
# 查看集群状态
kubectl cluster-info
# 运行管理命令前
export KUBECONFIG=/etc/kubernetes/admin.conf
# 查看nodes
kubectl get nodes
# 修改角色
kubectl label node node32 node-role.kubernetes.io/worker=worker

# 查看pod
kubectl get pods -n kube-system
