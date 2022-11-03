class No(object):
    def __init__(self, pai=None, estado=None, nivel=None, anterior=None, proximo=None):
        self.pai = pai
        self.estado = estado
        self.nivel = nivel
        self.anterior = anterior
        self.proximo = proximo


class lista(object):
    head = None
    tail = None


    def inserePrimeiro(self, st, v1, pai):
        novo_no = No(pai, st, v1, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no


    def insereUltimo(self, st, v1, pai):
        novo_no = No(pai, st, v1, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        self.tail = novo_no


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


    def primeiro(self):
        return self.head


    def ultimo(self):
        return self.tail


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
            temp.append(aux.estado)
            temp.append(aux.nivel)
            str.append(temp)
            aux = aux.proximo

        return str


    def exibeCaminho(self):
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho


    def exibeCaminho1(self, valor):
        atual = self.head

        while atual.estado != valor:
            atual = atual.proximo

        caminho = []
        atual = atual.pai

        if atual is not None:
            while atual.pai is not None:
                caminho.append(atual.estado)
                atual = atual.pai
            caminho.append(atual.estado)

        return caminho


class busca(object):

    def amplitude(self, grafo, inicio, fim):
        l1 = lista()
        l2 = lista()
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual is None: break
            vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            for v in vizinhos:
                novo = v
                naoVisitado = True

                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel+1):
                            naoVisitado = False
                        else:
                            visitado[j][1] = atual.nivel+1
                        break

                if naoVisitado:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        return caminho
        return "caminho não encontrado"



    def profundidade(self, grafo, inicio, fim):
        l1 = lista()
        l2 = lista()
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            for v in vizinhos:
                novo = v
                naoVisitado = True

                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel+1):
                            naoVisitado = False
                        else:
                            visitado[j][1] = atual.nivel+1
                        break

                if naoVisitado:
                    l1.insereUltimo(novo, atual.nivel+1, atual)
                    l2.insereUltimo(novo, atual.nivel+1, atual)
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        return caminho
        return "caminho não encontrado"


    def prof_limitada(self, grafo, inicio, fim, limite):
        l1 = lista()
        l2 = lista()
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()
            if atual is None: break
            if atual.nivel < limite:
                vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            for v in vizinhos:
                novo = v
                naoVisitado = True

                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel+1):
                            naoVisitado = False
                        else:
                            visitado[j][1] = atual.nivel+1
                        break

                if naoVisitado:
                    l1.insereUltimo(novo, atual.nivel+1, atual)
                    l2.insereUltimo(novo, atual.nivel+1, atual)
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        return caminho
        return "caminho não encontrado"


    def aprof_iterativo(self, grafo, inicio, fim, l_max):
        for limite in range(l_max):
            l1 = lista()
            l2 = lista()
            l1.insereUltimo(inicio, 0, None)
            l2.insereUltimo(inicio, 0, None)
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)

            while l1.vazio() is not None:
                atual = l1.deletaPrimeiro()
                if atual is None: break
                if atual.nivel < limite:
                    vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

                    for v in vizinhos:
                        novo = v
                        naoVisitado = True

                        for j in range(len(visitado)):
                            if visitado[j][0] == novo:
                                if visitado[j][1] <= (atual.nivel+1):
                                    naoVisitado = False
                                else:
                                    visitado[j][1] = atual.nivel+1
                                break

                        if naoVisitado:
                            l1.insereUltimo(novo, atual.nivel+1, atual)
                            l2.insereUltimo(novo, atual.nivel+1, atual)
                            linha = []
                            linha.append(novo)
                            linha.append(atual.nivel+1)
                            visitado.append(linha)

                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                return caminho
        return "caminho não encontrado"


    def bidirecional(self, grafo, inicio, fim):
        l1 = lista()
        l3 = lista()
        l2 = lista()
        l4 = lista()
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        l3.insereUltimo(fim, 0, None)
        l4.insereUltimo(fim, 0, None)
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        ni = 0

        while l1.vazio() is not None or l3.vazio() is not None:
            while l1.vazio() is not None:
                atual = l1.deletaPrimeiro()
                vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

                for v in vizinhos:
                    novo = v
                    naoVisitado = True

                    for j in range(len(visitado1)):
                        if visitado1[j][0] == novo:
                            if visitado1[j][1] <= (atual.nivel+1):
                                naoVisitado = False
                            else:
                                visitado1[j][1] = atual.nivel+1
                            break

                    if naoVisitado:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado1.append(linha)
                        naoVisitado = False

                        for j in range(len(visitado2)):
                            if visitado2[j][0] == novo:
                                naoVisitado = True
                                break

                        if naoVisitado:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho

            while l1.vazio() is not None:
                atual = l1.deletaPrimeiro()
                vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

                for v in vizinhos:
                    novo = v
                    naoVisitado = True

                    for j in range(len(visitado2)):
                        if visitado2[j][0] == novo:
                            if visitado2[j][1] <= (atual.nivel+1):
                                naoVisitado = False
                            else:
                                visitado2[j][1] = atual.nivel+1
                            break

                    if naoVisitado:
                        l3.insereUltimo(novo, atual.nivel + 1, atual)
                        l4.insereUltimo(novo, atual.nivel + 1, atual)
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado2.append(linha)
                        naoVisitado = False

                        for j in range(len(visitado1)):
                            if visitado1[j][0] == novo:
                                naoVisitado = True
                                break

                        if naoVisitado:
                            caminho = []
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
            ni += 1
        return "caminho não encontrado"


    def sucessor(self, grafo, x, y):
        vizinhanca = []

        if x < len(grafo[0]):
            vizinho = []
            vizinho.append(x+1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        if x > 0:
            vizinho = []
            vizinho.append(x-1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        if y < len(grafo[0]):
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
