class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai = pai
        self.valor1 = valor1
        self.valor2 = valor2
        self.anterior = anterior
        self.proximo = proximo


class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo

        return str

    def exibeCaminho(self):

        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        caminho = caminho[::-1]
        return caminho

    def exibeCaminho1(self, valor):

        atual = self.head
        while atual.valor1 != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho

    def primeiro(self):
        return self.head

    def ultimo(self):
        return self.tail


class busca(object):

    def amplitude(self, inicio, fim, mapa):

        caminho = []
        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            filhos = []
            filhos = self.sucessor(mapa, atual.valor1[0], atual.valor1[1])

            # varre todos as conexões dentro do grafo a partir de atual
            for f in filhos:

                novo = f
                naoVisitado = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.valor2+1):
                            naoVisitado = False
                        else:
                            visitado[j][1] = atual.valor2+1
                        break

                # se não foi visitado inclui na fila
                if naoVisitado:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        # print("Árvore de busca:\n", l2.exibeLista())
                        return caminho

        return "caminho não encontrado"

    def custo(self, x, y):
        if mapa[x][y] == 0:
            return 1
        elif mapa[x][y] == 1:
            return 1.2

    def sucessor(self, mapa, x, y):
        vizinhanca = []

        #vizinho da direita
        if x < len(mapa):
            vizinho = []
            vizinho.append(x+1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        #vizinho da esquerda
        if x > 0:
            vizinho = []
            vizinho.append(x-1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        #vizinho de cima
        if y < len(mapa[0]):
            vizinho = []
            vizinho.append(x)
            vizinho.append(y+1)
            vizinhanca.append(vizinho)

        #vizinho de baixo
        if y > 0:
            vizinho = []
            vizinho.append(x)
            vizinho.append(y-1)
            vizinhanca.append(vizinho)

        return vizinhanca


mapa = [
    [0, 1, 2, 1, 0, 9],
    [0, 1, 2, 1, 0, 9],
    [0, 1, 2, 1, 0, 9],
    [0, 1, 2, 1, 0, 9],
    [0, 1, 2, 1, 0, 9],
    [0, 1, 2, 1, 0, 9]
]


sol = busca()
caminho = []


# PROBLEMA C
origem = [5, 5]
destino = [2, 0]


caminho = sol.amplitude(origem, destino, mapa)
print("\nAmplitude.......: ", caminho)
