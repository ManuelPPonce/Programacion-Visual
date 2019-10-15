"""
5.- Escribir un programa llamado diccionario.py que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

Nombre = input ("Nombre : ")
Edad = int(input ("Edad : "))
Direccion = input("Ingresa tu dirección :")
Telefono = input("Telefono: ")

diccionario = {
		
	
	"Nombre" : Nombre,
	"Edad":Edad,
	"Direccion": Direccion,
	"Telefono":Telefono,
	

}

print(diccionario["Nombre"],"Tiene ",diccionario["Edad"],"años, vive en ",diccionario["Direccion"] ,"y su numero de telefono es : " ,diccionario["Telefono"])