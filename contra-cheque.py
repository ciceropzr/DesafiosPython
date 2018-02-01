por_hora = int(input("Ganho por horas\n"))
trabalho = int(input("Horas trabalhadas/mes\n"))

bruto = trabalho * por_hora
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ( ir + inss + sindicato)

print('Salário bruto R$' + str('%.2f' % bruto))
print('Desconto do Imposto de Renda R$' + str('%.2f' % ir))
print('Desconto do INSS R$' + str('%.2f' % inss))
print('Desconto do Sindicato R$' + str('%.2f' % sindicato))
print('Salário Líquido R$' + str('%.2f' % liquido))