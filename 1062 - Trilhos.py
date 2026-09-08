def possivel(n, alvo):
    pilha = []
    proximo_vagao = 1

    for x in alvo:
        while (not pilha or pilha[-1] != x) and proximo_vagao <= n:
            pilha.append(proximo_vagao)
            proximo_vagao += 1

        if pilha and pilha[-1] == x:
            pilha.pop()
        else:
            return False

    return True


while True:
    n = int(input())
    if n == 0:
        break

    while True:
        linha = list(map(int, input().split()))
        if linha[0] == 0:
            break

        if possivel(n, linha):
            print("Yes")
        else:
            print("No")

    print()


'''

Exemplo de Entrada:
5
5 4 3 2 1
1 2 3 4 5
5 4 1 2 3
0
6
1 3 2 5 4 6
0
0
Exemplo de Saída:
Yes
Yes
No

Yes

'''