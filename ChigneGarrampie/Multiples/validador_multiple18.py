import os
#Compra de frutas
#declaracion de datos
mansanas,peras,platanos=0.0,0.0,0.0
limite=False

#input
mansanas=float(os.sys.argv[1])
peras=float(os.sys.argv[2])
platanos=float(os.sys.argv[3])

#processing
total=(mansanas+peras+platanos)
limite=(total>20)

#output
print("Kilos de mansanas:",mansanas)
print("kilos de peras:",peras)
print("kilos de platanos:",platanos)
print("total de kilos:",total)

#condicional multiple
#si superan los 20 kilos se llevara el descuento frutero
#si el total supera los 100 kilos gano una sandia gratis

if(limite):
    print("UD. gano el descuento frutero")
if(total<20):
    print("Gracias por su compra")
if(total>100):
    print("Felicidades acaba de llevarse una sandia gratis")
#fin_if
