from medical_history import MedicalHistory, Patient

class Hospital:
	def __init__(self, nums_beds: int) -> None:
		self.num_beds: int = nums_beds
		self.beds_used: int = 0
		self.medical_histories: list[MedicalHistory] = []

	def add_medical_history(self) -> None:
		"""Agrega un historial medico"""
		self.medical_histories.append(MedicalHistory())
		self.medical_histories[-1].input(self.num_beds - self.beds_used)

		if self.medical_histories[-1].bed:
			self.beds_used += 1
	
	def search_medical_history(self, document: str) -> int | None:
		"""Busca un historial medico dado un documento"""
		for i, medical_history in enumerate(self.medical_histories):
			if medical_history.patient.document == document:
				return i
		return None
		
	def delete_medical_history(self, document: str) -> MedicalHistory | None:
		"""Elimina un historial medico dado un documento"""
		index: int = self.search_medical_history(document)
		if index is None:
			print('Paciente no encontrado')
			return None
		
		print(f'El paciente con documento {document}, ha sido eliminado')
		temp: MedicalHistory = self.medical_histories.pop(index)
		if temp.bed:
			self.beds_used -= 1

		return temp

	def get_occupancy_rate(self) -> float:
		"""Calcula el porcentaje de ocupación de las camas del hospital"""
		return self.beds_used / self.num_beds
	
	def get_average_stay_per_service(self) -> float:
		"""Calcula el promedio de los días de estadía de los pacientes por servicio"""
		total_days: int = 0
		n_patients: int = 0

		for medical_history in self.medical_histories:
			if (days:=medical_history.nums_days_stay) is None:
				continue
			total_days += days
			n_patients += 1
		
		try:	
			return total_days / n_patients
		except ZeroDivisionError:
			return 0.0

	def get_admitted(self) -> int:
		"""Retorna el total de las pacientes admitidas en el servicio"""
		return sum([medical_history.admitted for medical_history in self.medical_histories])

	def get_discharged(self) -> int:
		"""Retorna el total de las pacientes que fueron dadas de alta en el servicio"""
		return sum([medical_history.discharged for medical_history in self.medical_histories if medical_history.discharged is not None])

	def get_patients_chronic_disease(self) -> None:
		"""Imprime la lista de pacientes con enfermedad cronica"""
		list_chronic_disease: list[Patient] = [medical_history.patient for medical_history in self.medical_histories if medical_history.patient.chronic_disease]
		print(f'Número de pacientes con enfermedades crónicas: {len(list_chronic_disease)}\n')
		
		print(f'Número de documento - Nombre completo')
		for i, patient in enumerate(list_chronic_disease):
			print(f'{i+1}. {patient.document} - {patient.full_name}')

	def get_prescription_drugs(self) -> None:
		"""Imprime el listado de los pacientes con las medicinas prescritas"""
		for i, medical_history in enumerate(self.medical_histories):
			print(f'{i+1}. {medical_history.patient.document}. {medical_history.patient.prescription_drugs}')
