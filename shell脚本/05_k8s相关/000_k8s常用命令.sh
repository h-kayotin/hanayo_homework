
# 需要运行以下命令，才能使用kubectl命令
export KUBECONFIG=/etc/kubernetes/admin.conf

# 应用yaml文件，也就是创建pod
kubectl apply -f sample.yaml
# 删除yaml文件，也就会删除所有pod
kubectl delete -f sample.yaml

# 获取制定namespace上的pod，-o参数会显示node和端口等信息
kubectl get pods -n kube-system -o wide
# 查看指定pod的具体信息，主要看event字段中的信息
kubectl describe pod calico-node-99pf4 -n kube-system

# 重启指定name的pod，因为pod总是会自动创建，所以删除就是重启
kubectl delete pod podname -n ingress-nginx


# 通过key value创建configmap
kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2
# 通过yaml文件创建configmap
kubectl create -f cm-appvars.yaml
# 查看configmap
kubectl get configmap
# 查看具体configmap
kubectl describe configmap kube-root-ca.crt
# 通过yaml格式输出configmap文件
kubectl get cm cm1 -o yaml


# 进入容器
kubectl exec -it cm-test-pod3 -- sh
# 退去
exit