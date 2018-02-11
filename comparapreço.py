'''

Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

'''
produlto1 = float(input('Produto 1 = '))
produlto2 = float(input('Produto 2 = '))
produlto3 = float(input('Produto 3 = '))

barato = min(produlto1, produlto2, produlto3)

print('R$%.2f' % barato)