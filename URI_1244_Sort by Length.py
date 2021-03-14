n = int(input())

for i in range(n):
    tamanho = []
    palavras = input()
    total = len(palavras)
    palavras = palavras.split()
    for comp in palavras:
        a = len(comp)
        if a not in tamanho:
            tamanho.append(a)
    tamanho = sorted(tamanho, reverse = True)
    final = ''
    for x in tamanho:
        for palavra in palavras:
            if len(palavra) == x:
                final += palavra
                final += ' '
    final = final.rstrip(' ')
    final += ' ' * (total-len(final))
    print(final)

