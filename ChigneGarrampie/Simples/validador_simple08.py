import os
#declaracion de datos
trabajador,dias,pago="",0.0,0.0
limite=False

#imput
trabajador=os.sys.argv[1]
dias=int(os.sys.argv[2])
pago=float(os.sys.argv[3])

#processing
total=(dias*pago)
limite=(total>1000)

#output
print("nombre del trabajador:",trabajador)
print("dias trabajados:",dias)
print("pago por dias:",pago)
print("total pagado",total)

#condicional simple
#si el empleado gano mas de 1000 tiene vvacaciones pagadas

if(limite):
    print("us.acaba de ganar vacaciones pagadas")
#fin_if
