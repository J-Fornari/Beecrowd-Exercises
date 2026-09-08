N = int(input())

for i in range(N):
    texto = input()

    meio = len(texto) // 2

    primeira = texto[:meio]
    segunda = texto[meio:]

    resultado = primeira[::-1] + segunda[::-1]

    print(resultado)
'''

Exemplo de entrada:
4
abcdef
ghijkl
mnopqr
stuvwx
Exemplo de saída:
fedcba
lkjihg
rqponm
xwvuts

'''
