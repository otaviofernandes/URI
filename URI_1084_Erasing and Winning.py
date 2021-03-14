'''
Problema 1084 - URI Online Judge - https://www.urionlinejudge.com.br/judge/pt/problems/view/1084
Resolução proposta por otaviofernandes - https://github.com/otaviofernandes
'''

n, d = map(int, input().split())                            # recebe valores de n(quantidade de posições do número) e d(quantidade de posições que devem ser apagadas).
while n != 0 and d != 0:                                    # testa se n e d são diferentes de zero.
    n1, d1 = n, d                                           # cria as variáveis auxiliáres n1 e d1, para teste em if da linha 17.
    numero = input()                                        # variável numero recebe número original, com n posições.
    pilha = []                                              # cria pilha para testar posições maiores e apagar menores.
    for i in numero:                                        # percorre a váriável número.
        pilha.append(i)                                     # incrementa o valor de número na posição i, para posterior teste no laço while.
        while len(pilha)>1 and pilha[-1]>pilha[-2] and d>0: #laço responsável por remover valores da pilha que forem menores que o valor do topo.
            pilha.pop(-2)
            d -= 1
    pilha = ''.join(pilha)                                  # transforma a pilha em string.
    if len(pilha) > (n1 - d1):                              #testa se a pilha tem elementos a mais na sua direita, que devem ser eliminados.
        pilha = (pilha[0:n1 - d1])
    print(pilha)
    n, d = map(int, input().split())                        #reinicia as entradas dos valores de n e d para o próximo teste.
