precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

n = int(input())
for _ in range(n):
    expressao = input()
    pilha = []
    saida = ""

    for c in expressao:
        if c.isalpha() or c.isdigit():
            saida += c
        elif c == '(':
            pilha.append(c)
        elif c == ')':
            while pilha[-1] != '(':
                saida += pilha.pop()
            pilha.pop()
        else:  # é um operador: +, -, *, /, ^
            while pilha and pilha[-1] != '(' and precedencia[pilha[-1]] >= precedencia[c]:
                saida += pilha.pop()
            pilha.append(c)

    while pilha:
        saida += pilha.pop()

    print(saida)


'''

Exemplo de Entrada:
3
A*2
(A*2+c-d)/2
(2*4/a^b)/(2*c)
Exemplo de Saída:
A2*
A2*c+d-2/
24*ab^/2c*/

'''