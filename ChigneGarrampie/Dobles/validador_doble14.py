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

#condicional doble
#si la fuerza resultante es mayor a 20 uso bien los datos

if(limete):
    print("Uso muy bien los datos")
else:
    print("Se confundio al momento de ayar la respuesta")
#fin_if
