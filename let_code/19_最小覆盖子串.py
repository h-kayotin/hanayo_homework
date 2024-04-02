"""
19_最小覆盖子串 - 
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
Author: kayotin
Date 2024/3/31
"""


def min_window(self, s: str, t: str) -> str:
    def get_id(x: str):
        """将字母转换成数字index"""
        # 大写字母占用26 到 52
        if x.isupper():
            return ord(x) - ord("A") + 26
        # 小写占用0到25
        else:
            return ord(x) - ord("a")

    # tot代表还需要匹配的字符种类
    n, tot = len(s), 0
    times_of_t, times_of_sub = [0]*60, [0]*60

    # 遍历字符串t，将字符频率记录在c1中，将字符种类记录在tot中
    for c in t:
        idx = get_id(c)
        times_of_t[idx] += 1
        if times_of_t[idx] == 1:
            tot += 1

    j = 0
    ans = ""
    # 遍历数组
    for i in range(n):
        sub_idx = get_id(s[i])
        times_of_sub[sub_idx] += 1
        # 对应字母频率相等，说明1种字母已经匹配，tot减去1
        if times_of_sub[sub_idx] == times_of_t[sub_idx]:
            tot -= 1
        while j < i:
            # 遍历区间[j,i]
            idx2 = get_id(s[j])
            # 如果该字母没在t出现过，j向右移动，子串频率中减去这个值
            if times_of_sub[idx2] > times_of_t[idx2]:
                j += 1
                times_of_sub[idx2] -= 1
            # 否则说明[i,j]中还未满足需要的子串，所以跳出并扩大子串范围
            else:
                break
        if tot == 0 and (not ans or len(ans) > i-j + 1):
            ans = s[j: i+1]
    return ans


print(min_window(",", "ADOBECODEBANC", "ABC"))
