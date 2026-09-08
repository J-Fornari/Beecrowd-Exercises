
import sys
from collections import Counter

def main():
    dados = sys.stdin.read().split('\n')
    n = int(dados[0])
    for i in range(1, n + 1):
        linha = dados[i].lower()
        letras = [c for c in linha if c.isalpha()]
        contagem = Counter(letras)
        maior = max(contagem.values())
        resultado = sorted([c for c, v in contagem.items() if v == maior])
        print(''.join(resultado))

if __name__ == '__main__':
    main()


'''

Exemplo de Entrada:
3
Computers account for only 5% of the country's commercial electricity consumption.
Input
frequency letters
Exemplo de Saída:
co
inptu
e

'''