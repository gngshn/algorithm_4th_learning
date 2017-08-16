from io import StringIO


class Graph(object):
    def __init__(self, v=0, file=''):
        if v:
            self.v, self.e = v, 0
            self.adj = []
            for i in range(self.v):
                self.adj.append([])
        elif file:
            with open(file, 'r') as f:
                self.v = int(f.readline())
                self.e = int(f.readline())
                self.adj = []
                for i in range(self.v):
                    self.adj.append([])
                for i in range(self.e):
                    a, b = (int(x) for x in f.readline().split())
                    self.add_edge(a, b)
        else:
            raise Exception('you must set v or file')

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.e += 1

    def __str__(self):
        s = StringIO()
        s.write(str(self.v) + ' vertices, ' + str(self.e) + ' edges\n')
        for v in range(self.v):
            s.write(str(v) + ': ' + str(self.adj[v]))
            s.write('\n')
        return s.getvalue()


if __name__ == '__main__':
    g = Graph(file='tinyG.txt')
    print(g)
