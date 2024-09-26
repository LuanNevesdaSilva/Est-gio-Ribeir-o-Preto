Fibonacci = [0, 1]
x = 0
y = 1

verif = int(input('Insira o número: '))

while True:
    soma = x + y
    x = y
    y = soma
    Fibonacci.append(soma)
    
    if Fibonacci[-1] >= verif:
        break

if verif in Fibonacci:
    print('existe')
else:
    print('não existe')