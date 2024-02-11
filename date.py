from dataclasses import dataclass

@dataclass
class Date:
	day: int = 0
	month: int = 0
	year: int = 0

	def __str__(self) -> str:
		return f'{self.day}/{self.month}/{self.year}'
	
	def input(self, message: str) -> None:
		day: int = 0
		month: int = 0
		year: int = 0

		while not Date.valid_date(day, month, year):
			date_str: str = input(f'{message} [dd/mm/aaaa]: ')

			try:
				day, month, year = [int(temp) for temp in date_str.split('/')]
			except ValueError:
				print('Agregue las fechas en el formato [dd/mm/aaaa]\n')
				continue

			if not Date.valid_date(day, month, year):
				print('Fecha inválida')

		self.day = day
		self.month = month
		self.year = year

	def input_date(self, date_str: str) -> None:
		# Ingresa la fecha en el formato [dd/mm/aaaa]
		try:
			day, month, year = [int(temp) for temp in date_str.split('/')]
		except ValueError:
			return
		
		self.day = day
		self.month = month
		self.year = year

	@staticmethod
	def __is_leap_year(year: int) -> bool:
		return (year % 400 == 0 or year % 4 == 0) and (year % 100 != 0)
	
	@staticmethod
	def valid_date(day: int, month: int, year: int) -> bool:
		# Validar que las fechas de por sí estén bien
		if month < 1 or month > 12:
			return False
		
		if day < 0 or day > 31:
			return False
		
		if month in (1, 3, 5, 7, 8, 10, 12):
			return day <= 31
		
		if month in (4, 6, 9, 11):
			return day <= 30
		
		if Date.__is_leap_year(year):
			return day <= 29
		
		return day <= 28

if __name__ == '__main__':
	a = Date()
	a.input('Fecha de nacimiento')

	print(f'\n\n\n{a}')