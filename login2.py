user = input("user: ")
password = input("password: ")
pet_stuff = input("pet stuff: ")
date_of_birtf = input("date_of_birtf: ")

number_of_letters = len(password)

if number_of_letters < 8:
  print('Password must be at least 8 characters')

elif user == password or password == pet_stuff or password == date_of_birtf:  
  print('Password invalid, can not be equal to user, pet stuff or date of birth. Try again!')

else:
  print('Valid Password')