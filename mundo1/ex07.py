
def soma (a,b,c):
    c=a+b
    soma=c
    return soma
def media (a,b,c):
    c=a+b
    media=c/2
    return media
a=float(input('Digite a sua primeira nota:'))
b=float(input('Digite sua segunda nota:'))
c=(soma)
resultado_media=media(a,b,c)
print(f'A média de suas notas é {media(a,b,c)}')
if resultado_media >= 7:
    print('Aprovado!\n Parabéns')
else:
    print('Reprovado!\n Estude mais')