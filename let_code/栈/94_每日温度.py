"""
94_每日温度 - 
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，
下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
Author: hanayo
Date： 2024/6/21
"""
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """模拟，会超时"""
    res = []
    n = len(temperatures)
    for i in range(n-1):
        nxt = 0
        for j in range(i+1, n):
            nxt += 1
            if temperatures[j] > temperatures[i]:
                res.append(nxt)
                break
            if j == n-1:
                res.append(0)
    res.append(0)
    return res


def daily_temperatures2(temperatures: List[int]) -> List[int]:
    """栈"""
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i in range(n-1, -1, -1):
        t = temperatures[i]
        while stack and t >= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans



print(daily_temperatures([30,40,50,60]))