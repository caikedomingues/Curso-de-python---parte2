
# façã um programa que leia um numero inteiro e diga se ele é ou não
# ou não um numero primo

num = int(input('Informe um valor: '))
print('A cor azul indica os valores divisiveis')

tot = 0

for c in range(1, num + 1):
    
    if num % c == 0:
    
     print('\033[34m {}'.format(c))
     tot = tot + 1
    else:
        print(' \033[31m{}'.format(c))
    
if tot == 2:
    print('O valor {} é primo'.format(num))
else:
    print('O valor {} não é primo'.format(num))