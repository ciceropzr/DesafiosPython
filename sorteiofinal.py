'''
Crie um programa que sorteia um valor entre 1 e 30 e receba um valor do usuario.
Verifique se ele acertou, dê  a ele 3 chances de tentar. Se ele acertar exiba uma mensagem
informando, se não, dê uma nova chance e informe se o número é mais baixo ou mais alto, ao 
final das tentativas exiba o numero correto
'''

import random 

numero = random.randint(1, 30)

tentativas = 0

while tentativas < 3:
  tentativa = int(input('Digite um numero de 1 a 30:\t'))
  # print(numero)
  tentativas = tentativas + 1

  if tentativa == numero:
    print('Finalmente acertou!')
    break

  elif tentativa > numero:
  	print('É menor')

  else:
  	print('É maior')

else:
	print('Errou e acabatam as tentativas! E o numero correto é ' + str(numero))
