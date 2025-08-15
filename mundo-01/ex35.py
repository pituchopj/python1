sal=float(input('Qual o valor do seu salário: '))
if sal <= 1250.00:
    reajuste=sal * 0.15
    sal_atual= reajuste + sal
    print(f'O seu salário é {sal}, após o reajuste, ele ficou {sal_atual}')
if sal > 1250.00:
    reajuste=sal * 0.1
    sal_atual=reajuste + sal
    print(f' O seu salário é {sal}, após o reajuste, ele ficou {sal_atual}')
