"""
04_容器 - 

Author: hanayo
Date： 2024/5/16
"""
import typing

# 避免频繁扩充列表 / 创建新列表

"""所以说，为了提高性能，内建函数 range “变懒”了。 而为了避免过于频繁的内存分配，在日常编码中，我们的函数同样也需要变懒，这包括：

更多的使用 yield 关键字，返回生成器对象
尽量使用生成器表达式替代列表推导表达式
生成器表达式：(i for i in range(100)) 👍
列表推导表达式：[i for i in range(100)]
尽量使用模块提供的懒惰对象：
使用 re.finditer 替代 re.findall
直接使用可迭代的文件对象： for line in fp，而不是 for line in fp.readlines()"""

# 在列表头部操作多的场景使用 deque 模块
"""
列表是基于数组结构（Array）实现的，当你在列表的头部插入新成员（list.insert(0, item)）时，它后面的所有其他成员都需要被移动，操作的时间复杂度是 O(n)。
这导致在列表的头部插入成员远比在尾部追加（list.append(item) 时间复杂度为 O(1)）要慢。

如果你的代码需要执行很多次这类操作，请考虑使用 collections.deque 类型来替代列表。因为 deque 是基于双端队列实现的，无论是在头部还是尾部追加元素，时间复杂度都是 O(1)
"""


# 使用集合/字典来判断成员是否存在
# 判断某个元素 if x in xxx时，集合的效率最高。列表不太行


# 写扩展性更换的代码
def add_ellipsis(comments: typing.List[str], max_length: int = 12):
    """如果评论列表里的内容超过 max_length，剩下的字符用省略号代替
    """
    index = 0
    for comment in comments:
        comment = comment.strip()
        if len(comment) > max_length:
            comments[index] = comment[:max_length] + '...'
        index += 1
    return comments


# 在新函数里，我们将依赖的参数类型从列表改成了可迭代的抽象类。这样做有很多好处，一个最明显的就是：无论评论是来自列表、
# 元组或是某个文件，新函数都可以轻松满足：
def add_ellipsis_gen(comments: typing.Iterable[str], max_length: int = 12):
    """如果可迭代评论里的内容超过 max_length，剩下的字符用省略号代替
    """
    for comment in comments:
        comment = comment.strip()
        if len(comment) > max_length:
            yield comment[:max_length] + '...'
        else:
            yield comment


# 处理放在元组里的评论
comments = ("Implementation note", "Changed", "ABC for generator")
print("\n".join(add_ellipsis_gen(comments)))
