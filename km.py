'''
O valor de entrada contém dois valores, em valor inteiro X, representatdo a ditância percorrida (em Km),
e um valor real Y representando o tatal de combustivel gasto, com um digito após a casa decimal.
'''

X = int(input())
Y = int(input())

consumoMedio = X / Y

print(str('%.3f' % consumoMedio) + ' Km/l')