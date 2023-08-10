# Crie um programa onde o usuário possa digitar vários numeros e
# cadastre -os em uma lista. Caso o numero já exista lá dentro 
# ele não será adicionado. No final serão exibidos todos os valores 
# unicos digitados, em ordem crescente.

numeros = []

while True:
    
    n = int(input('Digite um valor: '))
    
    if n not in numeros:
        
        numeros.append(n)
        print('Valor {} adicionado'.format(n))
    else:
        print('Valor duplicado, não vou adicionar')
    r = str(input('Quer continuar? [s/n] '))
    
    if r in 'Nn':
        
        break
    
numeros.sort()
print('Valores informados: {}'.format(numeros))
     