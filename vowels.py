# -*- coding: utf-8 -*-
vowels = ["a", "e", "i", "o", "u"]
word = input("Forneça uma palavra para procurar por vogais: ")
#found = []
found = {"a": 0,
         "e": 0,
         "i": 0,
         "o": 0,
         "u": 0}

#Pega cada letra da palavra
for letter in word:
    #Verifica se cada letra está em vogais
    if letter in vowels:
        # Nova linha para contar ocorrencia de letras e atualizar no dicionário
        found[letter] += 1
        
        #Verifica se a letra não existe em found e adiciona
        if letter not in found:
            found.append(letter)
            
#Imprime a lista de vogais
print()
print(found)
print()

#Imprime as vogais em linhas separadas
#for vowel in found:
#    print(vowel)