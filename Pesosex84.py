# Faça um programa que leia o nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves.

# primeiro, vamos criar uma lista temporária e uma lista principal

temp = []
princ = []

maior = 0 # Ira guardar o maior peso
menor = 0 # ira guardar o menor peso


# Agora precisamos criar um loop infinito e dentro dele adicionar os 
# valores dentro da lsita temporária

while True:
    
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
   
    #Verificação de pesos
    # se o tamanho da lista for igual a 0, ou seja se a lista estiver
    # vazia, maior e menor recebe temp[1], o peso da pessoa que possui
    # o maior e o menor peso
    
    if len(princ) == 0:
        
        maior = temp[1]
        menor = temp[1]
        
    else:
        
        if temp[1] > maior:
            
            maior = temp[1]
        
        if temp[1] < menor:
            
            menor = temp[1]
        
        
    
    #Será necessário jogar a lista temp dentro de princ como uma cópia
    princ.append(temp[:])
    
     #O clear serve para apagar os valores copiados da lista
    temp.clear()
  
    
    resp = str(input('Você quer continuar? s/n: '))
    
    if resp in'Nn':
        
        break


# Vamos imprimir pro usuário a quantidade de pessoas cadastradas, usando
# o len que é o metodo que retorna o tamanho da lista

print('Ao todo você cadastradou {} pessoas'.format(len(princ)))

# Impressão dos resultados dos pesos

print('O maior peso foi de {}'.format(maior))
print('O menor peso foi de {}'.format(menor))

#Por ultimo precisamos criar a lista que contem as pessoas mais pesadas
# e as mais leves, para isso devemos criar um laço que verifique os 
# os valores que são iguais (tanto os maiores quanto os menores).

for p in princ:
    
    if p[1] == maior:
        
        print('Dono(a) do maior peso: {}'.format(p[0])) 
        
    elif p[1] == menor:
        
        print('Dono(a) do menor peso: {}'.format(p[0]))






    
    


