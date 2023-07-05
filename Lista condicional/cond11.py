"""
Dado um número inteiro N de 5 dígitos (00000 <= N <= 99999), você deve fazer um programa para descobrir a quantidade de dígitos de N que são divisíveis por 2 e por 3. Lembre que o número ZERO (0) é divisível por qualquer número.

Entradas:

Um número inteiro N de 5 dígitos.
Saídas:

Um número inteiro que indica a quantidade de dígitos existentes em N que são divisíveis por 2;
Um número inteiro que indica a quantidade de dígitos existentes em N que são divisíveis por 3;
Um número inteiro que indica a quantidade de dígitos existentes em N que são divisíveis por 2 e por 3, ao mesmo tempo;
Exemplo de Entrada:

12346
Exemplo de Saída:

3
2
1
Exemplo de Entrada:

23069
Exemplo de Saída:

3
4
2

"""

N= int(input())

a=0
b=0
c=0
d=0
e=0
 
if ((N//10000)%10)%2==0:
	a=1
else:
		a=0
if ((N//1000)%10)%2==0:
	b=1
else:
	b=0
if ((N//100)%10)%2==0:
	c=1
else:
	c=0
if ((N//10)%10)%2==0:
	d=1
else:
	d=0
if ((N)%10)%2==0:
	e=1
else:
	e=0
print(a+b+c+d+e)

#######################

if ((N//10000)%10)%3==0:
	a=1
else:
		a=0
if ((N//1000)%10)%3==0:
	b=1
else:
	b=0
if ((N//100)%10)%3==0:
	c=1
else:
	c=0
if ((N//10)%10)%3==0:
	d=1
else:
	d=0
if ((N)%10)%3==0:
	e=1
else:
	e=0
print(a+b+c+d+e)

######################

if ((N//10000)%10)%3==0 and ((N//10000)%10)%2==0 :
	a=1
else:
		a=0
if ((N//1000)%10)%3==0 and ((N//1000)%10)%2==0 :
	b=1
else:
	b=0
if ((N//100)%10)%3==0 and ((N//100)%10)%2==0 :
	c=1
else:
	c=0
if ((N//10)%10)%3==0 and ((N//10)%10)%2==0:
	d=1
else:
	d=0
if ((N)%10)%3==0 and ((N)%10)%2==0:
	e=1
else:
	e=0
print(a+b+c+d+e)


