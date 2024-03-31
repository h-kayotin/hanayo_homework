"""
28_字符串加密 - 

Author: kayotin
Date 2024/3/31
"""

ent_code = "nihao"
my_word = "ni"
code_a = ord("a")
code_z = ord("z")
key_list = [chr(x) for x in range(code_a, code_z + 1)]
val_list = []
for c in ent_code:
    if c not in val_list:
        val_list.append(c)
val_set = set(val_list)
for val in key_list:
    if val not in val_set:
        val_list.append(val)
print(val_list)

ent_dict = dict()
for key, val in zip(key_list, val_list):
    ent_dict[key] = val

res = ""
for c in my_word:
    res += ent_dict[c]
print(res)
