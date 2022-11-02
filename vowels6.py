vowels = ['a', 'e', 'i', 'o', 'u']
word = input ("Forneça uma palavra para buscar por vogais: ")

found = {}

for letter in word:
    if letter in vowels:
        # Inicializa o item do dicionário se for encontrado e elimina o erro: KeyError
        found.setdefault(letter, 0)
        # incrementa o item em 1
        found[letter] += 1
        
for k, v in sorted(found.items()):
    print (k, 'foi encontrada', v, 'vez(es)')