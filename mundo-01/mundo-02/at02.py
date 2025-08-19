saque=int(input('Digite o valor do seu saque: '))
n1=int(50)
nota=saque // n1
saque2=saque%n1
n2=int(10)
nota2=saque2//n2
saque3=saque2%n2
n3=int(1)
nota3=saque3 // n3
saque4=saque3%n3
print(f'Seu saque é de {saque}\n Você receberá:\n {nota} nota(s) de 50 R$ \n {nota2} nota(s) de 10 R$ \n {nota3} nota(s) de 1 R$')
