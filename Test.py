#Solicitar el salario actual y el tiempo laborado
#Hay que calcular el nuevo salario segun el aumento
#Debe funcionar para 5 empleados

salario = int(input("¿Cual es su salario actual?"))

antiguedad = int(input("¿Por cuantos años ha laborado en la empresa?"))

if antiguedad <=5:
    aumento = salario * 0.10
elif antiguedad <=9:
    aumento = salario * 0.15
elif antiguedad <=15:
    aumento = salario * 0.25
else:
    aumento = salario * 0.30

salario2 = salario + aumento

print("El nuevo salario es " ,salario2)
