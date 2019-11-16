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

#Comdisional simple
#si la edad es mayor a 18 si accedera a tener una cuenta

if(limite):
    print("Edad permitida")
    print("Cuenta creada")
#fin_if
