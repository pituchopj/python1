km=int(input('Digite a distância de sua viagem: '))
if km <= 200:
    preço_km=0.50
    valor_total= km * preço_km
    print(f'Sua viagem é de {km}km e custa o valor de R${valor_total}')
else:
    preço_km=0.45
    valor_total=km * preço_km
    print(f'Sua viagem é de {km}km e custará o valor de R${valor_total}')
print('--FIM--')