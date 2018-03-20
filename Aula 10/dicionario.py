'''
1 - Escreva um dicionário sobre o perfil de um usuário do Github.
2 - Adicione novos campos a esse dicionários
3 - Exiba esse dicionário mostrando cada chave e valor
'''

#========== 1 ==========#

cicero = {
	'username': 'ciceropzr',
	'repositórios': '16',
	'followers': '3',
	'following': '1'
}

# print('Parte 1 :\n' + str(cicero))

#========== 2 ==========#

cicero['stars']= '0'

print('Parte 2 :\n' + str(cicero))

# #========== 3 ==========#

# for key in cicero:
#   print(key + ':\t' + cicero[key])