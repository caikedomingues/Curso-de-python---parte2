# crie um programa que leia varios numeros inteiros pelo teclado. O
# programa só vai parar quando o usuário digitar o valor 999, que é
# a condição de parada. No final, mostre quantos numeros foram digitados
# e qual foi a soma entre eles (desconsiderando o flag) 


# Nesse caso temos que iniciar fora do laço e finalizar dentro dele
# Assim, ele não conta ou manipula o ultimo valor informado, sendo
# assim, ele ira paenas verificar se o valor limite foi alcançado
# e encerrara o programa

numero = int(input('Digite um numero [999 para parar] '))

soma = 0

cont = 0

while numero != 999:
    
    soma = soma + numero 
    cont = cont + 1
    numero = int(input('Digite um numero [999 para parar] '))
   

print('Você digitou {} numeros e a soma entre eles foi {}'.format(cont,soma))

