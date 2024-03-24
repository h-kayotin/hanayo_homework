"""
21_单词倒序排列 - 

Author: kayotin
Date 2024/3/24
"""
sentence = str(input())

word_list = []

left, right = 0, 0
while right < len(sentence):
    if sentence[left].isalpha():
        right = left + 1
        while right < len(sentence) and sentence[right].isalpha():
            right += 1
        word_list.append(sentence[left:right])
        left = right
    else:
        left += 1

for i in range(-1, - len(word_list)-1, -1):
    print(word_list[i], end=" ")