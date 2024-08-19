#!/bin/bash
#在指定目标范围ip的主机间复制文件

# 目标主机 IP 范围
network="192.168.32"
start_ip=22
end_ip=23

# 获取当前日期和时间
current_date=$(date +%Y%m%d)
current_time=$(date +%H%M%S)

# 日志文件名
log_file="${current_date}_${current_time}.log"

# 发送文件并记录结果到日志文件
function send_file() {
    local target_ip=$1
    local file_path=$2

    scp "$file_path" root@"$target_ip":/opt/ &>> "$log_file"
    # 检查发送结果并记录到日志文件
    if [ $? -eq 0 ]; then
        echo "${file_path}文件发送成功到${target_ip}"
        echo "${file_path}文件发送成功到${target_ip}" >> "$log_file"
    else
        echo "${file_path}文件发送失败到${target_ip}"
        echo "${file_path}文件发送失败到${target_ip}" >> "$log_file"
    fi
}



for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    echo "正在复制文件到 ${target_ip}..."
    send_file "$target_ip" "/opt/install_jdk.sh"
    send_file "$target_ip" "/opt/openjdk-22.0.2_linux-x64_bin.tar.gz"
done
echo "文件复制完成。请查看日志文件 ${log_file} 获取详细结果。"