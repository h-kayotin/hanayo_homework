
# 查看硬盘使用情况
df -h

# 查看当前目录，最大的文件夹
du -h --max-depth=1

# 查看所有文件夹大小
du -sh *

# docker中的日志文件清理，/var/lib/docker/containers/b0c9ed5
cat /dev/null > b0c9ed511b7042d75bb9b1aa4bf95f41419f4a202d23dc57482d63a4e58b29b7-json.log