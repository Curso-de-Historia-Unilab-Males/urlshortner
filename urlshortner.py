'''
Crie um encurtador de URL com Python
Author: Eric Brasil a partir do código de Ayushi Rawat
'''
# Importando o pacote
from pyshorteners import Shortener

# Definindo o link a ser encurtado
link = str(input('Insira o link a ser encurtado: '))

# Chamando o Shortener e aplicando na variável link
s = Shortener()
shorturl = (s.tinyurl.short(link))

# Imprimido o resultado na tela
print(f'URL encurtada: {shorturl}')
