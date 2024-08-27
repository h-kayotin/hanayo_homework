#!/bin/bash

# 目标主机 IP 范围
network="192.168.32"
start_ip=22
end_ip=23


# 运行脚本并记录结果到日志文件
function run_script() {
    local target_ip=$1
    local script_path=$2

    ssh root@"$target_ip" "$script_path" &>> "$log_file"
    # 检查运行结果并记录到日志文件
    if [ $? -eq 0 ]; then
        echo "${script_path}脚本在${target_ip}上成功运行"
        echo "${script_path}脚本在${target_ip}上成功运行" >> "$log_file"
    else
        echo "${script_path}脚本在${target_ip}上运行失败"
        echo "${script_path}脚本在${target_ip}上运行失败" >> "$log_file"
    fi
}

# 获取当前日期和时间
current_date=$(date +%Y%m%d)
current_time=$(date +%H%M%S)

# 日志文件名
log_file="${current_date}_${current_time}.log"

for ip in $(seq ${start_ip} ${end_ip})
do
    target_ip=${network}.${ip}
    echo "正在运行脚本在 ${target_ip}..."
    run_script "$target_ip" "/opt/a.sh"
done
echo "脚本运行完成。请查看日志文件 ${log_file} 获取详细结果。"