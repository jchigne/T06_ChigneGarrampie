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

#condicional doble
#si superan los 20 kilos se llevara el descuento frutero

if(limite):
    print("UD. gano el descuento frutero")
else:
    print("Gracias por su compra, Tenga un buen dia")
#fin_if
