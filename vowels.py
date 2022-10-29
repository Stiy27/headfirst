# -*- coding: utf-8 -*-

# Trabalhando com Dicionários

vowels = ["a", "e", "i", "o", "u"]
word = input("Forneça uma palavra para procurar por vogais: ")

# Dicionário vazio
found = {} #{"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}


#Pega cada letra da palavra
for letter in word:
    # Verifica se a letra está na lista de vogais
    if letter in vowels:
        # "setdefault" evita exception de "KeyErro" e permite aumentar um dicionário dinamicamente
        found.setdefault(letter, 0)
        # Incrementa em 1 o valor da chave no dicionário.
        found[letter] += 1
                   
#Imprime a lista/dicionário de vogais
print()
#ordena o dicionário por item
print(sorted(found.items()))
print()

#Imprime as vogais em linhas separadas
#for vowel in found:
#    print(vowel)