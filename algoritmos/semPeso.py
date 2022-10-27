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

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, v1, pai):
        novo_no = No(pai, st, v1, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, v1, pai):

        novo_no = No(pai, st, v1, None, None)

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

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head

    # RETORNA O ÚLTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False

    # EXIBE O CONTEÚDO DA LISTA
    def exibeLista(self):

        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.nivel)
            str.append(tempai)
            aux = aux.proximo

        return str

    # EXIBE O CAMINHO ENCONTRADO
    def exibeCaminho(self):
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho

    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
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
    # BUSCA EM AMPLITUDE
    def amplitude(self, grafo, inicio, fim):

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
            # if atual is None: break

            vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            # varre todos as conexões dentro do grafo a partir de atual
            for v in vizinhos:

                novo = v
                naoVisitado = True  # pressuponho que não foi visitado

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel+1):
                            naoVisitado = False
                        else:
                            visitado[j][1] = atual.nivel+1
                        break

                # se não foi visitado inclui na fila
                if naoVisitado:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"

    # BUSCA EM PROFUNDIDADE

    def profundidade(self, grafo, inicio, fim):
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
            vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            # varre todos as conexões dentro do grafo a partir de atual
            for v in vizinhos:

                novo = v
                naoVisitado = True  # pressuponho que não foi visitado

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel+1):
                            naoVisitado = False
                        else:
                            visitado[j][1] = atual.nivel+1
                        break

                # se não foi visitado inclui na fila
                if naoVisitado:
                    l1.insereUltimo(novo, atual.nivel+1, atual)
                    l2.insereUltimo(novo, atual.nivel+1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho
        return "caminho não encontrado"

    # BUSCA EM PROFUNDIDADE

    def prof_limitada(self, grafo, inicio, fim, limite):
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
            if atual is None: break
            if atual.nivel < limite:
                vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

            # varre todos as conexões dentro do grafo a partir de atual
            for v in vizinhos:
                novo = v
                naoVisitado = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel+1):
                            naoVisitado = False
                        else:
                            visitado[j][1] = atual.nivel+1
                        break

                # se não foi visitado inclui na fila
                if naoVisitado:
                    l1.insereUltimo(novo, atual.nivel+1, atual)
                    l2.insereUltimo(novo, atual.nivel+1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        # print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho
        return "caminho não encontrado"

    # BUSCA EM PROFUNDIDADE

    def aprof_iterativo(self, grafo, inicio, fim, l_max):

        for limite in range(l_max):

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
                atual = l1.deletaPrimeiro()
                if atual is None: break
                if atual.nivel < limite:
                    vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

                    # varre todos as conexões dentro do grafo a partir de atual
                    for v in vizinhos:
                        novo = v
                        naoVisitado = True  # pressuponho que não foi visitado

                        # controle de nós repetidos
                        for j in range(len(visitado)):
                            if visitado[j][0] == novo:
                                if visitado[j][1] <= (atual.nivel+1):
                                    naoVisitado = False
                                else:
                                    visitado[j][1] = atual.nivel+1
                                break

                        # se não foi visitado inclui na fila
                        if naoVisitado:
                            l1.insereUltimo(novo, atual.nivel+1, atual)
                            l2.insereUltimo(novo, atual.nivel+1, atual)

                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.nivel+1)
                            visitado.append(linha)

                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                # print("Fila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho
        return "caminho não encontrado"

    # BUSCA BIDIRECIONAL

    def bidirecional(self, grafo, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()
        l3 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
        l4 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)
        l3.insereUltimo(fim, 0, None)
        l4.insereUltimo(fim, 0, None)

        # controle de nós visitados
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
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
                vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

                # varre todos as conexões dentro do grafo a partir de atual
                for v in vizinhos:
                    novo = v
                    naoVisitado = True  # pressuponho que não foi visitado

                    # controle de nós repetidos
                    for j in range(len(visitado1)):
                        if visitado1[j][0] == novo:
                            if visitado1[j][1] <= (atual.nivel+1):
                                naoVisitado = False
                            else:
                                visitado1[j][1] = atual.nivel+1
                            break

                    # se não foi visitado inclui na fila
                    if naoVisitado:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado1.append(linha)

                        # verifica se é o objetivo
                        naoVisitado = False
                        for j in range(len(visitado2)):
                            if visitado2[j][0] == novo:
                                naoVisitado = True
                                break

                        if naoVisitado:
                            caminho = []
                            # print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho

            while l1.vazio() is not None:
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
                vizinhos = self.sucessor(grafo, atual.estado[0], atual.estado[1])

                # varre todos as conexões dentro do grafo a partir de atual
                for v in vizinhos:
                    novo = v
                    naoVisitado = True  # pressuponho que não foi visitado

                    # controle de nós repetidos
                    for j in range(len(visitado2)):
                        if visitado2[j][0] == novo:
                            if visitado2[j][1] <= (atual.nivel+1):
                                naoVisitado = False
                            else:
                                visitado2[j][1] = atual.nivel+1
                            break

                    # se não foi visitado inclui na fila
                    if naoVisitado:
                        l3.insereUltimo(novo, atual.nivel + 1, atual)
                        l4.insereUltimo(novo, atual.nivel + 1, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado2.append(linha)

                        # verifica se é o objetivo
                        naoVisitado = False
                        for j in range(len(visitado1)):
                            if visitado1[j][0] == novo:
                                naoVisitado = True
                                break

                        if naoVisitado:
                            caminho = []
                            # print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]

            ni += 1

        return "caminho não encontrado"

    def sucessor(self, grafo, x, y):
        vizinhanca = []

        # vizinho da direita
        if x < len(grafo):
            vizinho = []
            vizinho.append(x+1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        # vizinho da esquerda
        if x > 0:
            vizinho = []
            vizinho.append(x-1)
            vizinho.append(y)
            vizinhanca.append(vizinho)

        # vizinho de cima
        if y < len(grafo[0]):
            vizinho = []
            vizinho.append(x)
            vizinho.append(y+1)
            vizinhanca.append(vizinho)

        # vizinho de baixo
        if y > 0:
            vizinho = []
            vizinho.append(x)
            vizinho.append(y-1)
            vizinhanca.append(vizinho)

        return vizinhanca
