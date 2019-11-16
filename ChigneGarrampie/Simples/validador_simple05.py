import os
#declaracion de datos
cliente,horas,precio="",0.0,0.0
limite=False

#Input
cliente=os.sys.argv[1]
horas=float(os.sys.argv[2])
precio=float(os.sys.argv[3])

#processing
total=(horas*precio)
limite=(total>50)

#output
print("#########################")
print(" # GIMNACIO PEPITO      #")
print("# horas ejercitadas:",horas)
print("# Nombre del cliente:",cliente)
print("# prcio:",precio)
print("total a pagar=",total)
print("#########################")

#condicional simple
#si el monto supera los 50 obtendra un energisador gratis

if(limite):
    print("Ud acaba de ganar un bebida energisante gratis")
#fin_if

