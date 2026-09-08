N = []

for i in range(20):
    numero = int(input())
    N.append(numero)

for i in range(10):
    N[i], N[19 - i] = N[19 - i], N[i]

for i in range(20):
    print(f"N[{i}] = {N[i]}")
    
'''

Exemplo de Entrada:
0
-5
...
63
230
Exemplo de Saída:
N[0] = 230
N[1] = 63
...
N[18] = -5
N[19] = 0

'''
