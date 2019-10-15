peso = int(input("Ingresa tu peso en kg : "))

estatura = float(input("Ingresa tu estatura en metros : "))

estaturaf = estatura*estatura

imc = peso/estaturaf

imf = round(imc,2)

if (imf <= 15):
	print("Tu imc es :", imf ,"por lo tanto tienes --> Delgadez muy severa")
elif(imf < 15.9 and imf > 15):
	print("Tu imc es :", imf ,"por lo tanto tienes --> Delgadez severa")
elif(imf > 15.9 and imf < 18.4):
	print("Tu imc es :", imf ,"por lo tanto tienes --> Delgadez")
elif(imf < 24.9 and imf >18.4):
	print("Tu imc es :", imf ,"por lo tanto tienes --> Peso saludable")
elif (imf < 29.9 and imf > 24.9 ):
	print("Tu imc es :", imf ,"por lo tanto tienes --> Sobrepeso")
elif(imf < 34.9 and imf > 29.9):
	print("Tu imc es :", imf ,"por lo tanto tienes --> Obesidad Moderada")
elif(imf > 34.9 and imf < 39.9):
	print("Tu imc es :", imf ,"por lo tanto tienes --> Obesidad severa")
else:
	print("Tu imc es :", imf ,"por lo tanto tienes --> Obesidad Morbida")
