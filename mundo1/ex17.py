import math
angulo=int(input('Digite em graus o seu ângulo °:'))
seno=math.sin(math.radians(angulo))
print(f'O angulo {angulo} tem o SENO de {seno:.3f}')
cos=math.cos(math.radians(angulo))
print(f'O ângulo {angulo} tem o COSSENO de {cos:.3f}')
tan=math.tan(math.radians(angulo))
print(f'O ângulo {angulo} tem a TANGENTE de {tan:.3f}')
