preço_produto=float(input('Qual o preço do produto escolhido?'))
desconto_produto=preço_produto * 0.05
preço_final=preço_produto - desconto_produto
print(f'O valor inicial do produto era de {preço_produto}, o valor após o desconto de 5%, ficou igual a {preço_final}')