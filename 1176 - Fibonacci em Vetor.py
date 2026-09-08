T = int(input())

fib = [0, 1]

for i in range(2, 61):
    fib.append(fib[i - 1] + fib[i - 2])

for i in range(T):
    N = int(input())
    print(f"Fib({N}) = {fib[N]}")


'''

Exemplo de Entrada:
3
0
4
2
Exemplo de Saída
Fib(0) = 0
Fib(4) = 3
Fib(2) = 1

'''