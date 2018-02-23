'''
Crie um programa que sorteia um valor entre 1 e 30 e receba um valor do usuario.
Verifique se ele acertou, dê  a ele 3 chances de tentar. Se ele acertar exiba uma mensagem
informando, se não, dê uma nova chance e informe se o número é mais baixo ou mais alto, ao 
final das tentativas exiba o numero correto
'''

import random 

numero = random.randint(1, 30)

tentativas = 1

while tentativas <= 3:
  tentativa = int(input('Digite um numero de 1 a 30:\t'))

  tentativas = tentativas + 1

  if tentativa == numero:
    print('Acertou')
    break

print('Agora vamos te ajudar.')

while tentativas > 3:
	tentativa = int(input('Digite um numero de 1 a 30:\t'))

	if tentativa > numero:
		print('\n\tÉ mais baixo')

	elif tentativa < numero:
		print('\n\tÉ masi alto')

print('Finalmente acertou!')
	