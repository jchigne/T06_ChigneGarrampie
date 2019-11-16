import os
#venta de prendas de vestir
#declaracion de datos
busos,polos,casacas=0,0,0
limite=False

#input
busos=int(os.sys.argv[1])
polos=int(os.sys.argv[2])
casacas=int(os.sys.argv[3])

#processing
total=(busos+polos+casacas)
limite=(total>10)

#output
print("Numeros de busos:",busos)
print("Numeros de polos:",polos)
print("Numeros de casacas:",casacas)
print("Total de prendas compradas:",total)

#condicional simple
#si el numero deprendas compradas supera las 20 ganara un conjuntos gratis

if(limite):
    print("ud a ganado una conjunto gratis,GRACIAS POR SU COMPRA")

#fin_if
