
tempo_carro=int(input('Quantos dias você ficou com o carro:'))
qt_km=float(input('Qual a quantidade de km rodados no carro?'))
valor=(tempo_carro*60) + (qt_km *0.15)
print('De acordo com o tempo e a kilometragem, o valor a ser pago será de {}'.format (valor))