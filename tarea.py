
nombre = input("¿como te llamas?")
if nombre:
    print(nombre)
else:
    print ("no se ha proporcionado un nombre.")
    exit()
apellidoPaterno = input("¿cual es tu apellido paterno?")
if apellidoPaterno:
    print(apellidoPaterno)
else:
    print("no se ha proporcionado apellidoPaterno")
    exit()
apellidoMaterno = input("¿cual es tu apellido materno?")
if apellidoMaterno:
    print(apellidoMaterno)
else:
    print("no se ha proporcionado apellidoMaterno")
    exit()
edad =int(input("¿cuantos años tienes?"))
if edad:
    print(edad)
else:
    print("no se ha proporcionado edad")
    exit()
estatura = float(input("¿cual es tu altura en metros?"))
if estatura:
    print(estatura)
else:
    print("no se ha proporcionado estatura")
    exit()
peso = int(input("¿cual es tu peso en kilogramos?"))
if peso:
    print(peso)
else:
    print("no se ha proporcionado peso")
    exit()

Imc = peso/estatura**2

print (f"hola{nombre} {apellidoPaterno} {apellidoMaterno} tu indice de masa corporal es {Imc}")
 
 