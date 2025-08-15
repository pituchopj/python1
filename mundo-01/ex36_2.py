from colorama import Back, Style, Fore, init
init(autoreset=True)
print('Iremos confirmar seu financiamento...')
print('Passe as seguintes informações para confirmamos.')
valor=int(input('Valor da casa: '))
sal=int(input('Seu salário: '))
anos=int(input('Em quantos anos você deseja pagar?'))
prestacao= valor / (anos*12)
limite= sal * 0.3
if prestacao < limite:
    print(f'O valor da casa é {valor} em {anos} anos, gera uma prestação mensal de {prestacao}')
    print(Fore.BLUE+'\nSeu empréstimo foi aprovado! ')
else:
    print(f'O valor da casa é {valor} em {anos} anos, gera uma prestação mensal de {prestacao}')
    print(Fore.RED + '\n Seu empréstimo foi NEGADO!')
