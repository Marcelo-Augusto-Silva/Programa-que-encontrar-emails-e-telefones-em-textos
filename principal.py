import re


def email(txt):
    email = re.compile('([a-zA-Z0-9._%+-]+)'   # Nome do usuario
                        '(@[a-zA-Z0-9]+)'    # dominio
                        '(\.[a-zA-Z]{2,4})') # depois do .com

    procurar = email.findall(txt)
    return procurar

def numero(num):
    numero_celular = re.compile('(\(\d{2}\)|\d{2})?'  # Encontrar o DDD do telefone
                                '( ?\d{5})'  # encontrar os cincos primeiros numeros
                                '(\s|-|\.)?'  # ve se ele separa com um - espaco ou um ponto
                                '(\d{4})') # encontrar os 4 ultimos numeros

    procurar = numero_celular.findall(num)
    return procurar


texto = str(input('Cole o texto para encontrar emails e telefones '))

numeros = []
emails = []
try:
    numeros.append(numero(texto))
    if numeros[0][0] == None:
        print('erro')
    for c in numeros:
        print('Encontrei os seguintes numeros ')
        for n in range(0,len(c)):
            print(''.join(numeros[0][n]))
except:
    print('Não encontrei nenhum numero telefonico')

try:
    emails.append(email(texto))
    if emails[0][0] == None:
        print('erro')
    for c in emails:
        print('Encontrei os seguintes emails')
        for n in range(0,len(c)):
            print(''.join(emails[0][n]))

except:
    print('Não encontrei nenhum email')