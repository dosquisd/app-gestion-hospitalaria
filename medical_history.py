from patient import Patient
from valid_inputs import valid_two_options, valid_int_greater_than_0

class MedicalHistory:
	def __init__(self, *, admitted: bool | None = None,
				bed: bool | None = None, discharged: bool | None = None,
				nums_days_stay: int | None = None) -> None:
		
		self.patient: Patient = Patient()
		self.admitted: bool | None = admitted
		self.bed: bool | None = bed
		self.discharged: bool | None = discharged
		self.nums_days_stay: int | None = nums_days_stay
		
	def input(self, available_beds: int) -> None:
		"""Ingresa los datos del historial medico desde consola"""
		self.patient.input()
		print()

		self.admitted = valid_two_options('* ¿El paciente ha sido admitido previamente? [y/n]: ', ('y', 'n')) == 'y'
		if not self.admitted:
			return None
		
		self.discharged = valid_two_options('* ¿A el paciente ya se le dio el alta en este servicio? [y/n]: ', ('y', 'n')) == 'y'
		self.bed = valid_two_options('* ¿El paciente ocupa una cama? [y/n]: ', ('y', 'n')) == 'y'

		if self.bed:
			self.nums_days_stay = valid_int_greater_than_0('* Días de estancia: ')

		if self.discharged:
			self.bed = None

		if self.bed and available_beds == 0:
			print('No hay camas disponibles para admitir al paciente')
			self.admitted = False
			self.discharged = None
			self.bed = None
			self.nums_days_stay = None

		return None
		
	def __str__(self) -> str:
		output: str = str(self.patient)
		output += f"\n\n* ¿Paciente admitido?: {'Sí' if self.admitted else 'No'}\n"
		
		output += '* ¿Paciente dado de alta?: '
		if self.discharged is None:
			output += 'No aplica'
		else:
			output += 'Sí' if self.discharged else 'No'
		
		output += '\n* ¿Paciente ocupa una cama?: '
		if self.bed is None:
			output += 'No aplica'
		else:
			output += 'Sí' if self.bed else 'No'

		output += f"\n* Días de estancia: {'No aplica' if self.nums_days_stay is None else self.nums_days_stay}"
		
		return output
