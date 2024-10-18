

# 安装kubectl(仅master节点、kubelet/kubeadm所有节点都需要安装
yum install -y kubelet-1.20.9 kubeadm-1.20.9 kubectl-1.20.9
# 启动kubelet服务
systemctl enable kubelet && systemctl start kubelet


