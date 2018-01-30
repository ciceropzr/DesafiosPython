x = int(input('Insira um número => '))

if x < 0 and x % -2 == -1:  
  print('Número negativo impar')

elif x < 0 and x % -2 == 0:
  print(' Número negativo par')

elif x % 2 == 0 and x != 0:
  print(' Número positivo par')

elif x == 0:
  print('Zero é NULOOOOOOOO....')

else:
  print('Número positivo impar')