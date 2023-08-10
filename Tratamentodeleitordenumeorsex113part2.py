

def leiaFloat(msg):
    
    while True:
        
        try:
            
            n = float(input(msg))
        
        except (ValueError, TypeError):
            
            print('Valor inválido, por favor digite um numero real')
        
        except KeyboardInterrupt:
            
            print('O usuário interrompeu o programa durante a execução')
            break
        
        else:
            
            print('O valor informado foi {}'.format(n))
            print('Obrigado, volte sempre!')
            break


# programa principal

num2 = leiaFloat('Informe um valor real ou inteiro: ')