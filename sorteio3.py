'''
Crie um programa que sorteia um valor entre 1 e 30 e receba um valor do usuario.
Verifique se ele acertou, dê  a ele 3 chances de tentar. Se ele acertar exiba uma mensagem
informando, se não, ao final das tentativas, exiba o número correto.
'''

import random 

numero = random.randint(1, 30)

tentativas = 0

while tentativas < 3:
  tentativa = int(input('Digite um numero: '))

  tentativas = tentativas + 1

  if tentativa == numero:
    	print('Acertou')
    	break

print('O numero sorteado é ' + str(numero))