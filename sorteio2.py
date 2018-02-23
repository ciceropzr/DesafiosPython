'''
Crie um programa que sorteia um valor entre 1 e 30 e receba um valor do usuario,
se o usuario acetar exiba uma mensagem parabenizando
'''

import random 

numero = random.randint(1, 30)
tentativa = int(input('Digite um numero: '))

if numero == tentativa:
  print('Acertou!')

else:
  print('Não foi dessa vez!')