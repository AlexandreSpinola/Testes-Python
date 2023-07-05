"""
Um grupo de espiões utiliza rádios para conversar entre si a respeito de operações secretas. Entretanto, eles sabem que as frequências utilizadas são interceptadas pela contra inteligência, dessa forma eles desenvolveram um código para indicar diversas ações. Por exemplo, para mandar uma mensagem de "Avancar" ou "Retroceder" para indicar a ação a ser tomada eles devem passar pelo rádio um número contendo 6 dígitos. O receptor deverá extrair o segundo dígito e o quinto dígito. Caso a soma dos dois seja igual a 7 ou 8 e a multiplicação seja igual a 12 a equipe deverá avançar, caso contrário, retroceder. Faça um algoritmo para extrair a informação.

Entradas:

Um número inteiro contendo 6 dígitos.
Saídas:

Uma string correspondente ao status do local.
Exemplo de Entrada:

040030
Exemplo de Saída:

Avancar
Exemplo de Entrada 2:

147840
Exemplo de Saída 2:

Retroceder
"""

n= str(input())


if ((int (n[1])) + (int(n[4])) == 7 or ((int (n[1])) + (int(n[4])) == 8))  and ((int(n[1]))*(int(n[4]))== 12):
	print("Avancar")
else:
	print("Retroceder")