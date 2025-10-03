from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *

#teste commit / push git
class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

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
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        # grau=0
        # for a in self.vertices[V]:
        #     grau = grau+1
        # return grau
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"Vértice '{V}' não existe no grafo.")

        grau = 0
        for aresta in self.arestas:
            if self.arestas[aresta].v1.rotulo == V:
                grau +=1

            if self.arestas[aresta].v2.rotulo == V:
                grau += 1
        return grau
        # for i in self.arestas:
        #     if self.arestas.v1 == V or self.arestas.v2 == V:
        #         grau +=1
        #
        #     elif self.arestas.v1 == self.arestas.v2 == V:
        #         grau +=1
        # return grau



    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a in self.arestas:
            v1 = self.arestas[a].v1
            v2 = self.arestas[a].v2
            for i in self.arestas:
                if i!=a and self.arestas[i].v1 == v1 and self.arestas[i].v2 == v2:
                    return True
                elif i!=a and self.arestas[i].v1 == v2 and self.arestas[i].v2 == v1:
                    return True
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        rotulos = set()
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"Vértice '{V}' não existe no grafo.")

        for a in self.arestas:
            rotulo_V1 = self.arestas[a].v1.rotulo
            rotulo_V2 = self.arestas[a].v2.rotulo

            if rotulo_V1 == V:
                rotulos.add(self.arestas[a].rotulo)
            elif rotulo_V2 == V:
                rotulos.add(self.arestas[a].rotulo)

        return rotulos


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for a in self.arestas:
            v1 = self.arestas[a].v1
            for i in self.arestas:
                if i!=a and self.arestas[i].v1==v1:
                    return False
                elif i!=a and self.arestas[i].v2==v1:
                    return False

        return True


