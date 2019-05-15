# Python 3

# para executar, digite python3 bellman_ford.py nome_do_arquivo vértice_inicial
# nome_do_arquivo: nome do arquivo contendo a representação matricial do grafo
# vértice_inicial: inteiro entre 1 e N

import sys

# Cria o grafo a partir do arquivo
def create_graph(file):
    graph = []

    with open(file, 'r') as f:
        for row in f:
            row = row.replace('\n', '')
            row = row.split(',')
            row = [int(x) for x in row]
            graph.append(row)

    g = {}
    m = 1

    for row in graph:
        n = len(row)
        l = {}
        for i in range(n):
            if row[i] > 0:
                l[i+1] = row[i]
        
        g[m] = l
        m = m + 1

    return g

# Cria as arestas no formato (weight, u, v)
def create_edges(G):
    edges = []

    for u in G.keys():
        for v in G[u].keys():
                edges.append((G[u][v], u, v))

    return edges

def bellman_ford(G, s):
    d = [float('inf')] * len(G)
    vert_parents = [0] * len(G)
    d[s-1] = 0

    edges = create_edges(G)

    for i in range(len(G) - 1):
        for edge in edges:
            w, u, v = edge
            if d[v-1] > d[u-1] + w:
                d[v-1] = d[u-1] + w
                vert_parents[v-1] = u

    for edge in edges:
        w, u, v = edge
        if d[v-1] > d[u-1] + w:
            return False
    
    return d

def main():
    file, s = sys.argv[1], int(sys.argv[2])
    G = create_graph(file)
    print(bellman_ford(G, s))

if __name__ == '__main__': main()
    


