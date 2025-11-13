from meu_grafo_lista_adj_nao_dir import MeuGrafo

g_p = MeuGrafo()
g_p.adiciona_vertice("J")
g_p.adiciona_vertice("C")
g_p.adiciona_vertice("E")
g_p.adiciona_vertice("P")
g_p.adiciona_vertice("M")
g_p.adiciona_vertice("T")
g_p.adiciona_vertice("Z")
g_p.adiciona_aresta('a1', 'J', 'C')
g_p.adiciona_aresta('a2', 'C', 'E')
g_p.adiciona_aresta('a3', 'P', 'C')
g_p.adiciona_aresta('a4', 'T', 'C')
g_p.adiciona_aresta('a5', 'M', 'C')
g_p.adiciona_aresta('a6', 'M', 'T')
g_p.adiciona_aresta('a7', 'T', 'Z')


print(g_p.grafo_dfs("C"))
