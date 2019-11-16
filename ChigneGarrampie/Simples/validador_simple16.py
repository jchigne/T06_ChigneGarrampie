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

#condicional simple
#se el area en menor a 300 es pequeña

if(limite):
    print("Su casa es pequena")
#fin_if
