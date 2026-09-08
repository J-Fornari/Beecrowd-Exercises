N = int(input())

for i in range(N):
    A, B = input().split()

    resultado = ""

    menor = min(len(A), len(B))

    for j in range(menor):
        resultado += A[j]
        resultado += B[j]

    resultado += A[menor:]
    resultado += B[menor:]

    print(resultado)


'''

Exemplo de Entrada:
2
Tpo oCder
aa bb
Exemplo de Saída:
TopCoder
abab

'''