'''
Eescreva um algorotimo que recebe uma data de nascimento de usuário, e compare 
essa data com uma data existente pré-cadrastrada. Se a senha for diferente, 
exiba uma mensagem de erro, e pergunte novamente.
'''

nascimento = input('Sua data de Nascimento:\n')

while nascimento != '04031995':
  print('Informaçao Incorreta')
  nascimento = input('Sua data de Nascimento\n')