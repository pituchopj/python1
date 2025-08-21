print('---------------LOJA PITUCHO--------------------')
valorCompra=float(input('Digite o valor da compra: '))
formaPagamento=input({'FORMA DE PAGAMENTO: \n', '{1} á vista / dinheiro' , '{2} á vista / cartão' '{3} 2x no cartão' '{4} 3x ou mais no cartão'})
if formaPagamento == '1':
    desconto= valorCompra * 0.1
    valorFinal= valorCompra - desconto
    print(f'O valor da sua compra com o desconto é {valorFinal}')
elif formaPagamento == '2':
    desconto = valorCompra * 0.05
    valorFinal = valorCompra - desconto
    print(f'O valor da sua compra com o desconto é {valorFinal}')
elif formaPagamento == '3':
    valorFinal = valorCompra
    print(f'O valor da sua compra com o desconto é {valorFinal}')
elif formaPagamento == '4':
    juros=valorCompra * 0.3
    valorFinal=valorCompra + juros
    print(f'O valor da sua compra com o desconto é {valorFinal}')
    