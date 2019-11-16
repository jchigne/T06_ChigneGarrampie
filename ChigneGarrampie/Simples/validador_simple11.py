import os
#declaracion de datos
costo_fijo,costo_variable=0.0,0.0
limite=False

#imput
costo_fijo=float(os.sys.argv[1])
costo_variable=float(os.sys.argv[2])

#processing
costo_total=(costo_variable+costo_fijo)
limite=(costo_total>100)

#output
print("# El costo fijo:",costo_fijo)
print("# El costo Variable:",costo_variable)
print("# El costo total:",costo_total)

#condisional simple
#si el costo total es > 100 hubo perdida

if(limite):
    print("Este mes de Trabajo si hubo perdidas econimocas")
#fin_if
