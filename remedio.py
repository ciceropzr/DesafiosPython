'''
Maria tem que tomar remédios de 15 em 15 minutos.
Escreva um programa que mostre todos os horários em que 
Maria precisa tomar o remédio num período de um dia.
'''


for horas in range(0,24):
	for minutos in range(0,60,15):
		print(str(horas)+ ':' + str(minuto))