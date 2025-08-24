numUser=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão de sua progressão aritmética: '))
soma=0
for progressaoAritmetica in range(1,11):
    termo=numUser+ progressaoAritmetica * razao
    print(termo)