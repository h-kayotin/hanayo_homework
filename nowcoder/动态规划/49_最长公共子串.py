"""
49_最长公共子串 - 

Author: kayotin
Date 2024/4/14
"""


def max_sub_string(str_a: str, str_b: str):
    """动态规划"""
    # 此处默认长度a < b
    n, m = len(str_a), len(str_b)
    max_l = 0
    max_loc = [0, 0]
    dp = [[0]*(m+1) for _ in range(n+1)]

    # dp[i][j]表示字符a中以i结尾的字符与b中j结尾的字符是否能组成子串
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 字符相同才能组成子串，子串长度+1
            if str_a[i-1] == str_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                # 如果长度比之前长，更新索引
                if dp[i][j] > max_l:
                    max_l = dp[i][j]
                    max_loc = [i, j]
            # 字符不相同就需要从0 开始了
            else:
                dp[i][j] = 0
    return str_a[max_loc[0] - max_l:max_loc[0]]


s_a = str(input())
s_b = str(input())
if len(s_a) > len(s_b):
    s_a, s_b = s_b, s_a

print(max_sub_string(s_a, s_b))
