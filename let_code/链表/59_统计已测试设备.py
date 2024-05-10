"""
59_统计已测试设备 - 

Author: hanayo
Date： 2024/5/10
"""


def count_test_devices(batteryPercentages: list[int]):
    bat_arr = batteryPercentages
    count = 0
    for i in range(len(bat_arr)):
        if bat_arr[i] > 0:
            count += 1
            for j in range(i, len(bat_arr)):
                bat_arr[j] = max(0, bat_arr[j] - 1)
    return count


def count_test_devices2(batteryPercentages: list[int]):
    bat_arr = batteryPercentages
    count = 0
    for x in bat_arr:
        if x > count:
            count += 1
    return count


print(count_test_devices([0,1,2]))

