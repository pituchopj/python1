nomes = []
idades = []
sexos = []
for _ in range(5):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite M para masculino ou F para feminino: ').lower()
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
media = sum(idades) / len(idades)
idadeVelha = -1
nomeVelho = ''
fem20 = 0
for i in range(len(nomes)):
    if sexos[i] == 'm':
        if idades[i] > idadeVelha:
            idadeVelha = idades[i]
            nomeVelho = nomes[i]
    elif sexos[i] == 'f':
        if idades[i] > 20:
            fem20 += 1
print(f'A média de idades é {media:.1f}')
print(f'O nome do homem mais velho é {nomeVelho}')
print(f'A quantidade de mulheres com mais de 20 anos é {fem20}')




    