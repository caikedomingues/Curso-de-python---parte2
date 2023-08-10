# faça um programa que calcule a soma entre todos os impares que são
# multiplos de 3 e que se econtram no intervalo de 1 até 500
#Vamos adicionar a funcionalidade que faz o programa contar os valores
soma = 0
cont = 0

for c in range(1,501):
    
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
        cont = cont + 1
        print(c)
print('Quantidade de valores: {}'.format(cont))
print('Soma dos valores: {}'.format(soma))

    