salarioMin=float(input('Digite o salário minimo: '))
salarioFIxo=salarioMin * 2
carrosVendidos=int(input('Digite quantos carros você vendeu: '))
valorCarro=float(input('Qual o valor do carro? '))
comissão=carrosVendidos * 50
if carrosVendidos > 10:
    comissãoVar=(valorCarro*carrosVendidos) * 0.05
    salTotal=comissãoVar + comissão + salarioFIxo
    print(f'O seu salário é {salTotal}.')
else:
    salTotal=comissão + salarioFIxo
    print(f'Seu salário é {salTotal}')