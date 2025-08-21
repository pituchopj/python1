nota1=float(input('Digite sua nota: '))
nota2=float(input('Digite sua segunda nota: '))
media= (nota1 + nota2) / 2
print(f'Sua média é {media}')
if media >= 7:
    print('Você passou!')
elif 6<= media <=6.9:
    print('Você está de recuperação')
elif media < 6:
    print('Você foi reprovado')
