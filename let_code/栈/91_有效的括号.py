"""
91_有效的括号 - 
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
Author: hanayo
Date： 2024/6/20
"""


def is_valid(s: str) -> bool:
    hash_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
        "?": "?"
    }
    stack = ['?']
    for c in s:
        if c in hash_dict:
            stack.append(c)
        elif hash_dict[stack.pop()] != c:
            return False
    return len(stack) == 1
