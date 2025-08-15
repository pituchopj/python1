distancia_km=int(input('Digite a distância em km da sua viagem: '))
distancia_p=distancia_km * 0.50
distancia_g=distancia_km * 0.45
if distancia_km <= 200:
    print(f'A sua viagem será de {distancia_km} e o valor será de {distancia_p}')
if distancia_km > 200:
    print(f'A sua viagem será de {distancia_km} e o valor será de {distancia_g}')