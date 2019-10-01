
print ('Programa de opereaciones aritmeticas')

operacion = input ("Teclee la operacion: ")
num1 = int(input ("Teclee el primer numero: "))
num2 = int(input ("Teclee el segundo numero: "))

if operacion == "suma":
	resultado = num1 + num2 
elif operacion == "resta":
	resultado = num1 - num2
elif operacion == "division":
	resultado = num1 / num2
else:
	resultado = num1 * num2

print("El resultado de la operacion " + str(operacion) + " es " + str(resultado))
#print ("El resultado de la operacion {0} es {1} ").format(operacion,resultado)