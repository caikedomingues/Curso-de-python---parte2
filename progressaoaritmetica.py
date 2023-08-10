# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão

primeiro = int(input('Informe  um valor: '))

razao = int(input('Razão: '))

#Fórmula para descobrir o decimo valor de uma pa

decimo = primeiro + (10-1) * razao

for p in range(primeiro, decimo + razao, razao):
    
    print(p)
    
    