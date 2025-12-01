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


print(g_p.bfs("J"))

# Dijkstra
from meu_grafo_lista_adj_dir import  MeuGrafo

def test_dijkstra(self):
        """
        Testa o funcionamento do Dijkstra no grafo manual g_p_sem_paralelas.
        """
        beta, pi = self.g_p_sem_paralelas.dijkstra("J")

        esperado_beta = {
            'J': 0,    # origem
            'C': 2,    # J → C
            'E': 5,    # J → C → E   (2 + 3)
            'P': 4,    # J → C → P   (2 + 2)
            'M': 6,    # J → C → M   (2 + 4)
            'T': 7,    # J → C → M → T  (2 + 4 + 1)
            'Z': 9     # J → C → M → T → Z  (2 + 4 + 1 + 2)
        }

        self.assertEqual(beta, esperado_beta)

        # Predecessores esperados
        esperado_pi = {
            'J': None,
            'C': 'J',
            'E': 'C',
            'P': 'C',
            'M': 'C',
            'T': 'M',
            'Z': 'T'
        }

        self.assertEqual(pi, esperado_pi)

