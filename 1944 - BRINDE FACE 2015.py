class Pilha:
    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        return self.elementos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Pilha está vazia!")
        return self.elementos[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.elementos)

while True:
    try:
        n = int(input())
    except EOFError:
        break

    painel = Pilha()
    painel.push("FACE")
    brindes = 0

    for _ in range(n):
        letras = input().split()      # lê as 4 letras separadas por espaço, ex: ['E','C','F','A']
        bloco = "".join(letras)       # junta numa string só: "ECFA"

        reverso = bloco[::-1]

        if reverso == painel.peek():
            painel.pop()
            brindes += 1
            if painel.is_empty():
                painel.push("FACE")
        else:
            painel.push(bloco)

    print(brindes)


'''

Exemplos de Entrada:
4
E C F A
A C E F
F E C A
A F C E
Exemplos de Saída:
2

'''