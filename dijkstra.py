# Python 3

# para executar, digite python3 dijkstra.py nome_do_arquivo vértice_inicial
# nome_do_arquivo: nome do arquivo contendo a representação matricial do grafo
# vértice_inicial: inteiro entre 1 e N

import heapq
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

def dijkstra(G, s):
    d = [float('inf')] * len(G)
    vert_parents = [0] * len(G)
    d[s-1] = 0

    S = []
    Q = list(G.keys())
    Q_aux = list(zip(d, Q))
    heapq.heapify(Q_aux)

    while Q:
        _, u = heapq.heappop(Q_aux)
        i = Q.index(u)
        Q.remove(u)
        S.append(u)

        for v in G[u].keys():
            if d[v-1] > d[u-1] + G[u][v]:
                d[v-1] = d[u-1] + G[u][v]
                vert_parents[v-1] = u

        key_aux = d[:i] + d[i+1:]
        Q_aux = list(zip(key_aux, Q))
        heapq.heapify(Q_aux)

    return d

def main():
    file, s = sys.argv[1], int(sys.argv[2])
    G = create_graph(file)
    print(dijkstra(G, s))

if __name__ == '__main__': main()