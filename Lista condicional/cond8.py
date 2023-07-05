"""
Ao comprar nos supermercados Lavras, de acordo com o valor de sua compra, você ganha um saldo para a próxima compra. O saldo é calculado da seguinte forma:

Compras até R$ 100,00 ganhe de volta 1%
Compras acima de R$ 100,00, ganhe de volta 3%
Faça um programa que recebe como entrada o valor da compra e retorne o saldo que o cliente ganhará para a próxima compra.

Entradas:

Valor real, indicando o valor da compra
Saídas:

Valor real, com duas casas decimais (arredondado, se necessário), indicando o saldo obtido na compra
Exemplo de Entrada:

95.40
Exemplo de Saída:

0.95
"""
valor= float(input())

if valor<=100:
	print( valor *0.01)
else:
	print(valor*0.03)