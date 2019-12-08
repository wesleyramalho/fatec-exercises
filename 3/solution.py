# -*- coding: utf-8 -*-
import io
import sys
import numbers
from random import randint
from random import randrange

TiposValidosDeSenha = ["a", "b", "c", "d", "e", "A", "B", "C", "D", "E"]

nomeDoArquivoEntrada = 'MATR.TXT'
nomeDoArquivoSaida = 'SENHAS.TXT'
listaMatriculas = []
listaSenhas = []
TipoGlobal = "inicializando tipo"
TamanhoGlobal = 0

# Funções auxiliares:

def checarSeNumeroEPar(numero):
  if (numero % 2) == 0:
    return True
  return False

def GerarNumeroAleatorioComNDigitos(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Funções para trabalhar com arquivos

def lerArquivo(nomeDoArquivo):
  with open(nomeDoArquivo) as arquivo:
      conteudoArquivoEmLista = arquivo.read().splitlines() #lendo linha a linha e inserindo numa lista sem o \n
  return conteudoArquivoEmLista


def escreverArquivo(arquivoSaida, lista):
  arquivo = open(arquivoSaida, 'w') # 'w+' cria um novo arquivo caso não exista, 'a' adiciona no arquivo, 'w' escreve no arquivo
  for item in lista:
        arquivo.write("%s\n" % item)
  arquivo.close() 


# Funções de validação:

def ValidarTipoSenha(SenhaDigitada):
  if TiposValidosDeSenha.count(SenhaDigitada): # se o tipo de senha for uma das opções disponíveis, retorna verdadeiro
    return True 
  return False # se não, retorna falso

# Funções para leitura de dados

def LerTipoSenha():
    # Utilizando variáveis globais para sobrescrita
    global TipoGlobal
    global TamanhoGlobal

    print("Por favor, escolha um tipo de senha:")
    print("a. Numérica – conterá apenas algarismos")
    print("b. Alfabética – conterá apenas letras maiúsculas e minúsculas")
    print("c. Alfanumérica 1 – conterá letras maiúsculas e algarismos")
    print("d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos")
    print("e. Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres ASCII [33, 46] e [58, 64]")

    
    Tipo = sys.stdin.read(1) # Lê somente um caractere
    if ValidarTipoSenha(Tipo): 
      TipoGlobal = Tipo
      TamanhoGlobal = int (input ("Digite o tamanho da senha (número inteiro): "))
    else:
      print("Por favor, digite um tipo válido de senha.")
      exit() # encerra o programa caso seja um tipo inválido

#Funções para gerar senha

# a. Numérica – conterá apenas algarismos;
def GerarSenhaTipoA(Tamanho):
  Senha = GerarNumeroAleatorioComNDigitos(Tamanho)
  return Senha

# b. Alfabética – conterá apenas letras maiúsculas e minúsculas;
def GerarSenhaTipoB(Tamanho):
  MAIUSCULAS_ASCII_PRIMEIRO_DECIMAL = 65
  MAIUSCULAS_ASCII_ULTIMO_DECIMAL = 90

  MINUSCULAS_ASCII_PRIMEIRO_DECIMAL = 97
  MINUSCULAS_ASCII_ULTIMO_DECIMAL = 122

  # Para cada caractere até completar o tamanho da lista, gerar um caractere aleatório dentro do range ASCII
  # que contemple apenas letras MAIÚSCULAS e minúsculas
  
  #Gerando uma lista que será transformada numa string e armazenará cada caractere da nova senha  
  senha = list(range(Tamanho))

  # gerando cada caractere da senha
  for indice in range(Tamanho):
    # Se o indice for par, gerar caractere MAIUSCULO
    # Aqui qualquer lógica que escolha alguma das opções de range da tabel ASCII é válida, optei por checar se o índice é par ou ímpar
    if checarSeNumeroEPar(indice):
      # chr() converte um número para um caractere com base na tabela ASCII
      senha[indice] = chr(randrange(MAIUSCULAS_ASCII_PRIMEIRO_DECIMAL, MAIUSCULAS_ASCII_ULTIMO_DECIMAL))
    # Se o indice for ímpar, gerar caractere minúsculo
    else:
      senha[indice] = chr(randrange(MINUSCULAS_ASCII_PRIMEIRO_DECIMAL, MINUSCULAS_ASCII_ULTIMO_DECIMAL))
  # Transformando lista de senha em string com caracteres juntos
  Senha = "".join((senha))
  return Senha

# c. Alfanumérica 1 – conterá letras maiúsculas e algarismos;
def GerarSenhaTipoC(Tamanho):
  Senha = 'TipoC'
  return Senha

# d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos;
def GerarSenhaTipoD(Tamanho):
  Senha = 'TipoD'
  return Senha

# e. Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres ASCII [33, 46] e [58, 64]
def GerarSenhaTipoE(Tamanho):
  Senha = 'TipoE'
  return Senha

switcher = {
        "a": GerarSenhaTipoA,
        "A": GerarSenhaTipoA,
        "b": GerarSenhaTipoB,
        "B": GerarSenhaTipoB,
        "c": GerarSenhaTipoC,
        "C": GerarSenhaTipoC,
        "d": GerarSenhaTipoD,
        "D": GerarSenhaTipoD,
        "e": GerarSenhaTipoE,
        "E": GerarSenhaTipoE,
    }
 
 
def tipoParaFuncao(tipo):
    func = switcher.get(tipo, "nenhum tipo")
    return func

def GeraSenha(Tipo, Tam):
  GerarSenhaPorTipo = tipoParaFuncao(Tipo)
  senha = GerarSenhaPorTipo(Tam)
  return senha


def IniciarPrograma():
  # Utilizando variáveis globais
  global TipoGlobal
  global TamanhoGlobal


  # Valida a entrada do usuário e armazena o tipo nas variáveis globais antes da leitura do arquivo
  LerTipoSenha() 
  
  # Lê arquivo e transforma o conteúdo para uma lista iterável
  listaMatriculas = lerArquivo(nomeDoArquivoEntrada) 

  # Para cada prontuário do arquivo, gera uma senha baseada na escolha do usuário
  for matricula in listaMatriculas:
    senha = GeraSenha(TipoGlobal, TamanhoGlobal)
    #converte os inteiros para string e concatena as variáveis formatando-as da forma que tem que ser inseridas no arquivo
    listaSenhas.append(str(matricula) + ';' + str(senha) + ';')

  #salva matricula;senha; no arquivo de SENHAS.TXT
  escreverArquivo(nomeDoArquivoSaida, listaSenhas)


IniciarPrograma()