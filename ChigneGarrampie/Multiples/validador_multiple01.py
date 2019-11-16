import os
#boleta de venta
#declaracion de variables
limite=False

#imput
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])

#pocessing
total_pagar=(precio*cantidad)
limite=(total_pagar>100)

#output
print("########################")
print("#   BOLETA DE VENTA    #")
print("########################")
print("# Cliente:",cliente)
print("# Producto:",producto)
print("# Precio:",precio)
print("# Cantidad:",cantidad)
print(" Total a pagar:",total_pagar)
print("#########################")

#condicional multiple
#si el comprador supera el monto de 100$ gano un descuento del 10%
#si supera el 200$ ganara un descuento del 25%

if(limite):
    print("ud. gano un descuento de 10%")
if(total_pagar<100):
    print("Gracias por su compra")
if(total_pagar>200):
    print("Ud gano un descuento del 25%")
#fin_if

