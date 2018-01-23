preço = int(input('Preço do Hot-Dog\n'))
cliente = input('Nome de clinte\n')
quant = int(input('Quantos Hot-Dog?\n'))
pagar = preço * quant

print('O cliente ' + cliente +  ' comprou ' + str(quant) + ' cacholos quientes e vai pagar\nR$' + str('%.2f' % pagar))