# crie um programa que tenha como função chamada voto() que vai receber
# como parametro o ano de nascimento de uma pessoa, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL,
# ou OBRIGATÓRIO nas eleições


from datetime import date


def voto(ano):
    
    idade = date.today().year - ano
    mensagem = ' '
    
    if idade < 16:
        
        mensagem = 'Você não pode votar'
        print('Idade do usuário: {}'.format(idade))
        return mensagem
    
    elif idade == 16 or idade < 18:
        
        mensagem = 'O seu voto é opcional'
        print('Idade do usuário: {}'.format(idade))
        return mensagem
    
    elif idade >= 18 and idade < 70:
        
        mensagem = 'O seu voto é obrigatório'
        print('Idade do usuário: {}'.format(idade))
        return mensagem
    
    elif idade > 70: 
        
        mensagem = 'O seu voto é opcional'
        print('Idade do usuário: {}'.format(idade))
        return mensagem        




#Programa principal
nome = str(input('Qual o seu nome: '))
nasc = int(input('Em que ano você nasceu: '))
print('Status da solicitação de {}: {}'.format(nome, voto(nasc)))
