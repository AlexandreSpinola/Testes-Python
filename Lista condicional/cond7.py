"""
A companhia Choque Ltda fornece energia elétrica para a cidade de Lavras. Para emitir a fatura de cobrança de um cliente residencial a empresa verifica o consumo mensal (quantidade de energia consumida em quilowatts, kWh) e calcula o preço de acordo com a equação e regras estabelecidas a seguir:

Preço = Valor referente à quantidade consumida + Taxa fixa

Regras:

Até 10 kWh o valor referente à quantidade consumida é de R$ 5,00. Nesse caso, a taxa fixa é igual a R$ 0,00.
Acima de 10 kWh até 100 kWh, o valor referente à quantidade consumida é dado pelo consumo (kWh) multiplicado pela taxa de R$ 0,60. Nesse caso, a taxa fixa é igual a R$ 2,00.
Acima de 100 kWh a taxa fixa é igual a R$ 3,00. Além disso, o valor referente à quantidade consumida é calculado da seguinte maneira:
R$ 0,60 por kWh para os primeiros 100 kWh,
R$ 0,85 por kWh para os próximos 50 kWh,
R$ 1,20 por kWh para a quantidade restante, ou seja, para aquilo que ultrapassa 150 kWh.
Escreva um programa que receba como entrada a quantidade de energia elétrica consumida por um cliente residencial e calcule o valor da fatura desse cliente.
Entrada:

Consumo mensal em kWh (número inteiro).
Saída:

Valor da fatura do cliente.
Exemplo de Entrada:

9
Exemplo de Saída:

5.0

"""

consumo= int(input())
alto=0
if consumo <=10:
	print(5.00)
	
if consumo > 10 and consumo <=100:
	print((consumo*0.60)+ 2)
	
if consumo >100 and consumo<= 150:
	medio= consumo -100
	consumo= (medio*0.85)+63
	print(consumo)

if consumo> 150:
	consumo= 105.5+(consumo -150)*1.20
	print(consumo)