import sys

dados = sys.stdin.read().split()
i = 0

n = int(dados[i])
i += 1

principal = []
minimos = []
saida = []

for _ in range(n):
    comando = dados[i]
    i += 1

    if comando == 'PUSH':
        v = int(dados[i])
        i += 1
        principal.append(v)

        if not minimos:
            minimos.append(v)
        else:
            if v < minimos[-1]:
                minimos.append(v)
            else:
                minimos.append(minimos[-1])

    elif comando == 'POP':
        if not principal:
            saida.append("EMPTY")
        else:
            principal.pop()
            minimos.pop()
    else:  # comando == 'MIN'
        if not principal:
            saida.append("EMPTY")
        else:
            saida.append(str(minimos[-1]))

print("\n".join(saida))


'''

Exemplo de Entrada:
11
PUSH 5
PUSH 7
PUSH 3
PUSH 8
PUSH 10
MIN
POP
POP
MIN
POP
MIN
Exemplo de Saída:
3
3
5

'''