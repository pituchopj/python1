print('PROGRAMA DE VERIFICAÇÃO:')
def palindromo(texto):
    texto=texto.lower().replace(' ', '')
    return texto == texto [:: -1]
palavrasTeste=input('Digite uma palavra, texto ou número: ')
if palindromo(palavrasTeste):
    print('É palindromo')
else:
    print('Não é palindromo')
