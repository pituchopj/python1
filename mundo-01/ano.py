ano=int(input('Digite o ano: '))
if ano % 4 ==0 and ano % 100!=0 and ano % 400 == 0:
    print('Esse ano é bissexto.')
else:
    print('Não é bissexto')