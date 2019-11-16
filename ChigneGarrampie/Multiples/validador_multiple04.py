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

#condicional multiple
#si el monto supero los 40$ puedes acceder al 2x3
#si supera los 100$ se le dara un descuento del 35%

if(limite):
    print("us. puede aseder al 2x3")
if(total<40):
    print("Gracias por su compra,Vuelva pronto")
if(total>100):
    print("Felicidades se le otorgara un descuento del 35%")
#fin_if
