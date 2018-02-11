'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = int(input('N1 =>'))
n2 = int(input('N2 =>'))
n3 = int(input('N3 =>'))

print(sorted((n1, n2, n3), key=int, reverse=True)) 