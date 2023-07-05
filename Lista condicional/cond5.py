"""
Você encontrou uma pedra mágica capaz de prever a estação do ano e a sensação térmica. Caso a pedra esteja molhada e quente, a estação atual é primavera, caso esteja molhada e fria a estação é inverno, caso esteja seca e quente a estação é verão, nas outras situações é outono. Além disso, a pedra pode ajudar a calcular a sensação térmica, sendo que se for primavera a sensação térmica equivale a temperatura da pedra acrescida de 10%, caso seja inverno a sensação térmica equivale a temperatura da pedra decrescida de 10%, caso seja verão deve-se acrescentar 20% e caso não se enquadre nestas situações a sensação térmica é a mesma da temperatura da pedra.

Entradas:

Estado da pedra ('MOLHADA' ou 'SECA')
Estado da pedra ('QUENTE' ou 'FRIA')
Temperatura da pedra (real)
Saídas:

Estação ('PRIMAVERA','INVERNO','VERAO' ou 'OUTONO')
Sensação Térmica (real)

"""

estadop1= input()
estadop2= input()
temp= float(input())
estadoF= str()
if estadop1 == "MOLHADA" and estadop2== "QUENTE":
	estadoF= "PRIMAVERA"
	print(estadoF)
if estadop1 == "MOLHADA" and estadop2=="FRIA":
	estadoF="INVERNO"
	print(estadoF)
if estadop1 == "SECA" and estadop2 == "QUENTE":
	estadoF= "VERAO"
	print(estadoF)
if estadop1 == "SECA" and estadop2 == "FRIA":
	estadoF="OUTONO"
	print(estadoF)

if estadoF== "PRIMAVERA":
	temp= temp*1.1
	print(temp)
if estadoF=="INVERNO":
	temp= temp*0.9
	print(temp)
if estadoF== "VERAO":
	temp= temp*1.2
	print(temp)
if estadoF=="OUTONO":
	print(temp)