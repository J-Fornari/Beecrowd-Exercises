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

N = int(input())

for _ in range(N):
    expressao = input()
    pilha = []
    diamantes = 0

    for char in expressao:
        if char == '<':

            pilha.append('<')
        elif char == '>':

            if len(pilha) > 0:
                pilha.pop()    
                diamantes += 1  

    print(diamantes)


'''

Exemplo de Entrada:
2
<..><.<..>>
<<<..<......<<<<....>
Exemplo de Saída:
3
1

'''