class Dijkstra:
    def __init__(self, v, tree, root):
        self.tree = tree
        self.v = v
        self.d = [float('inf') for i in range(len(v))]
        self.p = [None for i in range(len(v))]
        self.s = []
        self.s_var = v
        self.d[root] = 0
    
    def dijkstra(self):
        for node in range(len(self.v)):
            print(f"times: {node}")
            min_d = float('inf')
            
            for i in self.s_var:
                if self.d[i] < min_d:
                    min_d = self.d[i]
                    min_node = i
            self.s_var.remove(min_node)
            self.s.append(min_node)
            for i in range(len(self.tree[min_node])):
                if self.tree[min_node][i] != 0:
                    if self.d[i] > self.d[min_node] + self.tree[min_node][i]:
                        self.d[i] = self.d[min_node] + self.tree[min_node][i]
                        self.p[i] = min_node
                    
            d_list = ', '.join([f"d[{i}]: "+str(d) for i,d in enumerate(self.d)])
            print(d_list)

            p_list = ', '.join([f"p[{i}]: "+str(p) for i,p in enumerate(self.p)])
            print(p_list)
            print()

    def min_path(self, end_node):
        path = []
        path.append(end_node)
        node = end_node
        while self.p[node] != None:
            node = self.p[node]
            path.append(node)

        path.reverse()
        path = ' -> '.join([str(i) for i in path])
        print(f"Minimum Path : {path}")


if __name__ == '__main__':
    v = [0, 1, 2, 3, 4]
    tree  = [
        [0, 50, 80, 0, 0],
        [0, 0, 20, 15, 0],
        [0, 0, 0, 10, 15],
        [0, 0, 0, 0, 30],
        [0, 0, 0, 0, 0]
    ]
    dijkstra = Dijkstra(v, tree, 0)
    dijkstra.dijkstra()
    dijkstra.min_path(4)
