# -*- coding: utf-8 -*-
import io
import sys

tiposValidosDeSenha = 'abcde'

tiposValidosDeSenha = ["a", "b", "c", "d", "e"]

def ValidarTipoSenha(senhaDigitada):
  if tiposValidosDeSenha.count(senhaDigitada):
    return True
  return False
    # LerTipoSenha()

def ValidarTamanhoSenha(tamanhoDigitado):
  # if(senhaDigitada not in tiposValidosDeSenha)
    # print("Por favor, escolha um tipo de senha válido.")
    # LerTipoSenha()


# def LerTamanhoSenha():
#     Tipo = sys.stdin.read(1) # Lê somente um caractere

def LerTipoSenha():
    print("Por favor, escolha um tipo de senha:/n")
    print("a. Numérica – conterá apenas algarismos/n")
    print("b. Alfabética – conterá apenas letras maiúsculas e minúsculas/n")
    print("c. Alfanumérica 1 – conterá letras maiúsculas e algarismos/n")
    print("d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos/n")
    print("e. Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres ASCII [33, 46] e [58, 64]")
  # Tipo = sys.stdin.read(1) # Lê somente um caractere
  # if ValidarTipoSenha(Tipo): 
  #   print("Boa champs.")
  # else:
  #   print("Fez merda")
  # print(Tipo)


def IniciarPrograma():
  print("Iniciando Programa...")
  # LerTipoSenha()



def GeraSenha(Tipo, Tam):
  return senha

IniciarPrograma()