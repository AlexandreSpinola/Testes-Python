"""
Depois de um estudo aprofundado, um pesquisador chegou a conclusão que existe uma relação entre as notas atribuídas por críticos de cinema e a população em geral. Nesta pesquisa, concluiu-se que a nota dos críticos é equivalente a 90% da nota da população quando os filmes são da categoria terror ou guerra, de 80% em filmes de ação ou ficção, não se altera em filmes de romance ou suspense e aumentam em 20% em filmes de drama ou tragédias. Faça um programa que calcule a provável nota de um crítico.

Entradas:

Nota média atribuída pela população (real).
Estilo do filme ('TERROR','GUERRA','ACAO','FICCAO','TRAGEDIA','DRAMA','ROMANCE' ou 'SUSPENSE').
Saídas:

Provável nota do crítico (real).
Exemplo


Exemplo de entrada:

5.64
TERROR
Exemplo de Saída:

5.08
"""

nota_media= float(input())
estilo_filme= input()     #'TERROR','GUERRA','ACAO','FICCAO','TRAGEDIA','DRAMA','ROMANCE' ou 'SUSPENSE')

if estilo_filme == "TERROR" or estilo_filme== "GUERRA":
	nota_media= nota_media *0.90
	print(nota_media)
if estilo_filme == "ACAO" or estilo_filme== "FICCAO":
	nota_media= nota_media*0.80
	print(nota_media)

if estilo_filme == "ROMANCE" or estilo_filme== "SUSPENSE":
	nota_media= nota_media *1
	print(nota_media)
	
if estilo_filme == "DRAMA" or estilo_filme== "TRAGEDIA":
	nota_media= nota_media *1.20
	print(nota_media)