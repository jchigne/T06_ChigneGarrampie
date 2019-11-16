import os
#Area de una casa
#declaracion de datos
largo,ancho=0.0,0.0
limite=False

#imput
largo=float(os.sys.argv[1])
ancho=float(os.sys.argv[2])

#precessing
area=(largo*ancho)
limite=(area<300)

#output
print("AREA DE UNA CASA")
print("Largo de la casa:",largo)
print("Ancho de la casa:",ancho)
print("Area total:",area)

#condicional multiple
#se el area en menor a 300 es pequeña
#si el area en mayor de 300 pero menor de 500 es mediana
#si el area es mayor a 500  es Grande

if(limite):
    print("Su casa es pequena")
if(area>300 and area<500):
    print("Su casa es mediana")
if(area>500 and area<5000):
    print("Su casa es Grande")
#fin_if
