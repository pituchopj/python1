#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
altura=float(input('Digite sua altura em metros: '))
massa=float(input('Digite sua massa corporal em kilos: '))
imc=massa / altura ** 2
if imc > 18.5:
    print('Abaixo do peso')
elif 18.5 <=  imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')

