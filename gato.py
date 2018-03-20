'''
Escreva um programa que receba uma palavra com mais de cinco letras
e troque as últimas quatro letras pela palavra gato.
'''


palavra = input('Digite uma palavra:\t')
letrasq = len(palavra)

while letrasq < 5:
	print('\nA palavra contem menos que 5 letras!')
	palavra = input('Digite uma palavra maior:\t')
	letrasq = len(palavra)

	if letrasq >= 5:
		break

print(palavra[4:] + "gato")