import math
from datetime import datetime
fecha= datetime.now().strftime("%Y-%m-%d")
ancho_neumatico=float(input("Enter the tire width in mm (ej 205): "))
aspect_neumatico=float(input("Enter the aspect ratio of the tire (ej 50):"))
diametro=float(input("Enter the wheel diameter in inches (ej 15):"))
#formula is:
# v = (pi * w^2 * a * (w*a + 2540*d)) / 10,000,000,000
# Where:
# v = volume in liters
# pi = math.pi
# w = tire width
# a = aspect ratio
# d = wheel diameter
# We perform the mathematical calculation according to the formula.7
# We convert the diameter of the wheel from inches to mm (1 inch = 25.4 mm)
diametro_rueda_mm = diametro * 25.4
volumen = (math.pi * (ancho_neumatico**2) * aspect_neumatico * (ancho_neumatico * aspect_neumatico + 2540 * diametro)) / 10000000000
volumen_redondeado=round(volumen, 2)
#calculate price based on the information entered
precio = 0
if ancho_neumatico == 185 and aspect_neumatico == 50 and diametro == 14:
    precio = 120
elif ancho_neumatico == 205 and aspect_neumatico == 60 and diametro == 15:
    precio = 150
elif ancho_neumatico == 225 and aspect_neumatico == 65 and diametro == 17:
    precio = 180
else:
    precio = 100
with open("volumes.txt", "a") as archivo:
    archivo.write(f"{fecha}, {int (ancho_neumatico)}, {int(aspect_neumatico)}, {int(diametro)}, {volumen_redondeado}\n")
print(f"\n The approximate volume is{volumen_redondeado} liters.")
print(f"The simulated price of this tire is: ${precio}")
print(f"The data is saved in the file volumes.txt")