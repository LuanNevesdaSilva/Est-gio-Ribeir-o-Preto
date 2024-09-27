cont = 0
var = input('insira a String: ')


for i in var:
    if 'a' == i or 'A' == i:
        cont += 1
    
print(f'existe {cont} A nesta string')
