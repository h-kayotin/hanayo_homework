
# 下载配置
curl https://docs.projectcalico.org/v3.20/manifests/calico.yaml -O

# 修改ip，如果需要
#             - name: CALICO_IPV4POOL_CIDR
#              value: "172.20.0.0/16"


# 下载镜像
docker pull docker.m.daocloud.io/calico/cni:v3.20.6
docker pull docker.m.daocloud.io/calico/pod2daemon-flexvol:v3.20.6
docker pull docker.m.daocloud.io/calico/node:v3.20.6
docker pull docker.m.daocloud.io/calico/kube-controllers:v3.20.6

# 修改tag
docker tag docker.m.daocloud.io/calico/cni:v3.20.6 docker.io/calico/cni:v3.20.6
docker tag docker.m.daocloud.io/calico/pod2daemon-flexvol:v3.20.6 docker.io/calico/pod2daemon-flexvol:v3.20.6
docker tag docker.m.daocloud.io/calico/node:v3.20.6 docker.io/calico/node:v3.20.6
docker tag docker.m.daocloud.io/calico/kube-controllers:v3.20.6 docker.io/calico/kube-controllers:v3.20.6


# 应用配置
kubectl apply -f calico.yaml


# 移除
kubectl delete -f calico.yaml
# 重新部署
kubectl apply -f calico.yaml

# 问题排除过程
# 1.查看有问题的pod的具体信息，在event里可以看到
kubectl describe pod calico-node-99pf4 -n kube-system
# 2.查看是哪个node上缺少对应镜像
kubectl get pods -n kube-system -o wide
# 3.手动执行pull命令
docker pull docker.m.daocloud.io/calico/cni:v3.20.6
docker pull docker.m.daocloud.io/calico/pod2daemon-flexvol:v3.20.6
docker pull docker.m.daocloud.io/calico/node:v3.20.6
docker pull docker.m.daocloud.io/calico/kube-controllers:v3.20.6
# 4.修改tag
docker tag docker.m.daocloud.io/calico/cni:v3.20.6 docker.io/calico/cni:v3.20.6
docker tag docker.m.daocloud.io/calico/pod2daemon-flexvol:v3.20.6 docker.io/calico/pod2daemon-flexvol:v3.20.6
docker tag docker.m.daocloud.io/calico/node:v3.20.6 docker.io/calico/node:v3.20.6
docker tag docker.m.daocloud.io/calico/kube-controllers:v3.20.6 docker.io/calico/kube-controllers:v3.20.6