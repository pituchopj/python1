reta1=float(input('Digite o tamanho em metros da primeira reta: '))
reta2=float(input('Digite o tamanho em metros da segunda reta: '))
reta3=float(input('Digite o tamanho em metros da terceira reta: '))
if reta1< (reta2 + reta3) and reta2 < (reta1+reta3) and reta3 < (reta1 + reta2):
    print('As suas retas podem formar um triângulo!')
else:
    print('As suas retas não podem formar um triângulo.')
