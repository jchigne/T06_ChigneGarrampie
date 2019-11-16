import os
#declaracion de datos
masa,aceleracion=0.0,0.0
limete=False

#imput
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])

#processing
fuerza=(masa*aceleracion)
limete=(fuerza>20)

#uotput
print("La masa del cuerpo es:",masa)
print("LA aceleracion es:",aceleracion)
print("La fuerza resultante es:",fuerza)

#condicional multiple
#si la fuerza resultante es mayor a 20 uso bien los datos
#Si la fuerza supera los 100N , esta es mucha

if(limete):
    print("Uso muy bien los datos")
if(fuerza<20):
    print("La fuerza no es suficiente para el movil")
if(fuerza>100):
    print("La fuerza usada es demasiada")

#fin_if
