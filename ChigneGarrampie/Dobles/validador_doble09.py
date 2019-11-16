import os
#declaracion de datos
cliente,polos,precioU="",0,0.0
limite=False

#imput
cliente=os.sys.argv[1]
polos=int(os.sys.argv[2])
precioU=float(os.sys.argv[3])

#prcessing
total=(polos*precioU)
limite=(total>50)

#output
print("# cliente:",cliente)
print("# polos:",polos)
print("# precio unitario:",precioU)
print("# total a pagar:",total)

#condicional doble
#si el monto supera los 50$ ganara un polo gratis

if(limite):
    print("Ud. acaba de ganar un polo gratis")
else:
    print("Gracias por su compra")
#fin_if
