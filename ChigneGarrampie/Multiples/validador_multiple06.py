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

#condicional multiple
#si el alumno supera los 10 aprobara
#si el alumno supera los 15 quedara entre los mejores 10

if(limite):
    print("Felicidades aprobo el curso :D")
if(promedio<10):
    print("Siga practicado")
if(promedio>15):
    print("Felicidades esta entre los 10 mejores")
#fin_if


