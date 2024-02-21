"""
03_图的遍历 - 

Author: kayotin
Date 2024/2/21
"""
from b_图_邻接表 import GraphAdjList, Vertex
from collections import deque


def vals_to_vets(vals: list[int]) -> list[Vertex]:
    """输入值列表 vals ，返回顶点列表 vets"""
    return [Vertex(val) for val in vals]


def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """广度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res = []
    # 记录已经访问过的顶点
    visited = set[Vertex]([start_vet])
    # 队列用于实现dfs
    que = deque[Vertex]([start_vet])
    # 循环访问
    while len(que):
        vet = que.popleft()
        res.append(vet)
        # 遍历所有相邻顶点
        for adj_vet in graph.adj_list[vet]:
            # 跳过已访问的顶点
            if adj_vet in visited:
                continue
            # 入队未访问过的顶点
            que.append(adj_vet)
            visited.add(adj_vet)
    return res


def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    """深度优先遍历辅助函数"""
    res.append(vet)  # 记录访问顶点
    visited.add(vet)  # 标记该顶点已被访问
    # 遍历该顶点所有相邻顶点
    for adj_vet in graph.adj_list[vet]:
        if adj_vet in visited:
            continue
        # 递归访问相邻节点
        dfs(graph, visited, res, adj_vet)


def graph_dfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """深度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res = []
    # 哈希表，用于记录已被访问过的顶点
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res


if __name__ == '__main__':
    v = vals_to_vets([1, 3, 2, 5, 4])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
        [v[2], v[4]],
        [v[3], v[4]],
        ]
    my_graph = GraphAdjList(edges)
    graph_res = graph_dfs(my_graph, v[0])
    for n in graph_res:
        print(n.val)
