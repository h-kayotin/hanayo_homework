"""
93_字符串解码 - 
https://leetcode.cn/problems/decode-string/description/?envType=study-plan-v2&envId=top-100-liked
Author: hanayo
Date： 2024/6/21
"""


def decode_string(s: str) -> str:
    stack_s, res, multi = [], '', 0
    for c in s:
        if c == '[':
            stack_s.append([multi, res])
            res, multi = '', 0
        elif c == ']':
            cur_multi, last_res = stack_s.pop()
            res = last_res + cur_multi*res
        elif '0' <= c <= '9':
            multi = multi*10 + int(c)
        else:
            res += c
        print(stack_s)
    return res


def decode_string2(s: str) -> str:
    """递归"""
    def dfs(s, i):
        res, multi = "", 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                multi = multi*10 + int(s[i])
            elif s[i] == '[':
                i, tmp = dfs(s, i+1)
                res += multi*tmp
                multi = 0
            elif s[i] == ']':
                return i, res
            else:
                res += s[i]
            i += 1
        return res
    dfs(s, 0)


decode_string('3[a]2[bc]')