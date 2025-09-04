pesos=[]
for reps in range(0,6):
    peso=int(input('Digite em kg, seu peso: '))
    pesos.append(peso)
maior=max(pesos)
menor= min(pesos) 
print('O maior é {} e o menor é {}' .format(maior, menor))