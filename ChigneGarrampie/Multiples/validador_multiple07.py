import os
#declaracion de datos
obrero,horas,pu_hora="",0.0,0.0
limite=False

#imput
obrero=os.sys.argv[1]
horas=float(os.sys.argv[2])
pu_hora=float(os.sys.argv[3])

#processing
total_pagar=(horas*pu_hora)
limite=(total_pagar>200)

#output
print(" nombre del obrero:",obrero)
print("horas trabajadas:",horas)
print("pu por hora:",pu_hora)
print("total a pagar:",total_pagar)

#condicional multiple
#si el vendedor ganas mas de 200$ tentra un dia libre
#si el vendedor gano mas de 500 tenra una semana libre

if(limite):
    print("UD. acaba de ganar un dia libre")
if(total_pagar<200):
    print("Suerte la proxima ves")
if(total_pagar>500):
    print("Exelente, gano una semana libre")
#fin_if

