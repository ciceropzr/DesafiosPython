'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota1 = float(input('Primeiro Semestre: '))
nota2 = float(input('Segunda Semestre: '))

media = (nota1 + nota2) / 2

def conceito():
  if media >= 9.0:
    print('O conceito é A')

  elif media >= 7.5 and media < 9:
    print('O conceito é B')

  elif media >= 6.0 and media < 7.5:
    print('O conceito é C')

  elif media >= 4.0 and media < 6:
    print('O conceito é D')

  else:
    print('O conceito é E')

def mensagem():
  if media >= 6.0:
    print('APROVADO')

  else:
    print('REPROVADO') 

print('\nNotas: ' + str(nota1) + ' e ' + str(nota2))
print('Sua media é ' + str(media))
conceito()
mensagem()