from date import Date
from valid_inputs import *
import os

class Patient:
	def __init__(
			self, document: str | None = None, full_name: str | None = None, sex: str | None = None,
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
		"""Entrada de datos de un paciente desde consola"""
		print('* Datos del paciente:')
		self.document = input('\tDocumento: ')
		self.full_name = input('\tNombre: ')
		self.sex = valid_two_options('\tSexo [m/f]: ', ('m', 'f'))
		self.birthday.input('\tFecha de nacimiento')

		print('* Signos vitales:')
		self.blood_press = self.__valid_blood_press('\tPresión arterial [Systólica/Diastólica mmHg]: ')
		self.temperature = valid_float('\tTemperatura [°C]: ')
		self.o2_saturation = valid_float('\tSaturación de O2 [%]: ')
		self.frequency = valid_float('\tFrecuencia respiratoria [bpm]: ')

		self.lab_results = input('* Resultados de exámenes de laboratorio: ')
		self.evolution_notes = input('* Notas de evolución: ')
		self.prescription_drugs = input('* Medicamentos formulados: ')
		self.chronic_disease = valid_two_options('¿Presenta alguna enfermedad crónica? [y/n]: ', ('y', 'n')) == 'y'
		self.diagnostic_imgs = self.__valid_diagnostic_img('Escriba el nombre del archivo (con la extensión) para imágenes diagnósticas: ')

	@staticmethod
	def __valid_blood_press(msg: str) -> str:
		"""Método que valida que la presión arterial esté en el formato sytólica/diastólica"""
		while True:
			try:
				temp: str = input(msg)
				systolic, diastolic = [int(press_value) for press_value in temp.split('/')]
			except ValueError:
				continue

			if systolic < 0 or diastolic < 0:
				continue

			return temp

	@staticmethod
	def __valid_diagnostic_img(msg: str) -> str:
		"""Método que valida que esté bien ingresada la imagen diagnostica"""
		diagnostic_imgs: str = r'files\diagnostics_images'
		if not os.listdir(diagnostic_imgs): # Si la carpeta está vacía
			return ''

		while True:
			img: str = input(msg)
			diagnostic_img_path: str = fr'{diagnostic_imgs}\{img}'
			if not (os.path.exists(diagnostic_img_path) and img):
				print(f'No existe la imagen en la dirección: {diagnostic_img_path}')
				continue
			return img


	def __str__(self) -> str:
		return f"""* Datos del paciente
	Documento: {self.document}
	Nombre: {self.full_name}
	Sexo: {'Hombre' if self.sex == 'm' else 'Mujer'}
	Fecha de nacimiento: {self.birthday}
* Signos vitales
	Presión arterial: {self.blood_press} mmHg
	Temperatura: {self.temperature} °C
	Saturación de O2: {self.o2_saturation}%
	Frecuencia respiratoria: {self.frequency} bpm

* Resultados de exámenes de laboratorio: {self.lab_results}
* Notas de evolución: {self.evolution_notes}
* Medicamentos formulados: {self.prescription_drugs}
* ¿Presenta alguna enfermedad crónica?: {'Sí' if self.chronic_disease else 'No'}
* Imágenes diagnósticas: {self.diagnostic_imgs if self.diagnostic_imgs is not None else 'No aplica'}"""
