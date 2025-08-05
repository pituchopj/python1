import random 
num_pc=random.randint(0,5)
print('O jogo de adivinha começou!\n Escolha um número de 0 a 5 para tentar acertar.')
num_user=int(input('Escolha um número de 0 a 5: '))
if num_pc==num_user:
    print('Parabéns, você acertou!')
else:
    print('Oops, você errou!\n Tente novamente... ')
print('--FIM--')