frase = input()

vogal = "aeiou"
vogais_encontradas = ""

for caractere in frase:
    if caractere in vogal:
        vogais_encontradas = vogais_encontradas + caractere
        
invertida = vogais_encontradas[::-1]

if vogais_encontradas == invertida:
    print("S")
else:
    print("N")



'''

Exemplos de Entrada:
hahaha
riajkjdhhihhjak
a
huaauhahhuahau
Exemplos de Saída:
S
N
S
S

'''