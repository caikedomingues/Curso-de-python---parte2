# método sorted: serve para ordenar os dados em ordem alfabética, vale
# lembrar que o sorted não modifica ou altera a sua tupla

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

print(sorted(lanche))

# Também podemos unir duas tuplas por exemplo:
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)

# é possivel usar o len parar medir a tupla c que uniu os elementos de a
# e b

print('Tamanho de c: {}'.format(len(c)))

# é possivel utilizar o count para contar um determinado elemento
print('Quantidade de 5 na tupla: {}'.format(c.count(5)))

# O index retorna a posição inicial do elemento
print('Posição inicial do 8: {}'.format(c.index(8)))

# a gente pode apagar uma tupla da memória com o del: ex: del(lanche)