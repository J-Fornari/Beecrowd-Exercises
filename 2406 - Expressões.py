import sys

def eh_bem_definida(s: str) -> bool:
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for c in s:
        if c in '([{':
            pilha.append(c)
        else:
            if not pilha or pilha[-1] != pares[c]:
                return False
            pilha.pop()
    
    return len(pilha) == 0


def main():
    dados = sys.stdin.read().split('\n')
    t = int(dados[0])
    resultados = []
    
    for i in range(1, t + 1):
        cadeia = dados[i]
        resultados.append('S' if eh_bem_definida(cadeia) else 'N')
    
    print('\n'.join(resultados))


if __name__ == '__main__':
    main()



'''

Exemplo de Entrada:
12
()
[]
{}
(]
}{
([{}])
{}()[]
()]
{[]
(
(([{}{}()[]])(){}){}
(((((((((({([])}])))))))))
Exemplo de Saída:
S
S
S
N
N
S
S
N
N
N
S
N

'''