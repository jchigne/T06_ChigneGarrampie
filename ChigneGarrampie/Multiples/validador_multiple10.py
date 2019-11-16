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

#condicional multiple
#si el deportista tiene una velocidad > a 10 calificara para maraton
#si el deportista tiene una velocidad mayor a 20 contamos en el

if(limite):
    print("Felicidades califico para la maraton")
if(velocidad<10):
    print("Gracias por participar")
if(velocidad>20):
    print("Ud tiene un talento increible contamos con ud")
#fin_if
