import os
#venta de inmuebles
#declaracion de datos
venta01,venta02,venta03=0.0,0.0,0.0
limite=False

#input
venta01=float(os.sys.argv[1])
venta02=float(os.sys.argv[2])
venta03=float(os.sys.argv[3])

#prcessing
total=(venta03+venta02+venta01)
limite=(total>100)

#output
print("Primera venta:,",venta01)
print("Segunta venta:",venta02)
print("Tercera venta:",venta03)

#condicional simple
#si ventio mas de 100$ gano 10$ mas

if(limite):
    print("Ud acaba de ganar 10 nuevos soles")
#fin_if

