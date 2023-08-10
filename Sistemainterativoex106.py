# Faça um mini sistema que utilize o interactive help do python. O usuário

# vai digitar o comando e o manual vai aparecer. Quando o usuário digitar

# a palavra fim  o programa se encerrara

from time import sleep
#Lista de cores
c = ('\033[n' # sem cores #Lista de cores
      '\033[0;30;41m', # 1 - vermelho 
      '\033 [0;30;42m', # 2 - verde
      '\033 [0;30;43m', # 3 - amarelo
      '\033 [0;30;44m', # 4 - azul
      '\033 [0,30,45m', # 5 - roxo
      '\033 [7;30m' # 6 - branco
     ) 
def ajuda(com):
    titulo('Acessando o manual do comando  {}'.format(com))
    help(com)

def titulo(msg, cor = 0):

    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print('  {}'.format(msg))
    print('~' * tam)
    print(c[0], end='')



while True:
    titulo('Sistema de comando PyHELP', 2)
    comandos = str(input('Qual função você quer buscar? '))
    help(comandos)
    print('--------------------------------------------')
    
    if comandos.upper() == 'FIM':
        
        print('Programa encerrado')
        break
    else:
        
        ajuda(comandos)
        
titulo('Até logo', 1)