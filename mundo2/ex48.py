print('A soma dos múltiplos de 3 é: ')
soma=0
for somaMultiplos in range(3,501):
    if somaMultiplos % 3 ==0:
        print(somaMultiplos)
        soma= soma + somaMultiplos
print(f'A soma dos números é igual a {soma}')
    