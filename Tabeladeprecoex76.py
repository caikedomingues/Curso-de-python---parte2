# crie um programa que tenha uma tupla unica com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular

produtos = ('Lápis', 'borracha', 'bolacha', 'pulseira', 'canetas', 'caderno', 'hamburguer', 'batata')
print('Tamanho da lista de produtos: {}'.format(len(produtos)))

preco = (1.00, 2.00, 3.50, 4.50, 10.00, 20.00, 3.50, 2.20 )
print('Tamanho da lista de preços: {}'.format(len(preco)))


print('-----------------------------------------')
print('Listagem de preços')
print('-----------------------------------------')
print('{}...................................{}'.format(produtos[0], preco[0]))
print('{}...................................{}'.format(produtos[1], preco[1]))
print('{}...................................{}'.format(produtos[2], preco[2]))
print('{}...................................{}'.format(produtos[3], preco[3]))
print('{}...................................{}'.format(produtos[4], preco[4]))
print('{}...................................{}'.format(produtos[5], preco[5]))
print('{}...................................{}'.format(produtos[6], preco[6]))
print('{}...................................{}'.format(produtos[7], preco[7]))
