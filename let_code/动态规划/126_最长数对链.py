"""
126_最长数对链 - 
给你一个由 n 个数对组成的数对数组 pairs ，其中 pairs[i] = [lefti, righti] 且 lefti < righti 。

现在，我们定义一种 跟随 关系，当且仅当 b < c 时，数对 p2 = [c, d] 才可以跟在 p1 = [a, b] 后面。我们用这种形式来构造 数对链 。

找出并返回能够形成的 最长数对链的长度 。

你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
Author: hanayo
Date： 2024/7/12
"""
from typing import List


def find_longest_chain(self, pairs: List[List[int]]) -> int:
    n = len(pairs)
    dp = [1] * n
    pairs.sort(key=lambda x: x[0])
    for i in range(n):
        for j in range(i):
            if pairs[i][0] > pairs[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


find_longest_chain(1, [[3, 4], [2, 3],[1, 2]])
