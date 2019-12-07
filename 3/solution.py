# -*- coding: utf-8 -*-
import io
import sys
import numbers
from random import randint

TiposValidosDeSenha = ["a", "b", "c", "d", "e", "A", "B", "C", "D", "E"]

TipoGlobal = 'inicializando tipo global'
TamanhoGlobal = 0

# Funções auxiliares:

def GerarNumeroAleatorioComNDigitos(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Funções de validação:

def ValidarTipoSenha(SenhaDigitada):
  if TiposValidosDeSenha.count(SenhaDigitada): # se o tipo de senha for uma das opções disponíveis, retorna verdadeiro
    return True 
  return False # se não, retorna falso

# Funções para leitura de dados

def LerTipoSenha():
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
      GeraSenha(TipoGlobal, TamanhoGlobal)
    else:
      print("Por favor, digite um tipo válido de senha.")
      exit() # encerra o programa caso seja um tipo inválido

#Funções para gerar senha

# a. Numérica – conterá apenas algarismos;
def GerarSenhaTipoA(Tamanho):

  Senha = 'TipoA'
  return Senha

# b. Alfabética – conterá apenas letras maiúsculas e minúsculas;
def GerarSenhaTipoB(Tamanho):
  Senha = 'TipoB'
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
  print("Gerando senha...")
  # print("Tipo:")
  # print(Tipo)
  # print("Tamanho:")
  # print(Tam)

  GerarFuncaoPorTipo = tipoParaFuncao(Tipo)
  Senha = GerarFuncaoPorTipo(Tam)
  print(Senha)
  return Senha


def IniciarPrograma():
  LerTipoSenha()

IniciarPrograma()