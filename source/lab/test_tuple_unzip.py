

def prueba(val1, val2, val3, *args):
    print(val1)
    print(val2)
    print(val3)
    print(args)

value= (1,2,3,4,5,6,7,8,9)

(*_, ultimo)= value

print(ultimo) 


nombres=("Andres", "Samir", "Rosemberg")
apellidos=("Niño", "Mendoza", "Porras")
edad=("24", "43", "10")


zipping= zip(nombres, apellidos, edad)

print (zipping)