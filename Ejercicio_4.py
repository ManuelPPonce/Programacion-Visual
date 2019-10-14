#Validar si eres mayor de edad (18) puedes votar

edad = int(input('Ingresa tu edad : '))

if edad < 18:
	print ("No puedes votar , Eres menor de edad ")
else:
	print("Puedes votar")
