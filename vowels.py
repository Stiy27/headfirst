# -*- coding: utf-8 -*-
vowels = ["a", "e", "i", "o", "u"]
word = input("Forneça uma palavra para procurar por vogais: ")
found = []

#Pega cada letra da palavra
for letter in word:
    #Verifica se cada letra está em vogais
    if letter in vowels:
        #Verifica se a letra não existe em found e adiciona
        if letter not in found:
            found.append(letter)
#Imprime a lista de vogais
print(found)
print()

#Imprime as vogais em linhas separadas
for vowel in found:
    print(vowel)