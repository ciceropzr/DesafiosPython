'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino 
ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
ou "Valor Inválido!", conforme o caso.'''

resposta = input('Digite M-matutino ou V-Vespertino ou N- Noturno: ')

if resposta.lower() == 'm':
  print('Bom dia!!')

elif resposta.lower() == 'v':
  print('Boa Tarde!!')

elif resposta.lower() == 'n':
  print('Boa Noite!!')

else:
  print('Valor Inválido!')