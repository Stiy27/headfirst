# -*- coding: utf-8 -*-

# Utilizando Funções com anotações (:str, :int)
# Declaramos que o argumento (word) é uma string e que a função retorna um conjunto: (-> set)
def vowel_search(word:str) -> set:
    """ Exibe qualquer vogal encontrada em uma palavra fornecida. """
    vowels = set('aeiou')
    #uniao = vowels.union(set(word))
    #diferenca = vowels.difference(set(word))
    if bool(word):
        return vowels.intersection(set(word))
    else:
        pass

    #return bool(found)
    #for vowel in found:
    #    print (vowel)
 
 
#word = input('Forneça uma palavra para procurar por vogais: ')
vowel_search('abacaxi')