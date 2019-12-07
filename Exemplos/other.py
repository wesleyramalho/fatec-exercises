import math

arquivo = open('ALUNOS.txt','r')
i = 1

N = arquivo.readline()
print('{}  {:30}  {:^}  {:>10}'.format('Matrícula', 'Nome do Aluno', 'Média Final', 'Situação'))

while(N != ""):
    L = N.split(';')

    p1 = L[1]
    p2 = L[2]
    mt = L[3]
   
    media = ((4 * float(p1)) + (4 * float(p2)) + (2 * float (mt))) / 10

    L.pop(3)
    L.pop(2)
    L.pop(1)
    L.pop()
    L.append('{:.1f}'.format(media))

    if (media >= 6):
        aluno = 'Aprovado'
    else:
        aluno = 'Reprovado'

    print('{}  {:30}  {:<13.1f}  {:<15}'.format(L[0], L[1], media, aluno))

    N = arquivo.readline()