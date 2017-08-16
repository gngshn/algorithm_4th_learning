from algorithm.graph.graph import Graph


class CC(object):
    def __init__(self, g: Graph):
        self.marked = [False] * g.v
        self.id = [0] * g.v
        self.count = 0
        for w in range(g.v):
            if not self.marked[w]:
                self.dfs(g, w)
                self.count += 1

    def dfs(self, g: Graph, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.adj[v]:
            if not self.marked[w]:
                self.marked[w] = True
                self.id[w] = self.count
                self.dfs(g, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]


if __name__ == '__main__':
    graph = Graph(file='tinyG.txt')
    cc = CC(graph)
    print('{} components'.format(cc.count))
    print(cc.id)

