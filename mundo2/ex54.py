from datetime import date
for ano in range(0,8):
    anoNascimento=int(input('Digite seu ano de nascimento: '))
    anoAtual= date.today().year
    idade = anoAtual - anoNascimento
    if idade >= 18:
        print('Você é maior de idade.')
    else:
        print('Você é menor de idade')
    