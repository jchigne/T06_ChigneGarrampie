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

#condicional doble
#si trabajo mas de 15 dias resibira una semana libre

if(limite):
    print("Felicidades resivira una semana libre")
else:
    print("Sigue asi, gracias por su trabajo")
#fin_if
