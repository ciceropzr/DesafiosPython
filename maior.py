n1 = int(input('N1 =>'))
n2 = int(input('N2 =>'))
n3 = int(input('N3 =>'))

def maior(): 
  if n1 > n2 and n1 > n3:
    print(n1)

  elif n2 > n1 and n2 > n3:
    print(n2)

  elif n3 > n1 and n3 > n2:
    print(n3)

  else:
    print('Tds maiores iguais')

def menor():
  if n1 < n2 and n3:
    print(n1)

  elif n2 < n1 and n3:
    print(n2)

  elif n3 < n1 and n2:
    print(n3)

  else:
    print('Tds menores iguais')  

maior()
menor()