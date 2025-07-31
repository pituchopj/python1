def soma(a,b):
    soma=a+b
    return soma
def subtrai (a,b) :
    subtrai=a-b
    return subtrai
def multiplicaçao (a,b):
    multiplicaçao=a*b
    return multiplicaçao
def divisao (a,b):
    divisao=a/b
    return divisao
def potencia (a,b):
    potencia = a**b
    return potencia
n1=int(input('Digite um número '))
n2=int(input('DIgite outro número '))
print(f'A soma dos números{n1} e {n2} é igual a {soma(n1,n2)}, a subtração é {subtrai(n1,n2)}, a multiplicação é {multiplicaçao(n1,n2)}, a potencia é {potencia(n1,n2)}, a divisaõ é {divisao(n1,n2)}')