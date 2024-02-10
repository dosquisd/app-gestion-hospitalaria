from medical_history import MedicalHistory

class Hospital:
	def __init__(self, nums_beds: int) -> None:
		self.num_beds: int = nums_beds
		self.beds_used: int = 0
		self.medical_histories: list[MedicalHistory] = []

	def add_medical_history(self) -> None:
		self.medical_histories.append(MedicalHistory())
		self.medical_histories[0].input()
	
	def search_medical_history(self, document: str) -> int | None:
		for i, medical_history in enumerate(self.medical_histories):
			if medical_history.patient.document == document:
				return i
		return None
		
	def delete_medical_history(self, document: str) -> MedicalHistory | None:
		index: int | None = self.search_medical_history(document)
		if index is None:
			print('Paciente no encontrado')
			return None
		
		print(f'El paciente con documento {document}, ha sido eliminado')
		return self.medical_histories.pop(index)
