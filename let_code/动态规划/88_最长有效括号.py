"""
88_最长有效括号 - 

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

Author: hanayo
Date： 2024/6/18
"""


def longest_valid_parentheses(self, s: str) -> int:
    stack = []
    max_l = 0
    n = len(s)
    tmp = [0] * n
    cur = 0

    # 匹配2个括号的过程
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                j = stack.pop()
                if s[j] == '(':
                    tmp[i], tmp[j] = 1, 1

    # 统计最长序列，就是连续出现1的最大次数
    for num in tmp:
        if num:
            cur += num
        else:
            max_l = max(cur, max_l)
            cur = 0

    max_l = max(cur, max_l)
    return max_l
