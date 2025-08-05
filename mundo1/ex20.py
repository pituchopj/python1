import random
aluno1=input('Primeiro aluno:')
aluno2=input('Segundo aluno:')
aluno3=input('Terceiro aluno:')
aluno4=input('Quarto aluno:')
lista_alunos=([aluno1,aluno2,aluno3,aluno4])
random.shuffle(lista_alunos)
print('A ordem de apresentação será:{}'.format(lista_alunos))
for aluno in lista_alunos:
    print(aluno)