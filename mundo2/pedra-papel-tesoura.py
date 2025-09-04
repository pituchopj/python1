import random
print('Vamos começar o jogo?')
print('Escolha pedra, papel ou tesoura para começarmos o jokenpô')
opçoes=input('Escolha pedra,papel ou tesoura: ')
escolhas=['pedra', 'papel', 'tesoura']
opçoesComp=random.choice(escolhas)
if opçoes not in escolhas:
    print('Digite novamente')
if opçoes == 'pedra' and opçoesComp == 'papel' or opçoes == 'pedra' and opçoesComp == 'tesoura' or opçoes == 'tesoura' and opçoesComp == 'papel':
    print('Parabéns, você ganhou!')
elif opçoes == 'papel' and opçoesComp == 'pedra' or opçoes == 'tesoura' and opçoesComp == 'pedra' or opçoes == 'papel' and opçoesComp == 'tesoura':
    print('Você perdeu!!')
elif opçoes == opçoesComp:
    print('EMPATAMOS')

