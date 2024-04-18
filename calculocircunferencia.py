import math

def calcular_circunferencia(radio):
	pi = round(math.pi, 6)
	circunferencia = 2 * pi * radio
	return circunferencia
radio = float(input("Introduce el radio del circulo: ")

circunferencia = calcular_circunferencia(radio)

print("La circunferencia del circulo con radio", radio, "es:", circunferencia)
