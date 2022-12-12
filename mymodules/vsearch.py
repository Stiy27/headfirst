# -*- coding: utf-8 -*-

# Utilizando Funções com anotações (:str, :int)
# Declaramos que o argumento (word) é uma string e que a função retorna um conjunto: (-> set)
def vowel_search(phrase:str) -> set:
    """ Exibe qualquer vogal encontrada em uma palavra fornecida. """
    vowels = set('aeiou')
    #uniao => vowels.union(set(word))
    #diferenca => vowels.difference(set(word))
    return vowels.intersection(set(phrase))


# O argumento (letters) tem o valor padrão 'aeiou' atribuido.
def search4letters(phrase:str, letters:str='aeiou') -> set:
    """ Retorna um conjunto de letras encontradas na frase. """
    # Transforam o argumento letters em um objeto conjunto
    return set(letters).intersection(set(phrase))
