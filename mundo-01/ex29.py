v=int(input('Digite a velocidade do seu carro: '))
alta_v=v-80
multa=alta_v * 7
if v <=80:
    print('Você está na velocidade ideal ! Pode seguir.')
else:
    print('Você irá ser multado por alta velocidade.')
if alta_v >= 1:
    print(f'O valor da multa será de {multa} R$')