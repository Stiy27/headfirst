# -*- coding: utf-8 -*-
vowels = ["a", "e", "i", "o", "u"]
word = input("Forneça uma palavra para procurar por vogais: ")
found = []

#Pega cada letra da palavra
for letter in word:
    # Verifica se a letra está na lista de vogais
    if letter in vowels:
        # Verifica se a letra não está na lista found
        if letter not in found:
            # se não existir, essa letra será adicionada na lista found
            found.append(letter)

#Imprime as vogais em linhas separadas
for vowel in found:
    print (vowel)        
            
#Imprime a lista/dicionário de vogais
print()
print(found)
print()