
secreto = "joker"
respuesta = input("La palabra secreta es : ")
respuesta = respuesta.lower()
def secret(respuesta):
	if (secreto == respuesta):
		print("Bien hecho , Las palabras coinciden")
	else:
		print("Vuelve a intentarlo, adios ")
secret(respuesta)