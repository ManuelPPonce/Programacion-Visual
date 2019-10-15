#Escribir un programa llamado materias.py que pida el numero de asignaturas que se desean agregar, 
#Que pida el nombre de las asignaturas dadas y las almacene en una lista y la muestre por pantalla
Num_Materias = int(input("Cuantas materias deseas introducir : "))
asignaturas = []

for i in range(0,Num_Materias):
	print("Dame la (",i+1,") asignatura : " , end=" ")
	materia = input()
	asignaturas.append(materia)

print("Tus materias son  : ",asignaturas)

#for i in asignaturas:
#	print( i,end=",")

print(" ")
	