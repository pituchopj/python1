import time
numUser=int(input('Digite o primeiro termo: '))
razao= int(input('Digite a razão da progressão aritmetica: '))
progressaoAritmetica=1
while progressaoAritmetica <= 10:
    termo=numUser + progressaoAritmetica * razao
    progressaoAritmetica+=1
    print(termo)
print('PAUSA')
time.sleep(5)
exibição=int(input('Quantos termos a mais você quer ver? '))
progressaoAritmetica = 10
while progressaoAritmetica <= exibição + 10:
    termo=numUser + progressaoAritmetica * razao
    progressaoAritmetica += 1
    print(termo)


