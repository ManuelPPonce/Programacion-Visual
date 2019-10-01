
cars = ['audi','bmw','subaru','toyota']

for car in  cars:
	#print(car)
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())
respuesta = 17
if respuesta != 42:
	print("Esta respuesta no es correcta")	


usuarios_baneados = ['Pepe Charly', 'Jose','Maria']

# py2.7 raw_input
# p3.X input()

name = input ('Ingresa tu nombre de usuario: ')

if name not in usuarios_baneados:
	print(name.title() + " No esta baneado. ")
else:
	print(name.title() + " Si esta baneado. ")

#Validar si eres mayor de edad (18) puedes votar

edad = int(input('Ingresa tu edad : '))

if edad < 18:
	print ("No puedes votar , Eres menor de edad ")
else:
	print("Puedes votar")

''''
#if - else - else 
la entrada para menores de 4 años es gratuita.
la entrada para cualquier persona entre las edades de 4 y 18 años es de $50 
la entrada para cualquiero persona  mayor de 18 añow es de $100
'''
edad1 = int (input ('Ingresa tu edad : '))

if edad1 < 4:
	print ("La entrada es gratuita")
elif edad1 <18:
	print ("La entrada tiene un precio de $50")
else:
	print ("La entrada tiene un precio de $100")

#Optimizado
edad2 = int (input ('Ingresa tu edad : '))

if edad2 < 4:
	precio = 0
elif edad2 < 18:
	precio = 50
else:
	precio = 100

print ("La entrada te va a cosatar $" + str (precio))



