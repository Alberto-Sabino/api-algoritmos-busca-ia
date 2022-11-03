from math import ceil

class No(object):
    def __init__(self, pai=None, estado=None, custo=None, custoTotal=None, anterior=None, proximo=None):
        self.pai = pai
        self.estado = estado
        self.custo = custo
        self.custoTotal = custoTotal
        self.anterior = anterior
        self.proximo = proximo


class lista(object):
    head = None
    tail = None


    def inserePrimeiro(self, s, custo, custoTotal, p):
        novo_no = No(p, s, custo, custoTotal, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no


    def insereUltimo(self, s, custo, custoTotal, p):
        novo_no = No(p, s, custo, custoTotal, None, None)
        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no


    def inserePos_X(self, s, custo, custoTotal, p):
        if self.head is None:
            self.inserePrimeiro(s, custo, custoTotal, p)
        else:
            atual = self.head
            while atual.custo < custo:
                atual = atual.proximo
                if atual is None:
                    break

            if atual == self.head:
                self.inserePrimeiro(s, custo, custoTotal, p)
            else:
                if atual is None:
                    self.insereUltimo(s, custo, custoTotal, p)
                else:
                    novo_no = No(p, s, custo, custoTotal, None, None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual



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
            linha = []
            linha.append(aux.estado)
            linha.append(aux.custo)
            str.append(linha)
            aux = aux.proximo

        return str


    def exibeArvore(self):
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


    def exibeArvore1(self, s):
        atual = self.head
        while atual.estado != s:
            atual = atual.proximo

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


    def exibeArvore2(self, s, custo):
        atual = self.tail

        while atual.estado != s or atual.custo != custo:
            atual = atual.anterior

        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho


    def primeiro(self):
        return self.head


    def ultimo(self):
        return self.tail


class busca(object):

    def custo_uniforme(self, grafo, inicio, fim):
        l1 = lista()
        l2 = lista()

        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual is None:
                break
            vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            for novo in vizinhos:
                naoVisitado = True
                bloco = grafo[novo[0]][novo[1]]
                custoAtual = atual.custoTotal + \
                    bloco['value']

                for j in range(len(visitado)):
                    if visitado[j][0] == grafo[novo[0]][novo[1]]:
                        if visitado[j][1] <= custoAtual:
                            naoVisitado = False
                        else:
                            visitado[j][1] = custoAtual
                        break

                if naoVisitado:
                    l1.inserePos_X(novo, bloco['value'], custoAtual, atual)
                    l2.inserePos_X(novo, bloco['value'], custoAtual, atual)

                    linha = []
                    linha.append(bloco)
                    linha.append(custoAtual)
                    visitado.append(linha)

                    if novo == fim:
                        caminho = []
                        caminho.append(l2.exibeArvore2(
                            atual.estado, atual.custo))
                        caminho[0].reverse()
                        caminho[0].append(fim)
                        caminho.append(atual.custoTotal +
                                       grafo[fim[0]][fim[1]]['value'])
                        return caminho
        return "caminho não encontrado"


    def greedy(self, grafo, inicio, fim):
        l1 = lista()
        l2 = lista()

        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual is None:
                break

            vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            for novo in vizinhos:
                naoVisitado = True
                bloco = grafo[novo[0]][novo[1]]
                custoAtual = atual.custoTotal + ceil(bloco['value'] * 0.5)

                for j in range(len(visitado)):
                    if visitado[j][0] == grafo[novo[0]][novo[1]]:
                        if visitado[j][1] <= custoAtual:
                            naoVisitado = False
                        else:
                            visitado[j][1] = custoAtual
                        break

                if naoVisitado:
                    l1.inserePos_X(novo, bloco['value'], custoAtual, atual)
                    l2.inserePos_X(novo, bloco['value'], custoAtual, atual)

                    linha = []
                    linha.append(bloco)
                    linha.append(custoAtual)
                    visitado.append(linha)

                    if novo == fim:
                        caminho = []
                        caminho.append(l2.exibeArvore2(atual.estado, atual.custo))
                        caminho[0].reverse()
                        caminho[0].append(fim)
                        caminho.append(atual.custoTotal +
                                       grafo[fim[0]][fim[1]]['value'])
                        return caminho
        return "caminho não encontrado"


    def a_estrela(self, grafo, inicio, fim):
        l1 = lista()
        l2 = lista()
        l1.insereUltimo(inicio, 0, 0, None)
        l2.insereUltimo(inicio, 0, 0, None)

        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()

            if atual is None:
                break

            vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            for novo in vizinhos:
                naoVisitado = True
                bloco = grafo[novo[0]][novo[1]]
                custoAtual = atual.custoTotal + ceil(bloco['value'] * 0.5) + bloco['value']

                for j in range(len(visitado)):
                    if visitado[j][0] == grafo[novo[0]][novo[1]]:
                        if visitado[j][1] <= custoAtual:
                            naoVisitado = False
                        else:
                            visitado[j][1] = custoAtual
                        break


                if naoVisitado:
                    l1.inserePos_X(novo, bloco['value'], custoAtual, atual)
                    l2.inserePos_X(novo, bloco['value'], custoAtual, atual)
                    linha = []
                    linha.append(bloco)
                    linha.append(custoAtual)
                    visitado.append(linha)

                    if novo == fim:
                        caminho = []
                        caminho.append(l2.exibeArvore2(atual.estado, atual.custo))
                        caminho[0].reverse()
                        caminho[0].append(fim)
                        caminho.append(atual.custoTotal + grafo[fim[0]][fim[1]]['value'])
                        return caminho
        return "caminho não encontrado"


    def sucessor(self, grafo, x, y):
        vizinhanca = []

        if x < len(grafo[0]) - 1:
            vizinho = []
            vizinho.append(x+1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        if x > 0:
            vizinho = []
            vizinho.append(x-1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        if y < len(grafo[0]) - 1:
            vizinho = []
            vizinho.append(x)
            vizinho.append(y+1)
            vizinhanca.append(vizinho)

        if y > 0:
            vizinho = []
            vizinho.append(x)
            vizinho.append(y-1)
            vizinhanca.append(vizinho)

        return vizinhanca
