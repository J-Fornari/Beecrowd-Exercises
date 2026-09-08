import sys

for expressao in sys.stdin:
    expressao = expressao.strip()

    contador = 0
    correto = True

    for caractere in expressao:
        if caractere == "(":
            contador += 1

        elif caractere == ")":
            contador -= 1

            if contador < 0:
                correto = False
                break

    if correto and contador == 0:
        print("correct")
    else:
        print("incorrect")


'''

Exemplo de Entrada:
a+(b*c)-2-a 
(a+b*(2-c)-2+a)*2 
(a*b-(2+c) 
2*(3-a))  
)3+b*(2-c)( 
Exemplo de Saída:
correct
correct
incorrect
incorrect
incorrect

'''