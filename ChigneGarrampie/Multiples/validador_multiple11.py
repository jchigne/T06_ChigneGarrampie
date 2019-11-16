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

#condisional multiple
#si el costo total es > 100 hubo perdida
#si el costo toal es < 50 bono para todos

if(limite):
    print("Este mes de Trabajo si hubo perdidas econimocas")
if(costo_total<100):
    print("Este mes no hubo perdidas economicas")
if(costo_total<50):
    print("Este mes hay bono para todos")
#fin_if
