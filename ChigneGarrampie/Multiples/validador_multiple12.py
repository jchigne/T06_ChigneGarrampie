import os
#muestra si se puede recaudar el monto nesesario para ir de paseo
#declaracion de datos
monto01,monto02,monto03=0.0,0.0,0.0
limite=False

#imput
monto01=float(os.sys.argv[1])
monto02=float(os.sys.argv[2])
monto03=float(os.sys.argv[3])

#processing
total=(monto01+monto02+monto03)
limite=(total>100)

#output
print("El monto 01:",monto01)
print("El monto 02",monto02)
print("El monto 03:",monto03)
print("En total se recaudo:",total)

#condicional multiple
#si el monto supera los 100$ si abra viaje
#si el monto supera los 200$ almuerzo gratis para todos

if(limite):
    print("Si se llego a la meta establecida.Iremos de viaje")
if(total<100):
    print("No llegamos a la meta establecida")
if(total>200):
    print("Viaje y almuerzo gratis para todos")
#fin_if