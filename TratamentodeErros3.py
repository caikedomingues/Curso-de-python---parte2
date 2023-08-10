# Outro ponto interessante é que posso usar quantos except eu quiser
# para poder tratar varios tipos de erros




try:
    
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/ b
    
# Posso mais de 1 erro em uma mesma exception 
except (ValueError, TypeError):
    # erro de valor e erro de tipo
   print('tivemos um problema com o tipo de dado que você digitou')

except ZeroDivisionError:
    
    # erro de divisão por 0
    print('Não é possivel dividir por zero')
    
except KeyboardInterrupt:
    
    print('O usuário preferiu não informar os dados')
    
except Exception as erro:
    
    print('O erro encontardo foi {}'.format(erro.__cause__))

else:
    
    # Aqui eu crio o bloco caso o try de certo
    
   print('O resultado é {:.1f}'.format(r))

finally:
    
    # Bloco que será executado independente do resultado
    print('Volte sempre! Muito obrigado')