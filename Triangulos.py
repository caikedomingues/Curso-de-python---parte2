# Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar

# que tipo de triângulo será formado:

#equilatero: todos os lados iguais

# isóceles: dois lados iguais

# escaleno: todos os lados diferentes

reta1 = float(input('Primeira reta: '))

reta2 = float(input('Segunda reta: '))

reta3 = float(input('Terceira reta: '))

triangulo = True

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    triangulo = True
    print("Pode formar um triângulo")

else:
    triangulo = False
    print('Não pode formar um triângulo')
    


if triangulo == True and reta1 == reta2 and reta1 == reta3:
    print('é um triângulo equiltero')

elif triangulo == True and reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print('é um tri^ngulo isóceles') 
    
elif triangulo == True and  reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
    print('É um triângulo escaleno')

