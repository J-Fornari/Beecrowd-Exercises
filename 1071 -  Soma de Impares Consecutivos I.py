x = int(input())
y = int(input())

menor = min(x, y)
maior = max(x, y)

soma = 0

for numero in range(menor + 1, maior):
    if numero % 2 != 0:
        soma += numero

print(soma)