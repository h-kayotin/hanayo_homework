

curl https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.3.1/deploy/static/provider/cloud/deploy.yaml -O
sed -i 's/registry\.k8s\.io/k8s.dockerproxy.com/g' deploy.yaml

kubectl describe pod ingress-nginx-admission-create-rgzdw  -n ingress-nginx

kubectl delete pod ingress-nginx-controller-84f8c84b9c-f62k6 -n ingress-nginx
