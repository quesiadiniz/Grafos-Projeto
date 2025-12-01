from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        pass # Apague essa instrução e inicie seu código aqui

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau_entrada(self, V=''):
        '''
        Provê o grau de entrada do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau de saída do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

 def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"Vértice '{V}' não existe no grafo.")

        rotulos = set()

        for aresta in self.arestas.values():
            if aresta.v1.rotulo == V or aresta.v2.rotulo == V:
                rotulos.add(aresta.rotulo)

        return rotulos

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass
        pass

    def dijkstra(self, v_inicial, v_final):

        beta = {}  # menor distancia
        gama = {}  # já visitado
        pi = {}    # predecessor

        for a in self.arestas.values():
            if a.peso < 0:
                raise ValueError(
                    "Erro: Nao é possivel calcular o menor caminho"
                )

        for v in self.vertices:
            beta[v] = float('inf')
            gama[v] = 0
            pi[v] = 'x'

        beta[v_inicial] = 0

        while True:

            u = None  # vertice atual
            menor = float('inf')  # valor do menor beta

            for v in self.vertices:
                if gama[v] == 0 and beta[v] < menor:
                    menor = beta[v]
                    u = v
            gama[u] = 1
