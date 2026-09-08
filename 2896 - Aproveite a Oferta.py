T = int(input())

for i in range(T):
        n, k = map(int, input().split())
        resultado = (n // k) + (n % k)
        print(resultado)
        
'''
Exemplo de Entrada:
3
7 4
4 7
4000 7
Exemplo de Saída:
4
4
574
'''
