"""
01_图_邻接矩阵 - 用邻接矩阵实现图

Author: hanayo
Date： 2024/2/21
"""


class GraphAdjMat:
    """基于邻接矩阵实现的无向图类"""
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        """构造方法"""
        # 顶点列表,元素代表“顶点值”，索引代表“顶点索引”
        self.vertices: list[int] = []
        # 邻接矩阵，行列索引对应“顶点索引”
        self.adj_mat: list[list[int]] = []
        # 添加顶点
        for val in vertices:
            self.add_vertex(val)
        # 添加边, edges代表的是顶点的索引
        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self):
        """获取顶点数量"""
        return len(self.vertices)

    def add_vertex(self, val: int):
        """添加顶点"""
        n = self.size()
        # 向顶点列表添加新值
        self.vertices.append(val)
        new_row = [0] * n
        # 邻接矩阵中添加新行
        self.adj_mat.append(new_row)
        # 邻接矩阵中添加新列
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self, index: int):
        """删除顶点"""
        if index > self.size():
            raise IndexError()
        self.vertices.pop(index)
        # 在邻接矩阵中删除索引行
        self.adj_mat.pop(index)
        # 在临界矩阵中删除索引列
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        """添加边"""
        if i < 0 or j < 0 or j > self.size() or i > self.size():
            raise IndexError()
        # 参数i，j对应顶点索引
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        """删除边"""
        if i < 0 or j < 0 or j > self.size() or i > self.size():
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    def print(self):
        """打印邻接矩阵"""
        print("顶点：", self.vertices)
        print("邻接矩阵：")
        for row in self.adj_mat:
            print(row)


if __name__ == '__main__':
    vertices = [1, 3, 2, 5, 4]
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjMat(vertices, edges)

    graph.print()
