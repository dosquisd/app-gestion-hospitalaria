from menus import *
from hospital import Hospital
from hospital_files import HospitalFiles
from os import system
from time import sleep

def manage_medical_history(hospital: Hospital) -> None:
	while True:
		op: int = manage_medical_history_menu()
		print('\n')

		match op:
			case 1:
				add_patient_menu()
				print()
				hospital.add_medical_history()
				print('\n')
				
			case 2:
				search_patient_menu()
				document: str = input('\nIngrese el documento a buscar: ')

				index: int = hospital.search_medical_history(document)
				if index is None:
					print('Paciente no encontrado\n\n') 
					continue

				print(f'\n{hospital.medical_histories[index]}\n')

			case 3:
				delete_patient_menu()
				document: str = input('\nIngrese el documento a eliminar: ')
				print()

				hospital.delete_medical_history(document)
				print('\n')

			case 4:
				print('Volviendo al menú principal...')
				sleep(1)
				break
			
			case _:
				print(f'\nOpción {op} inválida. Intente de nuevo')
				sleep(1.5)
				system('cls')


def generate_reports(hospital: Hospital) -> None:
	while True:
		op: int = generate_reports_menu()
		print('\n')

		match op:
			case 1:
				occupancy_rate_menu()
				print(f'\nEl porcentaje de ocupación de las camas es: {hospital.get_occupancy_rate():.2%}\n')
			
			case 2:
				average_stay_service_menu()
				print(f'\nEl promedio de estancia por servicio es: {hospital.get_average_stay_per_service():.2} días\n')
			
			case 3:
				admissions_and_discharges_menu()
				print(f'\nCantidad de pacientes admitidos: {hospital.get_admitted()} pacientes')
				print(f'Cantidad de pacientes dados de alta: {hospital.get_discharged()} pacientes\n')

			case 4:
				patients_chronic_diseases_menu()
				print()
				hospital.get_patients_chronic_disease()
				print()

			case 5:
				medicine_prescription_menu()
				print('\nListado de los medicamentes prescritos a cada paciente:\n')
				print('Número de documento. Medicamente prescritos')
				hospital.get_prescription_drugs()
				print()
			
			case 6:
				print('Volviendo al menú principal...')
				sleep(1)
				break
			
			case _:
				print(f'\nOpción {op} inválida. Intente de nuevo')
				sleep(1.5)
				system('cls')

def main() -> None:
	hospital: Hospital = Hospital(300)
	HospitalFiles.read_register(hospital)

	while True:
		op: int = main_menu()
		print('\n')

		match op:
			case 1:
				system('cls')
				manage_medical_history(hospital)
				print('\n\n')
				system('cls')
			
			case 2:
				system('cls')
				generate_reports(hospital)
				system('cls')
			
			case 3:
				for i, medical_history in enumerate(hospital.medical_histories):
					print(f'{i+1}.')
					print(f'{medical_history}\n')

			case 4:
				system('cls')
				break
			
			case _:
				print(f'\nOpción {op} inválida. Intente de nuevo')
				sleep(1.5)
				system('cls')

	HospitalFiles.load_register(hospital)
	print('¡Que tenga buen resto de día!')
