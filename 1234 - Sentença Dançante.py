
import sys

for frase in sys.stdin:
    frase = frase.rstrip("\n")

    maiuscula = True
    resultado = ""

    for caractere in frase:

        if caractere == " ":
            resultado += " "

        elif maiuscula:
            resultado += caractere.upper()
            maiuscula = False

        else:
            resultado += caractere.lower()
            maiuscula = True

    print(resultado)

'''
Exemplo de Entrada:
This is a dancing sentence
  This   is         a  dancing   sentence  
aaaaaaaaaaa
z
Exemplo de Saída:
ThIs Is A dAnCiNg SeNtEnCe
  ThIs   Is         A  dAnCiNg   SeNtEnCe  
AaAaAaAaAaA
Z
'''