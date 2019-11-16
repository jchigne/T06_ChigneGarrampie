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
limite=(total>20)

#OUTPUT
print("#######################################")
print("#  BOLETA DE VENTA #")
print("#######################################")
print("#")
print("#cliente:  ",    cliente)
print("# Item   :  ",cantidad,"  Nr de naranjas")
print("P.U     : s/.",   kg_naranjas)
print("# TOTAL : s/.",      total)
print("#######################################")

#condicional multiple
#si el comprador supera los 20kg de narajas ganara un descuento del 15%
#si supera los 40 kilos se le dara un descueto del 35%

if(limite):
    print("Felicidades gano 15% de descuento")
if(total<20):
    print("Gracias por su compra")
if(total>40):
    print("Felicidades gano un descuento de 35%")
#fin_if
