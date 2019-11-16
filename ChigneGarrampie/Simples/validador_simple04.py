import os
#Declaracion de datos
cliente,pantalones,pu_pantalones="",0.0,0.0
limite=False

#INPUT
cliente=os.sys.argv[1]
pantalones=int(os.sys.argv[2])
pu_pantalones=float(os.sys.argv[3])

# PROCESSING
total = (pu_pantalones*pantalones)
limite=(total>40)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",pantalones,"  Nr de pantalones")
print("# P.U.   :  S/.", pu_pantalones)
print("# Total  :  S/.", total)
print("#######################")

#condicional simple
#si el monto supero los 40$ puedes acceder al 2x3

if(limite):
    print("us. puede aseder al 2x3")
#fin_if

