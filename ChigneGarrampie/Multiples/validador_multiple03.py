import os
#Declaracion de datos
cliente,sacos_arroz,pu_arroz="",0.0,0.0
limite=False

#INPUT
cliente=os.sys.argv[1]
sacos_arroz=int(os.sys.argv[2])
pu_arroz=float(os.sys.argv[3])

# PROCESSING
total = (pu_arroz* sacos_arroz)
limite=(total>150)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",sacos_arroz,"  Nr de sacos de arroz")
print("# P.U.   :  S/.", pu_arroz)
print("# Total  :  S/.", total)
print("#######################")

#condicional multiple
#si el comprador supera los 150$ ganara un mini saco de arroz
#si supera los 250$ se le dara un descuento del 15%

if(limite):
    print("Felicidades ud. ha ganado un mini sakito de arroz")
if(total<150):
    print("Gracias por su compra")
if(total>250):
    print("Ud adquirio un descuento del 15%")
#fin_if

