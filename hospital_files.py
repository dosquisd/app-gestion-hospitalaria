from hospital import Hospital
from numpy import loadtxt


class HospitalFiles:
	@staticmethod
	def read_register(hospital: Hospital) -> Hospital:
		hospital.beds_used = 100


if __name__ == '__main__':
	a = Hospital(300)
	HospitalFiles.read_register(a)

	print(a.beds_used)