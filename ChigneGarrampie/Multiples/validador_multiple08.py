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

#condicional multiple
#si el empleado gano mas de 1000 tiene vvacaciones pagadas
#si el empleado gano mas de 1500 su suelto aumentara 10% mas

if(limite):
    print("us.acaba de ganar vacaciones pagadas")
if(total<100):
    print("Gracias por su trbajo")
if(total>1500):
    print("Felicidades su sulto subira un 10% mas")
#fin_if
