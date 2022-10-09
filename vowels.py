vowels = ["a", "e", "i", "0", "u"]
word = "Milliways"
found = []

#Pega cada letra da palavra
for letter in word:
    #Verifica se cada letra está em vogais
    if letter in vowels:
        #Verifica se a letra não existe em found e adiciona
        if letter not in found:
            found.append(letter)
        
print(found)