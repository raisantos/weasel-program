import random
import string

padrao = "RAI SANTOS DA SOLEDADE"
lista = []
pontuacao = []
probabilidade = 25
maior_pontuacao = 0

for i in range(10):
    lista.append(padrao)
    pontuacao.append(0)

while(maior_pontuacao != len(padrao)):
    for i in range(10):
        copia = lista[i]
        pontos = 0
        for j in range(len(padrao)):
            numero_aleatorio = random.randint(1,100)
            if(numero_aleatorio <= probabilidade):
                caracter_aleatorio = random.choice(string.ascii_uppercase+' ')
                copia = copia[:j]+caracter_aleatorio+copia[j+1:]
        lista[i] = copia
        for k in range(len(padrao)):
            #print(copia+' '+padrao+' ')
            if(copia[k] == padrao[k]):
                pontos+=1
        pontuacao[i] = pontos
        #print(copia+' '+padrao+' ')
    maior_pontuacao = max(pontuacao)
    print("maior-score-atual: "+str(maior_pontuacao)+" "+lista[pontuacao.index(maior_pontuacao)])
#print(lista[pontuacao.index(maior_pontuacao)]+" score: "+str(maior_pontuacao))
