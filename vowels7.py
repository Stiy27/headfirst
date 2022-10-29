# -*- coding: utf-8 -*-

# Utilizando Conjuntos

vowels = set("aeiou")
word = input("Forneça uma palavra para procurar por vogais: ")

uniao = vowels.union(set(word))

diferenca = vowels.difference(set(word))

vogais = vowels.intersection(set(word))

for letter in vogais:
    print (letter)
