sal=int(input('Digite seu salário atual:'))
if sal < 1250.00:
    aumento=sal * 0.1
    sal_aumentado=aumento + sal
    print(f'Seu salário era de {sal}, mas você recebeu um aumento!\n Parabéns!! \n Agora seu salário é de {sal_aumentado}')
else:
    aumento=sal * 0.12
    sal_aumentado=aumento + sal
    print(f'Seu salário era de {sal}, mas você recebeu um aumento \n Parabéns \n Agora seu salário é de {sal_aumentado}')
print('--FIM-- ') 