print('Início do Programa')

import random

arq = open('NUMEROS.txt', 'w')

for i in range(1,2001):
    n = random.randint(1,100000)
    arq.write("{}\n".format(n))    

arq.close()

print("{} gravados no arquivo NUMEROS.txt!".format(i))
print('Fim do Programa')