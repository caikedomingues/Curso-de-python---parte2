# crie um programa que leia o nome e o preço de vários produtos. O 
# programa deverá perguntar se o usuário vai continuar. No fianl, mostre:
# qual é o total gasto na compra
# quantos produtos custam mais de 1000
# qual é o nome do produto mais barato.

# Vamos começar iniciando um laço infinito

total = 0
totmil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    total = total + preco
    cont = cont + 1
    if preco > 1000:
        
        totmil = totmil + 1
    if cont == 1:
        
        menor = preco
    else:
        if preco < menor:
            
            menor = preco
            barato = produto
        
    
    resp = ' '
    while resp not in 'SN':
        
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('Total de compras: {:.2f} R$'.format(total))
print('Temos {} produtos custando mais de 1000 reais'.format(totmil))
print( 'O produto mais barato foi {} que custa {}'.format(barato,menor))


