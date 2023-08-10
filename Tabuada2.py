# Refaça o desafio 9, mostrando a tabuada de um numero que o usuario

# escolher, só que utilizando um laço for

numero = int(input('Informe um numero: '))

for c in range(1,11):
    
    print('{} x {} = {} '.format(numero,c,numero*c))
