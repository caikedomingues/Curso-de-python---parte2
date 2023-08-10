

# Vamos iniciar os estudos sobre tratamentos de erros

# try: tera o bloco que será supervisionado 

# except: tera o bloco que tratara o erro





try:
    
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/ b
except:
    # Agora ao errarmos o tipo do valor, iremos conseguir informar o usuário 
    # de maneira 'personalizada'
    print('Infelizmente tivemos um problema...')

else:
    
    # Aqui eu crio o bloco caso o try de certo
    
   print('O resultado é {:.1f}'.format(r))

finally:
    
    # Bloco que será executado independente do resultado
    print('Volte sempre! Muito obrigado')