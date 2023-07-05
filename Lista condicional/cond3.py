"""Uma pessoa está aprendendo sobre cores, ela aprendeu que existem as cores primárias (amarelo, vermelho e azul) e as cores secundárias (verde, laranja e violeta) que são cores derivadas das primárias, mas ela está com dificuldades para entender a mistura das cores primárias e os resultados, para isso, ela pediu para você desenvolver um programa em que ela insira duas cores primárias e mostre o resultado da mistura das cores. As informações das misturas podem ser consultadas na tabela a seguir:

Mistura	Resultado
Azul+Amarelo	Verde
Azul+Vermelho	Violeta
Vermelho+Amarelo	Laranja
O programa deverá receber como entrada duas cores primárias escritas com letras minúsculas e deverá mostrar como saída o resultado da mistura entre elas com letras minúsculas.

Obs: A ordem das entradas não altera o resultado e caso as entradas sejam iguais, o resultado será a própria cor.

Entradas:

Primeira cor primária (letras minúsculas).
Segunda cor primária (letras minúsculas).
Saídas:

Resultado da mistura (letras minúsculas)
Exemplo de Entrada:

amarelo
vermelho
Exemplo de Saída:

laranja
Exemplo de Entrada:

azul
azul
Exemplo de Saída:

azul
"""

cor1=input()
cor2=input()

if cor1== "azul" and cor2== "amarelo":
	print("verde")
if cor1== "azul" and cor2== "vermelho":
	print("violeta")
if cor1== "vermelho" and cor2== "amarelo":
	print("laranja")
	
#ORDEM INVERSA

if cor1== "amarelo" and cor2== "azul":
	print("verde")
if cor1== "vermelho" and cor2== "azul":
	print("violeta")
if cor1== "amarelo" and cor2== "vermelho":
	print("laranja")

#MESMA COR 

if cor1== "amarelo" and cor2== "amarelo":
	print("amarelo")
if cor1== "vermelho" and cor2== "vermelho":
	print("vermelho")
if cor1== "azul" and cor2== "azul":
	print("azul")
