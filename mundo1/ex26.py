nome=input('Digite uma frase: ') 
qt_a=nome.count('A'.upper())+nome.count('a'.lower())
print('Seu nome tem {} letras "A" ou "a" '.format(qt_a))
p_a = nome.upper().find('A')
p_a2=nome.upper().rfind('A')
print('Considere que começa no 0...')
print('A primeira letra "A" aparece no {}° espaço e a última no {}° espaço.'.format(p_a, p_a2))




