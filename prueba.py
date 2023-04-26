def Hola():
    i = 0
    i = eval(input("Escribe un numero (desde el 1): "))
    if(i == 1):
        print("This is my world!")
    elif(i == 2):
        print("You should know this place")
    else:
        print("This is another world!")
    return 0

Hola()