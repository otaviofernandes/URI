#https://www.urionlinejudge.com.br/judge/en/problems/view/1121
# resolução por otaviofernandes - https://github.com/otaviofernandes

def recebe_matriz(n,m):
    matriz = []
    pos_ini = [0,0]
    indicador = ''
    linha_i = '#'* (m+2)
    linha_i = list(linha_i)
    matriz.append(linha_i)
    for i in range(n):
        linha = input()
        linha = '#' + linha + '#'
        if "N" in linha: 
            pos_ini[0] = i + 1
            pos_ini[1] = linha.index("N")
            indicador = "N"
        elif "S" in linha:
            pos_ini[0] = i + 1
            pos_ini[1] = linha.index("S")
            indicador = "S"
        elif "L" in linha:
            pos_ini[0] = i + 1
            pos_ini[1] = linha.index("L")
            indicador = "L"
        elif "O" in linha:
            pos_ini[0] = i + 1
            pos_ini[1] = linha.index("O")
            indicador = "O"
        linha = list(linha)
        matriz.append(linha)
    linha_f = '#'* (m+2)
    linha_f = list(linha_f)
    matriz.append(linha_f)
    return matriz, pos_ini, indicador
#--------------------------------------------------------------
def resultado(matriz, pos_ini, indicador, n, m):
    resultado = 0
    comandos = input()
    for x in comandos:
        if x == 'D':
            if indicador == 'N':
                indicador = 'L'
            elif indicador == 'L':
                indicador = 'S'
            elif indicador == 'S':
                indicador = 'O'
            elif indicador == 'O':
                indicador = 'N'
        elif x == 'E':           
            if indicador == 'N':
                indicador = 'O'
            elif indicador == 'O':
                indicador = 'S'
            elif indicador == 'S':
                indicador = 'L'
            elif indicador == 'L':
                indicador = 'N'
        elif x == 'F':
            if indicador == 'N' and matriz[pos_ini[0] -1][pos_ini[1]] != '#':
                pos_ini[0] -= 1
            elif indicador == 'O' and matriz[pos_ini[0]][pos_ini[1]-1] != '#':
                pos_ini[1] -= 1              
            elif indicador == 'S' and matriz[pos_ini[0] +1][pos_ini[1]] != '#':
                pos_ini[0] += 1            
            elif indicador == 'L' and matriz[pos_ini[0]][pos_ini[1]+1] != '#':
                pos_ini[1] += 1
            if matriz[pos_ini[0]][pos_ini[1]] == '*':
                resultado += 1
                matriz[pos_ini[0]][pos_ini[1]] = '.'
    return resultado
#--------------------------------------------------------------
n, m, s = map(int, input().split())
while n != 0 or m != 0 or s != 0:
    matriz, pos_ini, indicador = recebe_matriz(n, m)   
    print(resultado(matriz, pos_ini, indicador, n, m))
    n, m, s = map(int, input().split())
