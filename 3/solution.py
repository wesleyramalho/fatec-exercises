# -*- coding: utf-8 -*-
import io
import sys
import numbers

tiposValidosDeSenha = ["a", "b", "c", "d", "e", "A", "B", "C", "D", "E"]

TipoGlobal = 'kk'
TamanhoGlobal = 0


def ValidarTipoSenha(senhaDigitada):
  if tiposValidosDeSenha.count(senhaDigitada): # se o tipo de senha for uma das opções disponíveis, retorna verdadeiro
    return True 
  return False # se não, retorna falso

def ValidarTamanhoSenha(tamanhoDigitado):
  # if isinstance(tamanhoDigitado, int): # se o tamanho for uma variável do tipo inteiro, retorna verdadeiro
  return True
  return False


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

def IniciarPrograma():
  LerTipoSenha()


def GeraSenha(Tipo, Tam):
  print("Gerando senha...")
  print("Tipo:")
  print(Tipo)
  print("Tamanho:")
  print(Tam)
  senha = 'ksdfjla'
  return senha

IniciarPrograma()