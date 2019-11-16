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

#condicional simple
#si el obrero ganas mas de 200$ tentra un dia libre

if(limite):
    print("UD. acaba de ganar un dia libre")
#fin_if
