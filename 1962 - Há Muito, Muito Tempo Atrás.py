quantidade = int(input())

for i in range(quantidade):
    T = int(input())

    if T >= 2015:
        print(f"{T - 2014} A.C.")
    else:
        print(f"{2015 - T} D.C.")
        
'''
Após 2015 fica A.C. (Antes de Cristo), e antes de 2015, fica D.C. (Depois de Cristo).

'''
        