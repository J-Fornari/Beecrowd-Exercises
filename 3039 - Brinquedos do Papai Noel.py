N = int(input())

carrinhos = 0
bonecas = 0

for i in range(N):
    nome, sexo = input().split()

    if sexo == "M":
        carrinhos += 1
    else:
        bonecas += 1

print(carrinhos, "carrinhos")
print(bonecas, "bonecas")

'''

Exemplo de entrada:
5
Milena F
Joao M
Rafaela F
Renata F
Felipe M
Exemplo de saída:
2 carrinhos
3 bonecas

'''
