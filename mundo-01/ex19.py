import random
aluno1=input('Digite o nome do primeiro aluno:')
aluno2=input('Digite o nome do segundo aluno:')
aluno3=input('Digite o nome do terceiro aluno:')
aluno4=input('Digite o nome do quarto aluno:')
lista_nomes=aluno1,aluno2,aluno3,aluno4
escolhido=random.choice(lista_nomes)
print('Dentre os alunos {},{},{} e {}, foi escolhido o(a) {} para realizar a tarefa desejada.'.format(aluno1,aluno2,aluno3,aluno4,escolhido))