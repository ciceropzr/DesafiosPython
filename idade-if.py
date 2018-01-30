'''
Crie um programa que receba idade de uma pessoa e verifique se ela pode votar

=> entrada:
    idade
    nome

<= saida
  if = "nome" tem "idade" anos e pode votar
  else = "nome" tem "idade" anos e não pode votar

'''

nome = input('Seu nome?\n')
idade = int(input('Sua idade?\n'))

if idade > 18:
  print(nome + ' tem ' + str(idade) + ' anos e tem que votar')

elif idade >= 16:
  print(nome + ' tem ' + str(idade) + ' anos e vota se quiser')

else:
  print(nome + ' tem ' + str(idade) + ' anos e não pode votar')