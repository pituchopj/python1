import math
print('Temos um triângulo retângulo!')
oposto=int(input('Digite em metros, o cateto oposto desse triângulo:'))
adjacente=int(input('Agora digite o tamanho do cateto adjacente:'))
hipotenusa=int(math.hypot(oposto,adjacente))
print('A hipotenusa deste triângulo é {}.'.format (hipotenusa))