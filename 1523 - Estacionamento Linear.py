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
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    eventos = []
    for motorista in range(1, n + 1):
        c, s = map(int, input().split())
        eventos.append((c, 1, motorista))
        eventos.append((s, 0, motorista))

    eventos = sorted(eventos)

    estacionamento = Pilha()
    possivel = True

    for horario, tipo, motorista in eventos:
        if tipo == 1:
            estacionamento.push(motorista)
            if estacionamento.size() > k:
                possivel = False
        else:
            if estacionamento.peek() == motorista:
                estacionamento.pop()
            else:
                possivel = False

    if possivel:
        print("Sim")
    else:
        print("Nao")


'''

Exemplo de Entrada:
3 2
1 10
2 5
6 9
3 2
1 10
2 5
6 12
0 0
Exemplo de Saída:
Sim
Nao

'''