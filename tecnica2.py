cont = 0
teste = input('insira a String: ')


for i in teste:
    if 'a' == i or 'A' == i:
        cont += 1
    
print(f'existe {cont} A nesta string')