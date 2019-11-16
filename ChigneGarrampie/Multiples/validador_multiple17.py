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
limite=(total>1000)

#output
print("Primera venta:,",venta01)
print("Segunta venta:",venta02)
print("Tercera venta:",venta03)

#condicional multiple
#si ventio mas de 1000$ gano 10$ mas
#Si vendio mas de 2000$ gano 200 mas
#si vendio mas de 5000$ gano 500 mas

if(limite):
    print("Ud acaba de ganar 100 nuevos soles")
if(total>2000):
    print("Ud acaba de ganar 200 nuevos soles")
if(total>5000):
    print("Ud acaba de ganar 500 nuevos soles")
#fin_if
