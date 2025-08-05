nome=str(input('Digite seu nome completo: ')).split()
true='SILVA' in [n.upper() for n in nome]
print('Seu nome tem Silva?  {}'.format (true))