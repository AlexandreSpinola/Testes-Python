"""
A contribuição mensal a ser paga ao INSS é calculada segundo a tabela a seguir:

Salário	Alíquota
até 1.693,72	8%
de 1.693,73 até 2.822,90	9%
de 2.822,91 até 5.645,80	11%
Assim, um empregado que receba um salário de R$ 1.000,00 pagará 8% (R$ 80,00) de contribuição ao INSS, um assalariado que recebe R$ 3.000,00 pagará 11% (R$ 330,00). Já um assalariado que recebe R$ 10.000,00 pagará o teto da contribuição, que é 11% em cima do valor máximo da tabela, ou seja, 11% de R$ 5.645,80 (R$ 621,04 - valor obtido por arredondamento).

Faça um programa que receba o salário de um empregado e retorne o valor da contribuição mensal ao INSS.

Entradas:

Salário de um empregado.
Saídas:

Valor da contribuição mensal paga ao INSS.
Exemplo de Entrada:

1345.50
Exemplo de Saída:

107.64 
"""

salario= float(input())

#até 1.693,72	8%
#de 1.693,73 até 2.822,90	9%
#de 2.822,91 até 5.645,80	11%

if salario <=1693.72:
	print( salario*0.08)
if salario > 1693.72 and salario <= 2822.90:
	print(salario*0.09)
if salario> 2822.90 and salario <=5645.80 :
	print(salario*0.11)
if salario > 5645.80 :
	print (5645.80 *0.11)
 
 