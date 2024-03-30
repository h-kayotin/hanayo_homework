"""
24_密码截取 -

Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，
但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

本质是寻找，最长的对称子串

Author: kayotin
Date 2024/3/30
"""


def find_substr(s: str):
    """暴力解法"""
    n = len(s)
    if n == 1:
        return 1

    # 倒序遍历，先找出最长子串
    for i in range(n, 1, -1):
        sub_strs = []
        for left in range(n):
            sub_str = s[left: left+i]
            if len(sub_str) == i:
                sub_strs.append(sub_str)

        # 判断当前子串中，是否有对称的
        for s_str in sub_strs:
            left, right = 0, len(s_str) - 1
            not_ok = False
            while left < right:
                if s_str[left] != s_str[right]:
                    not_ok = True
                    break
                left += 1
                right -= 1
            if not not_ok:
                return len(s_str)


def find_longest_substring(s: str):
    """找对称,充分利用对称的性质进行剪枝"""
    n = len(s)
    res_list = []
    for i in range(n-1):
        for j in range(1, n):
            # 首先判断是否2个字母相等 再判断 i+1 : j-1 和翻转后是否相等
            if s[i] == s[j] and s[i+1: j] == s[j-1:i:-1]:
                res_list.append(len(s[i:j+1]))
    return max(res_list)


if __name__ == '__main__':
    my_str = "ccABACC"
    print(my_str[3:0:-1])
