import os
#boleta de venta
#Declaracion de Datos
clinete,nombre_tinda,kg_naranjas,cantidad="","",0.0,0
limite=False

#IMPUT
cliente=os.sys.argv[1]
nombre_tinda=os.sys.argv[2]
kg_naranjas=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])

#PROCESSING
total= (kg_naranjas*cantidad)
limite=(total>100)

#OUTPUT
print("#######################################")
print("#  BOLETA DE VENTA 01")
print("#######################################")
print("#")
print("#cliente:  ",    cliente)
print("# Item   :  ",cantidad,"  Nr de naranjas")
print("P.U     : s/.",   kg_naranjas)
print("# TOTAL : s/.",      total)
print("#######################################")

#condicional doble
#si el comprador supera los 20kg de narajas ganara un descuento del 15%

if(limite):
    print("Felicidades gano 15% de descuento")
else:
    print("GRACIAS POR SU COMPRA")
#fin_if
