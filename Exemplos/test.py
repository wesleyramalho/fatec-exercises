# from numpy.random import seed
# from numpy.random import randint
# seed random number generator
# seed(1)
# generate some integers
# values = randint(0, 10, 20)
# import random
# values = random.randrange(8923483)  
# print(values)


# from random import randint

# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)

# print(random_with_N_digits(2))
# print(random_with_N_digits(3))
# print(random_with_N_digits(1))


# import sys

# listaDeMatriculas = []
# nomeDoArquivo = 'MATR.TXT'

# def lerArquivo():
#   with open(nomeDoArquivo) as arquivo:
#       conteudoArquivoEmLista = arquivo.read().splitlines() #lendo linha a linha e inserindo numa lista sem o \n
#   return conteudoArquivoEmLista

# # print(lerArquivo())

# arquivoSaida = 'SENHAS.TXT'
# def escreverArquivo(arquivoSaida):
#   arqreais = open(arquivoSaida, 'w') # w+ cria um novo arquivo caso não exista
#   arqreais.write("oi amigos kkk") # linha 5
#   arqreais.close() 

# escreverArquivo(arquivoSaida)
# Exemplo para percorrer lista
# vingadores = ['Homem de Ferro', 'Hulk', 'Capitão America', 'Viúva Negra', 'Gavião Arqueiro']
# for i in range(0, len(vingadores)):
#     print('Vingador:', vingadores[i])
# print()
# for h in vingadores:
#     print('Vingador:', h)



# senha = list(range(4))
# senha[0] = 'lkj'
# senha[1] = 'lkj'
# senha[2] = 'lkj'
# senha[3] = 'lkj'
# print("".join((senha)))



minhaListaLinda = range(5)
print(minhaListaLinda[0], "lista")
print(minhaListaLinda[1], "lista")
print(minhaListaLinda[2], "lista")
print(minhaListaLinda[3], "lista")
print(minhaListaLinda[4], "lista")