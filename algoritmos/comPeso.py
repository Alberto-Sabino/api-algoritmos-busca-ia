class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, custo=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.valor1    = valor1        # valor do nó na árvore
        self.custo    = custo        # custo do caminho até o nó atual
        self.anterior  = anterior
        self.proximo   = proximo

class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual


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
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
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
    
    def exibeArvore1(self,s):

        
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
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
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

    
    def greedy(self, grafo, nos, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")

                return caminho, atual.custo
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.custo + novo[1]  # custo do caminho
                v1 = h[ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1 , v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      


    def a_estrela(self, grafo, nos, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)

                return caminho, atual.custo
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.custo + novo[1]  # custo do caminho
                v1 = v2 + h[ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1 , v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"


    def sucessor(self, grafo, x, y):
        vizinhanca = []

        # vizinho da direita
        if x < len(grafo):
            vizinho = []
            vizinho.append(x+1)
            vizinho.append(y)
            vizinho.append(grafo[x+1, y])
            vizinhanca.append(vizinho)

        # vizinho da esquerda
        if x > 0:
            vizinho = []
            vizinho.append(x-1)
            vizinho.append(y)
            vizinho.append(grafo[x-1, y])
            vizinhanca.append(vizinho)

        # vizinho de cima
        if y < len(grafo[0]):
            vizinho = []
            vizinho.append(x)
            vizinho.append(y+1)
            vizinho.append(grafo[x, y+1])
            vizinhanca.append(vizinho)

        # vizinho de baixo
        if y > 0:
            vizinho = []
            vizinho.append(x)
            vizinho.append(y-1)
            vizinho.append(grafo[x, y-1])
            vizinhanca.append(vizinho)

        return vizinhanca

