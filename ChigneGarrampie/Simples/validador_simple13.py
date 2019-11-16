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

#condicional simple
#si el residuo es mayor a 10 iso un buen trabajo

if(limete):
     print("Felicidades UD. ayo la respuesta")
#fin_if

