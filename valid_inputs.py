def valid_float(msg: str) -> float:
	"""Valida que el valor de tipo float, sea exclusivamente float y así no se corrompa el programa"""
	while True:
		try:
			return float(input(msg))
		except ValueError:
			print('Ingrese el valor numérico correctamente')

def valid_two_options(msg: str, options: list | tuple) -> str:
	"""Valida que una entrada se encuentre exclusivamente entre las opciones disponibles"""
	while True:
		temp = input(msg).lower()
		if temp in options:
			return temp
		
def valid_input_menus() -> int:
	"""Valida todas las entradas de los menus. Se encarga de ver que el tipo de dato sea exclusivamente enteros"""
	while True:
		try:
			return int(input('Ingrese el número de la opción: '))
		except ValueError:
			print('Ingrese tipo de dato numérico')

def valid_int_greater_than_0(msg: str) -> int:
	"""Valida que un número de tipo entero sea mayor o igual a 0"""
	while True:
		try:
			temp = int(input(msg))
			if temp >= 0:
				return temp
		except ValueError:
			print('Ingrese un número entero')