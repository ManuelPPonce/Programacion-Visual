#funciones

#def nombreDeFuncion():
#	"" Esta funcion hace ...""
#	passs

"""
Realiza una función que imprima "Hola Mundo"
Realiza una función que sume dos números pasados por parámetros
Realiza una función que indique si un número pasado por parámetro es par o impar.
Crea una función que calcule el factorial de un número pasado por párametro
Crea una función que dados dos números mostrará todos los números que hay entre ellos.

"""

#Funcion que dice "Hola Mundo"
def holaMundo():
	print("Hola Mundo")


holaMundo()



def saludarUser(username):
	print("Hola" + username)

saludarUser('noobmaster')

#Funcion que sume dos numeros 

summ = int()
a = int(input())
b = int(input())
def Sumando(a = 0 , b = 0):

	summ = a + b
	print ('El total de la suma es : ' + str(summ))
	

Sumando(a,b)

#Par e impar

num1 = int(input())

def par_impar(num1 = 0):

	if(num1 % 2 == 0):
		print ('El numero ' + str(num1) + ' es par : ' )
	else:
		print ('El numero ' + str(num1) + ' es impar : ')


par_impar(num1)


#Factorial


fac =int(input())
def factorial(fac = 0):

	total = 1
	for i in range(1,fac+1):
		total=total*i
	print(total)



factorial(fac)
#Crea una función que dados dos números mostrará todos los números que hay entre ellos.
x = int(input())
y = int(input())
def entre_numeros(x = 0 , y = 0 ):
	for i in range(x+1,y):
		print(i)
entre_numeros(x,y)