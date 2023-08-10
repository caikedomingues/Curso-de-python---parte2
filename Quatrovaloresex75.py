# Desenvolva um programa que leia 4 valores pelo teclado e guarde -os
# em uma tupla. No final, mostre:

# quantas vezes apareceu o valor 9
# em que posição foi digitado o primeiro valor 3
# quais foram os numeros pares

num1 = int(input('Informe o 1° valor: '))
num2 = int(input('Informe o 2° valor: '))
num3 = int(input('Informe o 3° valor: '))
num4 = int(input('Informe o 4° valor: '))

numeros = (num1, num2, num3, num4)




print('Quants vezes apareceu o 9?: {}'.format(numeros.count(9)))
print('-------------------------------------------------------')
print('em que posição aparece o primeiro 3?: {}'.format(numeros.index(3)))



#Verificação de numeros pares


if num1 % 2 == 0:
    
  
    print('Valores par: {}'.format(num1))

elif num2 % 2 == 0:
    
   
    print('Valores par: {}'.format(num2))

elif num3 % 2 == 0:
    
   
    print('Valores par: {}'.format(num3))

elif num4 % 2 == 0:
    
   
    print('Valores par: {}'.format(num4))

else:
    
    print('Nenhum valor par foi digitado')
    
