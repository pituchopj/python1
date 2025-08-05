limite=80
v=int(input('Qual a velocidade atual de seu carro?'))
if v>limite:
    excesso=v-80
    multa=7
    custo_total=excesso * multa
    print('Cuidado, você está muito rápido!\n Infelizmente você foi MULTADO!')
    print(f'Você ultrapssou em {excesso} km/h, o valor que irá ser pago será de {custo_total}')
else:
    print('Parabéns, você está dentro das normas!')
print('--FIM--')
