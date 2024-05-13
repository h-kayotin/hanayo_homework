"""
62_课程表 - 
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，
表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。


Author: hanayo
Date： 2024/5/13
"""
from collections import deque


def can_finish(numCourses, prerequisites: list[list]):
    in_degrees = [0 for _ in range(numCourses)]
    adjacency = [[] for _ in range(numCourses)]
    queue = deque()

    for cur, pre in prerequisites:
        in_degrees[cur] += 1
        adjacency[pre].append(cur)

    for i in range(len(in_degrees)):
        if not in_degrees[i]:
            queue.append(i)

    while queue:
        pre = queue.popleft()
        numCourses -= 1
        for cur in adjacency[pre]:
            in_degrees[cur] -= 1
            if not in_degrees[cur]:
                queue.append(cur)
    return not numCourses
