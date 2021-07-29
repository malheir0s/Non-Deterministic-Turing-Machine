class Linguagem:
    def __init__(self):
        self.estados = []
        self.simbolos = []
        self.alfabetoPilha = []
        self.dicionario = dict()
        self.palavrasTeste = []
        self.estadosFinais = []
        self.pilhaTransicoes = []
        self.limitanteEsquerda = ''
        self.simboloBranco = ''

    def lerTransicoes(self, num):
        for i in range (0, num):
            transicoes = input().split()
            self.criarDicionario(transicoes)

    def criarDicionario(self, transicoes):
        dupla = transicoes[0]+transicoes[1]
        if(dupla in self.dicionario):
            self.dicionario[dupla] = self.dicionario[dupla] + [[transicoes[2],transicoes[3], transicoes[4]]]
        else:
            novaTransicao = {transicoes[0]+transicoes[1]:[[transicoes[2],transicoes[3], transicoes[4]]]}
            self.dicionario.update(novaTransicao)


    def escrever(self, fita, caractere, registrador):
      nova_fita = fita.copy()
      nova_fita[registrador] = caractere
      return nova_fita

    def mover(self, fita, registrador, direcao):
      if(direcao == 'I'):
        return registrador
      elif(direcao == 'E'):
        if(registrador == 0):
          return registrador
        return registrador - 1
      elif(direcao == 'D'):
        if(len(fita)-1 == registrador):
          fita.append(self.simboloBranco)
        return  registrador + 1

    def validarTransicao(self, estadoAtual, fita, registrador, pilhaTransicoes):
        parou = True
        caractereLido = fita[registrador]
        if((estadoAtual+caractereLido) in self.dicionario):
          parou = False
          duplas = self.dicionario.get(estadoAtual+caractereLido)
          for dupla in duplas:
           novoRegistrador = self.mover(fita, registrador, dupla[2])
           pilhaTransicoes.append([dupla[0], self.escrever(fita, dupla[1], registrador), novoRegistrador])
        
        return parou

   

    def isAccepted(self, estado, parou):
      if(parou and estado in self.estadosFinais):
        return True
      else:
        return False


    def percorrerPilhaTransicoes(self, palavra, estadoInicial):
        fita = list(palavra)
        fita.insert(0, self.limitanteEsquerda)
        fita.append(self.simboloBranco)
        self.pilhaTransicoes = [[estadoInicial, fita, 1]]
        aceita = False
        while (not (len(self.pilhaTransicoes)==0)):
            novaPilhaTransicoes = []
            for pilha in self.pilhaTransicoes:  
              parou = self.validarTransicao(pilha[0], pilha[1], pilha[2], novaPilhaTransicoes)
              if(self.isAccepted(pilha[0], parou)):
                aceita = True
                break

            if(aceita):
              break
            self.pilhaTransicoes = novaPilhaTransicoes
       
        
        if(aceita):
            print('S')
        else:
            print('N')
            




L1 = Linguagem()
L1.estados = input()
L1.simbolos = input()
L1.alfabetoPilha = input()
L1.limitanteEsquerda = input()
L1.simboloBranco = input()
numeroTransicoes = int(input())
L1.lerTransicoes(numeroTransicoes)
estadoInicial = input()
L1.estadosFinais = input().split()
L1.palavrasTeste = input().split()


import time

for words in L1.palavrasTeste:
    start_time = time.perf_counter()
    L1.percorrerPilhaTransicoes(words, estadoInicial)
    print("--- %s ms ---" % ((time.perf_counter() - start_time)*1000.0))  