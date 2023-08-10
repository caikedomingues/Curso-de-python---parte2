# crie um programa que vai gerar 5 numeros aleatórios e colocar uma tupla
# Depois disso, mostre a listagem de numeros gerados e também indique
# o menor e o maior valor que estão na tupla.

from random import randint
 
 
numeros = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print('Valores: {}'.format(numeros))
print('Maior valor gerado: {}'.format(max(numeros)))
print('Menor valor gerado: {}'.format(min(numeros)))
