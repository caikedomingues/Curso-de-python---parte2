# Melhore o desafio 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. programa encerra quando ele disser que quer mostrar
# os termos


primeiro = int(input('Primeiro termo: '))

razao = int(input('Razão da pa: '))

termo = primeiro

cont = 1

total = 0

mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
    
        print(termo)
        termo = termo + razao
        cont = cont + 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))