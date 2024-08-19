#!/bin/bash
#在指定目标范围ip的主机间建立信任关系

# 判断公钥是否已存在，不存在就生成
echo "开始运行>>>"
if [ ! -f ~/.ssh/id_rsa ] ; then
    echo "生成公钥>>>"
    ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
else
    echo "公钥已存在，继续运行"
fi

cat ~/.ssh/id_rsa.pub >>~/.ssh/authorized_keys
pw="abc@1234"

# 目标主机 IP 范围
network="192.168.32"
start_ip=22
end_ip=23

# 用expect模拟输入，使用ssh-copy-id命令将公钥复制到各目标主机
for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    echo "正在和目标主机${target_ip}建立信任关系>>>"
    sleep 2
    my_command="ssh-copy-id -i /root/.ssh/id_rsa.pub root@${target_ip}"
    expect -c "
        spawn ${my_command};
        set timeout 60
        expect {
                 \"password:\"             {send \"${pw}\r\";  exp_continue}
                 \"connecting (yes/no)?\"  {send \"yes\r\";    exp_continue}
               }
        "
    echo "目标主机${target_ip}间的信任关系已建立>>>"
done
