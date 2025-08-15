import random
print('Vou pensar em um número de 0 a 5\n Tente adivinhar!')
n1=int(input('Digite um número de 0 a 5: '))
n_comp = random.choice([0, 1, 2, 3, 4, 5])
print('PROCESSANDO..')
if n1 == n_comp:
    print(f'Você ganhou! Eu pensei no número {n_comp} e você no {n1}')
else:
    print(f'Você perdeu! Eu pensei no número {n_comp} e você no {n1}')

