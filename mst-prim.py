# Python 3

# para executar, digite python3 mst-prim.py nome_do_arquivo
# nome_do_arquivo: nome do arquivo contendo a representação matricial do grafo

import heapq
import sys
import numpy as np

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

def mst(u, v, w):
    size = len(u)
    mst = [[0] * size for _ in range(size)]

    for i in range(1, size):
        mst[u[i]-1][v[i]-1] = w[i]
        mst[v[i]-1][u[i]-1] = w[i]

    return np.array(mst)

def mst_prim(G, r=1):
    vert_keys = [float('inf')] * len(G)
    vert_parents = [0] * len(G)

    vert_keys[r-1] = 0
    Q = list(G.keys())
    Q_aux = list(zip(vert_keys, Q))
    heapq.heapify(Q_aux)
    
    while Q:
        _, u = heapq.heappop(Q_aux)
        i = Q.index(u)
        Q.remove(u)
        for v in G[u].keys():
            if v in Q and G[u][v] < vert_keys[v-1]:
                vert_parents[v-1] = u
                vert_keys[v-1] = G[u][v]
        key_aux = vert_keys[:i] + vert_keys[i+1:]
        Q_aux = list(zip(key_aux, Q))
        heapq.heapify(Q_aux)

    return mst(list(G.keys()), vert_parents, vert_keys)

def main():
    file = sys.argv[1]
    G = create_graph(file)
    print(mst_prim(G))

if __name__ == '__main__': main()