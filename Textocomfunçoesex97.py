# Faça um programa que tenha uma função chamada escreva(), que receba  um
# texto qualquer como parametro e mostre uma mensagem com tamanho
# adaptavel 

def escreva(texto):
    
   print('-' * len(texto))
   print(texto)
   print('-' * len(texto))


frase = str(input('Digite uma palavra ou uma frase: '))

escreva(frase)