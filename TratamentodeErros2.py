# Também podemos tratar os erros de uma maneira mais avançada, utilizando
# exceptions que apontam erros especificos atribuindo a exception em ua
# variável. 



try:
    
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/ b
    
except Exception as erro:
    # Agora ao errarmos o tipo do valor, iremos conseguir informar o usuário 
    # de maneira 'personalizada'
    print('O problema encontrado foi {}'.format(erro.__class__))

else:
    
    # Aqui eu crio o bloco caso o try de certo
    
   print('O resultado é {:.1f}'.format(r))

finally:
    
    # Bloco que será executado independente do resultado
    print('Volte sempre! Muito obrigado')