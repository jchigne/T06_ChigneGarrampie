import os
#Declaracion de datos
alumno,nota01,nota02,nota03="",0.0,0.0,0.0
limite=False

#Imput
alumno=os.sys.argv[1]
nota01=float(os.sys.argv[2])
nota02=float(os.sys.argv[3])
nota03=float(os.sys.argv[4])

#processing
promedio=(nota01+nota02+nota03)/3
limite=(promedio>10)

#output
print("nota 01:",nota01)
print("nota 02:",nota02)
print("nota 03:",nota03)
print("promedio final:",promedio)

#condicional simple
#si el alumno supero los 10 aprobara

if(limite):
    print("Felicidades aprobo el curso :D")
#fin_if


