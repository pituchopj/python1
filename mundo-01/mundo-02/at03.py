num=int(input('Digite um número :'))
if num > 9999:
    print('ERRO!!')
else:
    mil=num // 1000
    cen=(num%1000) // 100
    dez=((num % 1000)( num % 100)) // 10
    uni=((num % 1000)(num % 100)(num %10))
    soma=mil+cen+dez+uni
    print(f' O número informado é {num}\n')
    print(f'A soma dos números é {soma} ')