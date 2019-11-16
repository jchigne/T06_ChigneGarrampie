import os
#Crear una cuenta de credito
#declaracion de datos
nombre,dni,edad="",0,0
limite=False

#imput
nombre=os.sys.argv[1]
dni=int(os.sys.argv[2])
edad=int(os.sys.argv[3])

#processing
limite=(edad>18)

#output
print("##########################")
print("###  BANCO NACIONAL     ##")
print("# Nombre del cliente:",nombre)
print("# Dni del cliente:",dni)
print("# Edad del cliente:",edad)

#Comdisional multiple
#si la edad es mayor a 18 si accedera a tener una cuenta
#si la edad es mayor a 60 se le pedira un garante

if(limite):
    print("Edad permitida")
    print("Cuenta creada")
if(edad<18):
    print("Edad insuficiente")
    print("Cuenta rechasada")
if(edad>60):
    print("Gracias por crearse una cuenta")
    print("Ud nesesita un garante")
#fin_if
