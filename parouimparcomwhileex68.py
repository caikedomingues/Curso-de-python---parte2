# Faça um programa que jogue par ou impar com o computador. O jogo
# só será interrompido quando o jogador perder, mostrando o total
# de  vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

soma = 0
ganhou = True
perdeu = False
vitoria = 0
derrota = 0

computador = randint(0, 101)

jogador = int(input('Escolha 1 para impar e 2 para par: '))

if jogador == 1:
    
    jogador = int(input('Informe um numero '))
    
    soma =  jogador + computador
    
    if soma % 2 != 0:
        
        print('Você ganhou: {} é impar'.format(soma))
        ganhou = True
        perdeu = False
        vitoria = vitoria + 1
    else:
        
        print('Você perdeu: {} é par'.format(soma))
        ganhou = False
        perdeu = True
        derrota = derrota + 1

elif jogador == 2: 
    
   jogador = int(input('Informe um numero: '))
   
   soma = jogador + computador
   
   if soma % 2 == 0:
       
       print('Você ganhou: {} é par'.format(soma))
       ganhou = True
       perdeu = False
       vitoria = vitoria + 1

   else: 
       print('você perdeu: {} é impar'.format(soma))
       ganhou = False
       perdeu = True
       derrota = derrota + 1


while ganhou == True:
    
  computador = randint(0, 100)
  
  jogador = int(input('Escolha 1 para impar e 2 para par '))

  if jogador == 1:
        
        jogador = int(input('Informe um numero '))
        
        soma =  jogador + computador
        
        if soma % 2 != 0:
            
            print('Você ganhou: {} é impar '.format(soma))
            ganhou = True
            perdeu = False
            vitoria = vitoria + 1
        else:
            
            print('Você perdeu: {} é par'.format(soma))
            ganhou = False
            perdeu = True
            derrota = derrota + 1

  elif jogador == 2: 
    
            jogador = int(input('Informe um numero: '))
            
            soma = jogador + computador
            
            if soma % 2 == 0:
                
                print('Você ganhou: {} é par'.format(soma))
                ganhou = True
                perdeu = False
                vitoria = vitoria + 1

            else: 
                print('você perdeu: {} é impar'.format(soma))
                ganhou = False
                perdeu = True
                derrota = derrota + 1

print('Quantidade de vitórias: {}'.format(vitoria))
print('Quantidade de derrotas: {}'.format(derrota))
    
    
            
    
