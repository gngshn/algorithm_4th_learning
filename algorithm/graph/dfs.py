from algorithm.graph.graph import Graph


class DepthFirstSearch(object):
    def __init__(self, g: Graph, s):
        self.s = s
        self.marked = [False] * g.v
        self.count = 0
        self.dfs(g, s)

    def dfs(self, g: Graph, v):
        self.marked[v] = True
        self.count += 1
        for w in g.adj[v]:
            if not self.marked[w]:
                self.dfs(g, w)

    def is_marked(self, w):
        return self.marked[w]


if __name__ == '__main__':
    graph = Graph(file='tinyG.txt')
    dfs = DepthFirstSearch(graph, 1)
    print(dfs.marked)
    dfs = DepthFirstSearch(graph, 7)
    print(dfs.marked)
    dfs = DepthFirstSearch(graph, 9)
    print(dfs.marked)
