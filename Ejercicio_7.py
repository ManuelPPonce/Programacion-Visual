# ---diccionarios --
participantes = {
				 'Nombre': 'Manuel', 
				 'Edad' : 20 ,
				 'Cursos': ['Python ' , 'React ' , ' Django'],
				 }
print (participantes ['Nombre'])
print (participantes ['Edad'])
print (participantes ['Cursos'])

participantes['telegono'] = 9811031944
participantes['ocupacion'] = 'Developer'

print("==========")
print(participantes)

jugador = {}

jugador['nickname'] = 'FunrryMonster'
jugador['score'] = 0

print (jugador)

jugador['score'] = 60
print("El score actual de el jugador " + jugador ['nickname'] + " es " + str (jugador['score']))

avengers = {
	'cap': {
		'name': 'Steve',
		'lastname': 'Roger',
		'avenger_name':'Capitan America',
		},
	'stark': {
		'name': 'Anthony Edward',
		'lastname': 'Stark',
		'avenger_name':'Iroman',

	},
	'MrGreen' : {
		'name': 'Bruce',
		'lastname': 'Banner',
		'avenger_name':'Hulk',

	}	

}

for username , avenger_info in avengers.items():
	print('\n Username ' + username )
	fullname = avenger_info['name'] + " " + avenger_info['lastname']
	avenger_name = avenger_info['avenger_name']

	print("\t Nombre real " + fullname)
	print ("\t Nombre vengador" + avenger_name)

