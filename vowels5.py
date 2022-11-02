vowels = ['a', 'e', 'i', 'o', 'u']
word = input ("Forneça uma palavra para buscar por vogais: ")

found = {}

'''
   Removida a inicialização dos itens
   Causará erro: KeyErro, itens de dicionário não inicializados
'''

for letter in word:
    if letter in vowels:
        
        # incrementa o item em 1
        found[letter] += 1
        
for k, v in sorted(found.items()):
    print (k, 'foi encontrada', v, 'vez(es)')