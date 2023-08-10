# Faça um programa que tenha uma lista chamada numeros e duas funçoes
# chamadas sorteia() e somapar(). A primeira função vai sortear 5 numeros
# e vai coloca-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os pares sorteados pela função anterior.


from random import randint
from time import sleep


numeros = list()
num = 0


def sorteia():
    
    for c in range(0,5):
        
        num = randint(0,100)
        
        numeros.append(num)
    
    print(numeros)


    
def somaPar():
    
    soma = 0
    
    for valor in numeros:
        
        if valor % 2 == 0:
            
            soma = soma + valor
            
    print('Soma dos valores pares: {}'.format(soma))
        

# Programa principal

sorteia()
somaPar()
