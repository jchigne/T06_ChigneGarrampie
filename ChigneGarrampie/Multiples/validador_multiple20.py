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

#condicional multiples
#si el numero de prendas compradas supera las 20 ganara un conjuntos gratis
#si el numero de prendas compradas supera las 30 se le ara un descuento de 50% en polos

if(limite):
    print("ud a ganado una conjunto gratis,GRACIAS POR SU COMPRA")
if(total<10):
    print("Gracias por su compra")
if(total>30):
    print("Felicidades se acaba de ganar un descuento en polos del 50%")
#fin_if
