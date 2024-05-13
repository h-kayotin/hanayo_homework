"""
63_实现Trie前缀树 -

Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

Author: hanayo
Date： 2024/5/13
"""


class Trie:
    def __init__(self):
        # 初始化根节点
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        # 从根节点开始插入
        current = self
        for char in word:
            # 如果当前字符不在子节点中，创新新的trie实例作为节点
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        # 设置单词结束标志
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        # 从根节点开始搜索
        current = self
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.children)