
#Vale lembrar que tuplas são imutaveis
#tipos de tuplas
# (): tupla
# []: lista 
# {}: dicionários
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'batata frita')
print(lanche)
print(lanche[1])

#Vamos percorrer uma tupla com um for

for comida in lanche:
    print(comida)
    
#podemos conferir o tamanho da tupla

print("Tamanho da tupla: {}".format(len(lanche)))

#podemos percorrer a tupla usando o for de uma outra maneira

for cont in range(0,len(lanche)):
   print('Outra maneira de imprimir: {}'.format(lanche[cont]))
   

#podemos usar o enumerate para numerar ou dar posição aos elementos da 
# tupla

for pos, comida in enumerate(lanche):
    
    print('Eu vou comer {} na posição {}'.format(comida, pos))

   