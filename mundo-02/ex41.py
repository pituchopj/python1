idadeAtleta=int(input)('Digite a idade do atleta: ')
if idadeAtleta <= 9:
    print('Atleta MIRIM')
elif 9<idadeAtleta <=14:
    print('Atleta INFANTIL ')
elif 14<idadeAtleta <-19:
    print('Atleta JÚNIOR ')
elif 19<idadeAtleta<=25:
    print('Atleta SÊNIOR')
elif idadeAtleta > 25:
    print('Atleta MASTER')

#– Até 25 anos: SÊNIOR
# – Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
# – Acima de 25 anos: MASTER