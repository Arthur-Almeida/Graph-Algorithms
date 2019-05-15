# Python 3

# para executar, digite python3 mst-kruskal.py nome_do_arquivo
# nome_do_arquivo: nome do arquivo contendo a representação matricial do grafo

import sys
import numpy as np

parent = {}
rank = {}

def make_set(v):
    if v not in parent.keys():
        parent[v] = v
        rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

def union(u, v):
    uRoot = find(u)
    vRoot = find(v)

    # u e v já estão no mesmo conjunto
    if uRoot == vRoot:
        return 

    # u e v não estão no mesmo conjunto
    if rank[uRoot] < rank[vRoot]:
        # Troca uRoot por vRoot
        rank[uRoot], rank[vRoot] = rank[vRoot], rank[uRoot]

    # União
    parent[vRoot] = uRoot
    if rank[uRoot] == rank[vRoot]:
        rank[uRoot] += 1

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

def create_edges(G):
    edges = []

    for u in G.keys():
        for v in G[u].keys():
                edges.append((G[u][v], u, v))

    return edges

def mst(G, A):
    size = len(G)
    mst = [[0] * size for _ in range(size)]

    for edge in A:
        w, u, v = edge
        mst[u-1][v-1] = w
        mst[v-1][u-1] = w

    return np.array(mst)

def mst_kruskal(G):
    A = []
    
    for v in G.keys():
        make_set(v)

    edges = create_edges(G)
    edges.sort()

    for edge in edges:
        _, u, v = edge
        if find(u) != find(v):
            A.append(edge)
            union(u, v)
    
    return mst(G, A)

def main():
    file = sys.argv[1]
    G = create_graph(file)
    print(mst_kruskal(G))

if __name__ == '__main__': main()