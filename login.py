'''
Faca um programa que leia um nome de usuário e a senha e não aceite a senha igual ao nome do usuário,
mmostrando uma mensagem de erro e voltando a pedir as informaçãoes.
'''

user = input("user: ")
password = input("password: ")

if user == password:  
  print('Invalid Password')

else:
  print('Valid Password')
