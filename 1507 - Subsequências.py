
import sys

def is_subsequence(r, s):
    it = iter(s)
    return all(c in it for c in r)

def main():
    dados = sys.stdin.read().split()
    idx = 0
    n = int(dados[idx]); idx += 1
    saida = []
    for _ in range(n):
        s = dados[idx]; idx += 1
        q = int(dados[idx]); idx += 1
        for _ in range(q):
            r = dados[idx]; idx += 1
            saida.append("Yes" if is_subsequence(r, s) else "No")
    print('\n'.join(saida))

if __name__ == '__main__':
    main()

'''

Exemplo de Entrada:
1
aabccbba
2
abc
abbc
Exemplo de Saída:
Yes
No

'''