import os
#Muestra la division de 2 numeros
numero01,numero02=0.0,0.0
limete=False

#imput
numero01=float(os.sys.argv[1])
numero02=float(os.sys.argv[2])

#processing
division=(numero01/numero02)
limete=(division>10)

#output
print("El divisor es:",numero01)
print("El dividendo es:",numero02)
print("El residuo es:",division)

#condicional multiple
#si el residuo es mayor a 10 iso un buen trabajo
#si el residio es menor a 10 es un errror
#si el residio es mayor a 20 los datos son erroneos

if(limete):
    print("Felicidades UD. ayo la respuesta")
if(division<10):
    print("Respuesta incorrecta")
if(division>20):
    print("Error no puede haber un resudio mayor a 20")
#fin_if

