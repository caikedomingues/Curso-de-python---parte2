
# Refaça o desafio 51, lendo o primeiro termo e a razão de uma pa
# mostrando os 10 primeiros termos da progressão usando a estrutura 
# while

primeiro = int(input('Primeiro termo: '))

razao = int(input('Razão da pa: '))

termo = primeiro

cont = 1

while cont <= 10:
    
    print(termo)
    termo = termo + razao
    cont = cont + 1
print('fim')