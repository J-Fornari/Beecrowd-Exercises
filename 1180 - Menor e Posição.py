N = int(input())

X = list(map(int, input().split()))
menor_v = X[0]
posicao = 0

for i in range(1, N):
    if X[i] < menor_v:
        menor_v = X[i]
        posicao = i
print(f"Menor valor: {menor_v}")
print(f"Posicao: {posicao}")


'''

Exemplo de Entrada:
10
1 2 3 4 -5 6 7 8 9 10
Exemplo de Saída:
Menor valor: -5
Posicao: 4

'''