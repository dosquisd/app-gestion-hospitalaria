from date import Date
from valid_inputs import *

class Patient:
	def __init__(self, document: str | None = None, full_name: str | None = None, sex: str | None = None,
			  	blood_press: float | None = None, temperature: float | None = None, o2_saturation: float | None = None,
				frequency: float | None = None, evolution_notes: str | None = None, diagnostic_imgs: str | None = None,
				lab_results: str | None = None, prescription_drugs: str | None = None, chronic_disease: bool | None = None) -> None:
		self.document: str | None = document
		self.full_name: str | None = full_name
		self.sex: str | None = sex
		self.birthday: Date = Date()
		self.blood_press: float | None = blood_press
		self.temperature: float | None = temperature
		self.o2_saturation: float | None = o2_saturation
		self.frequency: float | None = frequency
		self.evolution_notes: str | None = evolution_notes
		self.diagnostic_imgs: str | None = diagnostic_imgs
		self.lab_results: str | None = lab_results
		self.prescription_drugs: str | None = prescription_drugs
		self.chronic_disease: bool | None = chronic_disease

	def input(self) -> None:
		print('* Datos del paciente:')
		self.document = input('\tDocumento: ')
		self.full_name = input('\tNombre: ')
		self.sex = valid_two_options('\tSexo [m/f]: ', ('m', 'f'))
		self.birthday.input('\tFecha de nacimiento')

		print('* Signos vitales:')
		self.blood_press = valid_float('\tPresión arterial: ')
		self.temperature = valid_float('\tTemperatura: ')
		self.o2_saturation = valid_float('\tSaturación de O2: ')
		self.frequency = valid_float('\tFrecuencia respiratoria: ')

		self.evolution_notes = input('* Notas de evolución: ')
		self.lab_results = input('* Resultados de exámenes de laboratorio: ')
		self.prescription_drugs = input('* Medicamentos formulados: ')
		self.chronic_disease = valid_two_options('¿Presenta alguna enfermedad crónica? [y/n]: ', ('y', 'n')) == 'y'
		self.diagnostic_imgs = input('Escriba el nombre del archivo (con la extensión) para imágenes diagnósticas: ')

	def __str__(self) -> str:
		return f"""* Datos del paciente
	Documento: {self.document}
	Nombre: {self.full_name}
	Sexo: {'Hombre' if self.sex == 'm' else 'Mujer'}
* Signos vitales
	Presión arterial: {self.blood_press}
	Temperatura: {self.temperature}
	Saturación de O2: {self.o2_saturation}
	Frecuencia respiratoria: {self.frequency}

* Notas de evolución: {self.evolution_notes}
* Resultados de exámenes de laboratorio: {self.lab_results}
* Medicamentos formulados: {self.prescription_drugs}
* ¿Presenta alguna enfermedad crónica?: {'Sí' if self.chronic_disease else 'No'}
* Imágenes diagnósticas: {self.diagnostic_imgs}"""
	

if __name__ == '__main__':
	a = Patient()
	a.input()
	print(f'\n\n\n{a}')