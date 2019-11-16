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
limite=(total_pagar>10)

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

#condicional doble
#si el comprador supera el monto de 10$$ gano un descuento del 10%

if(limite):
    print("ud. gano un descuento de 10%")
else:
    print("VUELVA PRONTO")
#fin_if

