def numPrimo(n):
    if n==1:
        return False
    if n == 2:
        return True
    for num in range(2, int(n ** 0.5) + 1):
        if numPrimo % num == 0:
            return False
        return True
numInt=int(input('Digite um número: '))
if numPrimo(numInt):
    print(f'O número {numInt} é primo!')
else:
    print(f'O número {numInt} não é primo')


    