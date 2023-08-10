#  faça um programa que mostre a tabuada de varios numeros, um de
# cada vez, para cada valor digiatdo pelo usuário. O programa será
# interrompido quando o numero solicitado for negativo.


# Nesse caso, ja vamos começar com um loop infinito

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    #Após a entrada vamos verificar se o numero é negativo
    if n < 0:
        break
    print('-' * 30)
    for c in range(1,11):
        mult = n * c
        print('{} x {} = {} '.format(n,c,mult))
    print('-' * 30)  
print('Prograna tabuada encerrado. Volte sempre!')
