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
limite=(total>15)

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

#condicional doble
#si el comprador supera los 30kg ganara un mini saco de arroz

if(limite):
    print("Felicidades ud. ha ganado un mini sakito de arroz")
else:
    print("GRACIAS VUELVA PRONTO")
#fin_if

