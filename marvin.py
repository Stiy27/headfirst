paranoid_android = "Marvin, the paranoid android"
letter = list(paranoid_android)

for char in letter[:6]:
    print ('\t', char)

for char in letter[-7:]:
    print (2*'\t', char)
    
for char in letter[12:20]:
    print (3*'\t', char)