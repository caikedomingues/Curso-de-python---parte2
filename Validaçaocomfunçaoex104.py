# Crie um programa que tenha a função leiaInt(), que vai funcionar de
# forma semelhante a função input() do python, só que fazendo a validação
#  para aceitar apenas um valor numérico
# ex: n = leiaInt('Digite um n')

# Primeiro vamos criar a função leiaInt() que recebera como parametro
# uma mensagem

def leiaInt(msg):
    # criação de duas variaveis uma inteira e outra booleana
    ok = False
    valor = 0
    
    # após a criação da variável devemos criar um laço infinito
    while True:
        # Aqui dentro vamos atribuir a variável n input de strings que
        # recebera como parametro a variavel msg
        
        # Depois da atribuição vamos verificar se o valor é um numero
        
        n = str(input(msg))
        
        # Se o valor for um numero, a variável valor ira receber o valor
        # inteiro de n e ok passara a ser verdadeiro, caso contrário,
        # a mensagem de erro será apresentada e o  loop começara outra
        # vez
        if n.isnumeric():
            
            valor = int(n)
            ok = True
        
        else:
            
            print('ERRO! digite um numero inteiro válido')
        
        if ok:
           break
    return valor
# programa principal

n = leiaInt('Digite um numero: ')
print('Você acabou de digitar o numero {}'.format(n))
        
    