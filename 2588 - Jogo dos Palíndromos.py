palavra = input()
contagem = {}
impar = 0
for letra in palavra:
    if letra in contagem:
        contagem[letra] = contagem[letra] + 1
    else:
        contagem[letra] = 1
for valor in contagem.values():
    if valor % 2 == 1:
        impar += 1
print(impar)

'''

Exemplo de Entrada:
batata
aabb
abc
Exemplo de Saída:
1
0
2

'''