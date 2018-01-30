'''
Crie um programa que receba a data de nascimento de ma pessoa, seu no,e e cerifique se ela pode votar

'''

nome = input('Seu nome?\n')
ano = int(input('Seu ano de nacimento?\n'))

if ano < 2000:
  print(nome + ' nasceu em ' + str(ano) + ' e tem que votar')

elif ano <= 2002:
  print(nome + ' nasceu em ' + str(ano) + ' e vota se quiser')

else:
  print(nome + ' nasceu em ' + str(ano) + ' e não pode votar')