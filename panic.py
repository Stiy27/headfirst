phrase = "Don`t panic!"
plist = list(phrase)

print(phrase)
print(plist)

# Remove os 3 últimos caracteres da lista
for i in range(4):
    plist.pop()

# Remove o primeiro caractere
plist.pop(0)
# Remove o apóstofro
plist.remove("`")

# Remove o "p" e o "a", então adiciona invertendo as posições
plist.extend([plist.pop(), plist.pop()])

# Remove o espaço do índice 3 e adiciona no índice 2
plist.insert(2, plist.pop(3))

# Transforam a lista em uma string
new_phase = ''.join(plist)

print(plist)
print(new_phase)