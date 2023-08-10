# Crie uma lista onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares
# e impares. No final, mostre os valores pares e impares em ordem
# crescente

numeros = [[], []]


for c in range(0,7):
    
    n = int(input('Informe o {}° valor: '.format(c + 1)))
    
    numeros.append(n)
    
    if n % 2 == 0:
        
        numeros[0].append(n)
        
    else:
        
        numeros[1].append(n)
    
numeros[0].sort()
numeros[1].sort()
print('Valores pares: {}'.format(numeros[0]))
print('Valores impares: {}'.format(numeros[1]))