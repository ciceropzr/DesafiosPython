usuario = input("usuario: ")
Senha = input("Senha: ")
animal_de_estimação = input("animal de estimação : ")
data_de_nascimento = input("data de nascimento: ")

número_de_caracteries = len(Senha)

if número_de_caracteries < 8:
  print('Senha precisa ter no mínimo 8 caracteres.')

elif usuario == Senha or Senha == animal_de_estimação or Senha == data_de_nascimento:  
  print('Senha invalida, não pode ser igual ao usuário, animal de estimação ou data de nascimento. Tente de novo!')

else:
  print('Senha valida!')