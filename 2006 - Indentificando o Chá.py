T = int(input())

respostas = list(map(int, input().split()))

corretas = 0

for resposta in respostas:
    if resposta == T:
        corretas += 1

print(corretas)


'''
Exemplo de entrada:
5
1 2 3 4 5
Exemplo de saída:
1

'''
