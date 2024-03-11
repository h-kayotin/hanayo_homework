"""
字母异位词分组 - 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

Author: kayotin
Date 2024/3/11
"""

from collections import defaultdict


def group_words(strs: list[str]) -> list[list[str]]:

    # 默认值字典,区别在于普通字典key不存在会报错，默认值字典不会
    my_words = defaultdict(list)
    # 当key不存在时，会用list()来赋默认值

    for word in strs:
        key = "".join(sorted(word))
        my_words[key].append(word)
    return list(my_words.values())


if __name__ == '__main__':
    my_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_words(my_strs))
