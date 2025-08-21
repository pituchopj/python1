n1=int(input('Digite um número: '))
print('Escolha a base de conversão; 1 para binário, 2 para octal e 3 para hexadecimal.')
escolha=int(input('1 - Binário\n 2 - Octal \n 3 - Hexadecimal\n'))
if escolha == 1:
    binario=bin(n1)[2:]
    print(f'O número {n1} em número binário fica {binario}.')
elif escolha == 2:
    octal= oct(n1)[2:]
    print(f'O número {n1} em número octal fica {octal}.')
elif escolha == 3:
    hexadecimal=hex(n1)[2:]
    print(f'O número {n1} em número hexadecimal fica {hexadecimal}.')
else:
    print('Opção Inválida')

