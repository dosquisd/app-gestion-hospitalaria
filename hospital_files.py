from hospital import Hospital, MedicalHistory
import pandas as pd
import numpy as np

class HospitalFiles:
	@staticmethod
	def load_register(hospital: Hospital) -> None:
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
				m_h.patient.lab_results, m_h.patient.prescription_drugs, HospitalFiles.change_to_nan(m_h.patient.diagnostic_imgs),
				m_h.patient.chronic_disease, m_h.admitted, HospitalFiles.change_to_nan(m_h.discharged), 
				HospitalFiles.change_to_nan(m_h.bed), HospitalFiles.change_to_nan(m_h.nums_days_stay)
			]

		df_patients.to_csv(r'files\patients.csv', sep=';')

	@staticmethod
	def read_register(hospital: Hospital) -> None:
		try:
			df_patients = pd.read_csv(r'files\patients.csv', delimiter=';')
		except pd.errors.EmptyDataError:
			return None

		for i in range(len(df_patients)):
			hospital.medical_histories.append(MedicalHistory())
			hospital.medical_histories[-1].patient.document = df_patients['Document'][i]
			hospital.medical_histories[-1].patient.full_name = df_patients['Full Name'][i]
			hospital.medical_histories[-1].patient.sex = df_patients['Sex'][i]
			hospital.medical_histories[-1].patient.birthday = df_patients['Birth Day'][i]
			hospital.medical_histories[-1].patient.blood_press = df_patients['Blood Press'][i]
			hospital.medical_histories[-1].patient.temperature = df_patients['Temperature'][i]
			hospital.medical_histories[-1].patient.o2_saturation = df_patients['O2 Saturation'][i]
			hospital.medical_histories[-1].patient.frequency = df_patients['Breathing Rate'][i]
			hospital.medical_histories[-1].patient.evolution_notes = df_patients['Evolution Notes'][i]
			hospital.medical_histories[-1].patient.lab_results = df_patients['Lab Results'][i]
			hospital.medical_histories[-1].patient.prescription_drugs = df_patients['Prescription Drugs'][i]
			hospital.medical_histories[-1].patient.diagnostic_imgs = df_patients['Diagnostic Images'][i] if df_patients['Diagnostic Images'][i] is np.nan else None
			hospital.medical_histories[-1].patient.chronic_disease = df_patients['Chronic Disease'][i]
			hospital.medical_histories[-1].admitted = df_patients['Admitted'][i]
			hospital.medical_histories[-1].discharged = df_patients['Discharged'][i] if df_patients['Discharged'][i] is np.nan else None
			hospital.medical_histories[-1].bed = df_patients['Bed'][i] if df_patients['Bed'][i] is np.nan else None
			hospital.medical_histories[-1].nums_days_stay = df_patients['Stay Days'][i] if df_patients['Stay Days'][i] is np.nan else None

			if hospital.medical_histories[-1].bed:
				hospital.beds_used += 1
			
	@staticmethod
	def change_to_nan(value: object) -> object:
		return value if value is not None else np.nan
