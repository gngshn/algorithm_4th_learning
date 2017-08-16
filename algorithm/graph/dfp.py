from algorithm.graph.graph import Graph


class DepthFirstPath(object):
    def __init__(self, g: Graph, s):
        self.s = s
        self.marked = [False] * g.v
        self.edge_to = [0] * g.v
        self.dfs(g, s)

    def dfs(self, g: Graph, v):
        self.marked[v] = True
        for w in g.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(g, w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = []
        while v != self.s:
            path.append(v)
            v = self.edge_to[v]
        path.append(self.s)
        return list(reversed(path))


if __name__ == '__main__':
    graph = Graph(file='tinyCG.txt')
    dfd = DepthFirstPath(graph, 0)
    print(graph)
    for i in range(graph.v):
        print('{}: {}'.format(i, dfd.path_to(i)))
