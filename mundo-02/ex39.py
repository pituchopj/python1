from datetime import date
nascimento=int(input('Digite o seu ano de nascimento: '))
hoje=date.today().year
idade = hoje - nascimento
if idade > 18:
    pergunta=input('Você já se alistou? ')
    print('Digite sim ou não:')
    if pergunta == ('sim' or 'Sim' or 'SIM'):
        print('Parabéns, você fez no tempo certo!')
    elif pergunta == ('não' or 'Não' or 'NÃO'):
        print('Você já deveria ter se alistado!')
    else:
        print('Comando errado!')
if idade == 18:
    print('Você tem que se alistar durante esse ano!')
if idade < 18:
    diferença= 18 - idade
    print(f'Faltam {diferença} anos para você poder se alistar')