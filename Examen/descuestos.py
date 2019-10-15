
cantidad = float(input("Ingresa el importe del producto $"))
descuento = float(input("Ingresa el descuento del producto %"))

def des(descuento,cantidad):

	datos = {
	"Descuento":descuento,
	"Importe":cantidad

	}

	aplicar =  cantidad*descuento/100

	resultado = cantidad - aplicar

	print("El importe del producto es $",cantidad," y el descuento es :",descuento)
	print("El total es : ", resultado)

des(descuento,cantidad)