"""
16_找出字母异位词 - 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
Author: kayotin
Date 2024/3/30
"""


def find_anagrams(s: str, p: str) -> list[int]:
    """暴力枚举"""
    n = len(s)
    t = len(p)
    if n < t:
        return []
    sub_words = []
    for i in range(n):
        if i + t > n:
            break
        word = s[i:i+t]
        sub_words.append(word)
    res = []
    s_p = sorted(p)
    for idx, word in enumerate(sub_words):
        if sorted(word) == s_p:
            res.append(idx)

    return res


def find_anagrams_2(s: str, p: str) -> list[int]:
    """滑动数组"""
    n, m = len(s), len(p)
    if n < m:
        return []
    res = []
    count_s = [0] * 26
    count_p = [0] * 26

    # 遍历s中到m的字符，同时记录p中每个字母出现次数
    for i in range(m):
        count_s[ord(s[i]) - ord("a")] += 1
        count_p[ord(p[i]) - ord("a")] += 1
    # 如果相同就找到了第一个索引
    if count_s == count_p:
        res.append(0)

    # 继续遍历m到n
    for i in range(m, n):
        # 每次去掉一个旧字母，添加一个新字母
        count_s[ord(s[i-m]) - ord("a")] -= 1
        count_s[ord(s[i]) - ord("a")] += 1
        if count_s == count_p:
            res.append(i-m+1)
    return res


my_c = "bca"
print(sorted(my_c))
print(my_c)