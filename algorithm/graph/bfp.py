from collections import deque

from algorithm.graph.graph import Graph


class BreadthFirstPath(object):
    def __init__(self, g: Graph, s):
        self.s = s
        self.marked = [False] * g.v
        self.edge_to = [0] * g.v
        self.bfs(g, s)

    def bfs(self, g: Graph, v):
        q = deque()
        q.appendleft(v)
        self.marked[v] = True
        while q:
            w = q.pop()
            for x in g.adj[w]:
                if not self.marked[x]:
                    q.appendleft(x)
                    self.marked[x] = True
                    self.edge_to[x] = w

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
    bfd = BreadthFirstPath(graph, 0)
    print(graph)
    print(bfd.edge_to)
    for i in range(graph.v):
        print('{}: {}'.format(i, bfd.path_to(i)))
