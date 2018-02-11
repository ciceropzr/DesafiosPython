'''
Escreva um algoritimo para recarga de celular, que receba um numero de telefone,
é comum perguntamos o número novamente para confirmar, se o numero estiver errado
peça para ele tentar novamente, e exiba uma mensagem de erro, se não, mostre uma
mensagem informando qur a transição foi feita.
'''

telefone1 = input('Didite seu numero:\n')
telefone2 = input('Confirme seu numero:\n')

while telefone1 != telefone2 :
  print('Erro! Tente Novamente')
  telefone1 = input('Didite seu numero:\n')
  telefone2 = input('Confirme seu numero:\n')

else:
  print('Recarga feita com susseso!')