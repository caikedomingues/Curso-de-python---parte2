# Desenvolva um programa que leia 6 numeros inteiros e mostre a soma
# apenas daqueles que forem pares e mostre a soma apenas daqueles que forem pares. Se o
# valor digitado for impar. desconsidere-o


soma = 0
cont = 0

for c in range(1,7):
    
    num = int(input('Informe um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
        
    elif cont == 0:
        soma = 'não há como somar sem valores pares'
        cont = 'Não há valores pares'
        
    elif cont == 1:
        soma = 'não há como somar apenas um valor '
    
                
print('Soma dos valores pares: {}'.format(soma))
print('Quantidade de valores pares: {}'.format(cont))