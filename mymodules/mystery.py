def double(arg):
    print("Before: ", arg)
    arg = arg * 2 # Aplicará a semântica por valor, não modifica o valor da variável do código que chama
    #arg *= 2      # Aplicará a semântica por referência, modificando o valor da variável...
    print("After: ", arg)
    
    
def change(arg):
    print("Before: ", arg)
    arg.append("More data")
    print("After: ", arg)
    

num = 10
double(num)
print(num)
saying = 'Hello '
double(saying)
print(saying)
numbers = [42, 256, 16]
double(numbers)
print(numbers, "\n\n")

change(numbers)
print(numbers)