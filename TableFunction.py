import pandas as pd  # apenas para impressão da tabela

class TableFunction:
    def __init__(self, node: int = 0, edges: int = 0, adj_list: list[list[tuple[int, int]]] = None, node_list: list[list[str, str, int, int, list[str]]] = None):
        self.node = node
        self.edges = edges
        self.adj_list = adj_list or [[] for _ in range(node)]
        self.node_list = node_list or [[] for _ in range(node)]

    def exibe_csv(self,file_name):
        tabela = pd.read_csv(file_name)
        return tabela

    def le_arquivo(self, file_name):
        with open(file_name, encoding="utf8") as file:
            linhas = file.readlines()
            self.node = len(linhas) - 1
            self.node_list.append([None, 's', 0, 0, [None]])
            for i in range(1, len(linhas)):
                linha = linhas[i]
                aux = linha.split(',')
                inteiro2 = int(aux[2])
                inteiro3 = int(aux[3])
                string = aux[4].strip()
                if string == '':
                    string = None

                vetString = string.split(';') if string is not None else [string]
                self.node_list.append([aux[0], aux[1], inteiro2, inteiro3, vetString])

            self.node_list.append([None, 't', 0, 0, None])
            self.node += 2
            
            self.lista_adjacencia = [[] for i in range(self.node)]
            for u in range(1, self.node - 1):
                v = self.node - 1
                self.add_directed_edge(u, v, self.node_list[u][3])

    def aresta_auxiliar(self, string):
        for u in range(1, self.node):
            if string == self.node_list[u][0]:
                return u

    def adiciona_aresta(self):
        for v in range(1, self.node-1):
            if self.node_list[v][4] == [None]:
                self.add_directed_edge(0, v, 0)
            else:
                string = self.node_list[v][4]
                num = len(string)
                teste = self.node_list[v][3]
                for aux in range(num):
                    u = self.aresta_auxiliar(string[aux])
                    self.add_directed_edge(u, v, self.node_list[u][3])

    def add_directed_edge(self, u: int, v: int, w: int):
        if u < 0 or u >= len(self.lista_adjacencia) or v < 0 or v >= len(self.lista_adjacencia):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node - 1})")
        self.lista_adjacencia[u].append((v, w))
        self.edges += 1

    def dijkstra_max(self, s):
        dist = [float("-inf")] * self.node
        pred = [-1] * self.node
        dist[s] = 0
        Q = [i for i in range(self.node)]
        while Q != []:
            u = self.min_dist_Q(Q, dist)
            Q.remove(u)
            for (v, w) in self.lista_adjacencia[u]:
                if dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
        return dist, pred

    def min_dist_Q(self, Q, dist):
        min_dist = float("-inf")
        min_node = -1
        for node in Q:
            if dist[node] > min_dist:
                min_dist = dist[node]
                min_node = node
        return min_node

    def rec_caminho(self, s, t, pred):
        #funcao para recuperar caminho
        C = [t]
        aux = t
        while(aux != s):
            aux = pred[aux]
            C.insert(0, aux)
        return C

    def caminho_critico(self):
        dist, pred = self.dijkstra_max(0)

        max_dist_node = dist.index(max(dist))
        path = self.rec_caminho(0, max_dist_node, pred)

        node_names = [self.node_list[j][1] for j in path[1:-1]]

        return max(dist), path, node_names