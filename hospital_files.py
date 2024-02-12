from hospital import Hospital, MedicalHistory
from date import Date
import pandas as pd
import numpy as np

class HospitalFiles:
	@staticmethod
	def load_register(hospital: Hospital) -> None:
		"""Ingresa los datos en patients.csv"""
		df_patients: pd.DataFrame = pd.DataFrame(columns = [
			'Document', 'Full Name', 'Sex', 'Birth Day', 'Blood Press', 'Temperature',
			'O2 Saturation', 'Breathing Rate', 'Evolution Notes', 'Lab Results',
			'Prescription Drugs', 'Diagnostic Images', 'Chronic Disease', 'Admitted',
			'Discharged', 'Bed', 'Stay Days'
		])

		for i, m_h in enumerate(hospital.medical_histories):
			df_patients.loc[i] = [
				m_h.patient.document, m_h.patient.full_name, m_h.patient.sex,
				m_h.patient.birthday, m_h.patient.blood_press, m_h.patient.temperature,
				m_h.patient.o2_saturation, m_h.patient.frequency, m_h.patient.evolution_notes,
				m_h.patient.lab_results, m_h.patient.prescription_drugs, m_h.patient.diagnostic_imgs,
				m_h.patient.chronic_disease, m_h.admitted, m_h.discharged, m_h.bed, m_h.nums_days_stay
			]

		df_patients.fillna('?', inplace=True)
		df_patients.to_csv(r'files\patients.csv', sep=';')

	@staticmethod
	def read_register(hospital: Hospital) -> None:
		"""Lee los datos de patients.csv"""
		try:
			df_patients = pd.read_csv(r'files\patients.csv', delimiter=';')
		except pd.errors.EmptyDataError:
			return None

		for i in range(len(df_patients)):
			hospital.medical_histories.append(MedicalHistory())
			hospital.medical_histories[-1].patient.document = str(df_patients['Document'][i])
			hospital.medical_histories[-1].patient.full_name = df_patients['Full Name'][i]
			hospital.medical_histories[-1].patient.sex = df_patients['Sex'][i]
			hospital.medical_histories[-1].patient.birthday = Date()
			hospital.medical_histories[-1].patient.birthday.input_date(df_patients['Birth Day'][i])

			hospital.medical_histories[-1].patient.blood_press = df_patients['Blood Press'][i]
			hospital.medical_histories[-1].patient.temperature = float(df_patients['Temperature'][i])
			hospital.medical_histories[-1].patient.o2_saturation = float(df_patients['O2 Saturation'][i])
			hospital.medical_histories[-1].patient.frequency = float(df_patients['Breathing Rate'][i])
			hospital.medical_histories[-1].patient.evolution_notes = df_patients['Evolution Notes'][i]
			hospital.medical_histories[-1].patient.lab_results = df_patients['Lab Results'][i]
			hospital.medical_histories[-1].patient.prescription_drugs = df_patients['Prescription Drugs'][i]
			hospital.medical_histories[-1].patient.diagnostic_imgs = df_patients['Diagnostic Images'][i] if df_patients['Diagnostic Images'][i] != '?' else None
			hospital.medical_histories[-1].patient.chronic_disease = bool(df_patients['Chronic Disease'][i])
			hospital.medical_histories[-1].admitted = HospitalFiles.to_bool(df_patients['Admitted'][i])
			hospital.medical_histories[-1].discharged = HospitalFiles.to_bool(df_patients['Discharged'][i]) if df_patients['Discharged'][i] != '?' else None
			hospital.medical_histories[-1].bed = HospitalFiles.to_bool(df_patients['Bed'][i]) if df_patients['Bed'][i] != '?' else None
			hospital.medical_histories[-1].nums_days_stay = int(df_patients['Stay Days'][i]) if df_patients['Stay Days'][i] != '?' else None

			if (hospital.num_beds == hospital.beds_used) and hospital.medical_histories[-1].bed:
				hospital.medical_histories[-1].admitted = False
				hospital.medical_histories[-1].discharged = None
				hospital.medical_histories[-1].bed = None
				hospital.medical_histories[-1].nums_days_stay = None
			else:
				hospital.beds_used += 1 if hospital.medical_histories[-1].bed else 0

	@staticmethod
	def to_bool(sentence: np.bool_ | str) -> bool:
		"""Convierte los tipos de datos `np.bool_` y `str` a `bool`"""
		if type(sentence) == np.bool_:
			return sentence == np.True_

		return sentence == 'True'
