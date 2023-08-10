
# Crie um código em python que teste se o site pudim está acessivel pelp
# computador usado.

# Antes de tudo, é necessário importar a biblioteca urllib.request
import urllib.request

try:
    # Temos agora que usar o método que vai verificar a disponibilidade
    # do site
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    
    print('Deu erro')

else:
    
    print('Tudo ok')
    print(site.read())# Esse metodo da acesso a todo o html do site