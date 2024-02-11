def valid_float(msg: str) -> float:
	while True:
		try:
			return float(input(msg))
		except ValueError:
			print('Ingrese el valor numérico correctamente')

def valid_two_options(msg: str, options: list | tuple) -> str:
	while True:
		temp = input(msg).lower()
		if temp in options:
			return temp
		
def valid_input_menus() -> int:
	while True:
		try:
			return int(input('Ingrese el número de la opción: '))
		except ValueError:
			print('Ingrese tipo de dato numérico')

def valid_int_greater_than_0(msg: str) -> int:
	while True:
		try:
			temp = int(input(msg))
			if temp >= 0:
				return temp
		except ValueError:
			print('Ingrese un número entero')