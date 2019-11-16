import os
#declaracion de datos
deportista,distancia,tiempo="",0.0,0.0
limite=False

#imput
deportista=os.sys.argv[1]
distancia=float(os.sys.argv[2])
tiempo=float(os.sys.argv[3])

#processing
velocidad=(distancia/tiempo)
limite=(velocidad>10)

#output
print("# nombre del atleta:",deportista)
print("# distacia recorrida:",distancia)
print("# tiempo:",tiempo)
print("# velocidad del atleta:",velocidad)

#condicional doble
#si el deportista tiene una velicidad > a 20 calificara para maraton

if(limite):
    print("Felicidades califico para la maraton")
else:
    print("Gracias por su participacion")
#fin_if
