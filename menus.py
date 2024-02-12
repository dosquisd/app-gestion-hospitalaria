from valid_inputs import valid_input_menus

def main_menu() -> int:
	print('+------------------------------+')
	print('|     Hospital San Vicente     |')
	print('|        -Menú principal       |')
	print('+------------------------------+')
	print('|1. Gestionar historia clínica |')
	print('|2. Generar Reportes           |')
	print('|3. Enlistar los pacientes     |')
	print('|4. Salir                      |')
	print('+------------------------------+\n')

	return valid_input_menus()

def manage_medical_history_menu() -> int: # Opción 1 del menú principal
	print('+----------------------------+')
	print('| Gestionar historia clínica |')
	print('+----------------------------+')
	print('|1. Agregar paciente         |')
	print('|2. Buscar paciente          |')
	print('|3. Eliminar paciente        |')
	print('|4. Volver al menú principal |')
	print('+----------------------------+\n')

	return valid_input_menus()

def add_patient_menu() -> None:
	print('+----------------------------+')
	print('| Gestionar historia clínica |')
	print('| - Agregar paciente         |')
	print('+----------------------------+')

def search_patient_menu() -> None:
	print('+----------------------------+')
	print('| Gestionar historia clínica |')
	print('| - Buscar paciente          |')
	print('+----------------------------+')
	
def delete_patient_menu() -> None:
	print('+----------------------------+')
	print('| Gestionar historia clínica |')
	print('| - Eliminar paciente        |')
	print('+----------------------------+')

def generate_reports_menu() -> int:
	print('+------------------------------------------------+')
	print('|                Generar reportes                |')
	print('+------------------------------------------------+')
	print('|1. Porcentaje de ocupación                      |')
	print('|2. Promedios de estancia por servicio           |')
	print('|3. Cantidad de admisiones y altas por servicio  |')
	print('|4. Pacientes con enfermedad crónica             |')
	print('|5. Prescripción de medicamentos por servicio    |')
	print('|6. Volver al menú principal                     |')
	print('+------------------------------------------------+\n')

	return valid_input_menus()

def occupancy_rate_menu() -> None:
	print('+---------------------------+')
	print('| Generar reportes          |')
	print('| - Porcentaje de ocupación |')
	print('+---------------------------+')

def average_stay_service_menu() -> None:
	print('+--------------------------------------+')
	print('| Generar reportes                     |')
	print('| - Promedios de estancia por servicio |')
	print('+--------------------------------------+')

def admissions_and_discharges_menu() -> None:
	print('+-----------------------------------------------+')
	print('| Generar reportes  							   |')
	print('| - Cantidad de admisiones y altas por servicio |')
	print('+-----------------------------------------------+')

def patients_chronic_diseases_menu() -> None:
	print('+---------------------------------------+')
	print('| Generar reportes 					   |')
	print('| - Pacientes con enfermedades crónicas |')
	print('+---------------------------------------+')

def medicine_prescription_menu() -> None:
	print('+---------------------------------------------+')
	print('| Generar reportes 							 |')
	print('| - Prescripción de medicamentos por servicio |')
	print('+---------------------------------------------+')
