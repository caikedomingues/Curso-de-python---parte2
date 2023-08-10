# Reescreva a função leiaint() que fizemos no desafio 104, incluindo
# agora a possibilidade a possibilidade da digitação de um numero de tipo
# inválido. Aproveite e crie também uma função leiafloat com a mesma
# funcionalidade

def leiaInt(msg):
    
    while True:
        
        try:
            
            n = int(input(msg))
           
        except (ValueError, TypeError):
            
            print('Por favor digite um valor inteiro')
        
        except KeyboardInterrupt:
            
            print('O usuário encerrou o programa no meio da execução')
            break
        
        else:
            
            print('Você digitou o valor {}'.format(n))
            print('Obrigado, volte sempre')
            break
        
        

        
    
    
# Programa Principal

num = leiaInt('Digite um valor inteiro: ')
