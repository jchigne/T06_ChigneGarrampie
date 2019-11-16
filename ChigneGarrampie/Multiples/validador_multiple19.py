import os
#declaracion de datos
nombre,dias,horas="",0,0.0
limite=False

#imput
nombre=os.sys.argv[1]
dias=int(os.sys.argv[2])
horas=float(os.sys.argv[3])

#processing
limite=(dias>15)

#output
print("el monbre del trabajador:",nombre)
print("dias trabajados:",dias)
print("horas trabajadas:",horas)

#condicional multiple
#si trabajo mas de 15 dias resibira una semana libre
#si trabajo mas de 30 dias resivira 15 dias libres

if(limite):
    print("Felicidades resivira una semana libre")
if(dias<15):
    print("Gracias por su trabajo que tenga un buen fin de semana")
if(dias>30):
    print("Felicidades se le otorgara 15 dias libres")
#fin_if
