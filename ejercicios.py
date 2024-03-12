precio = int(input("ingrese el precio"))
def leer_edad():
    edad = int(input("ingrese edad"))
    while True:
        if edad >= 5:
            return edad
        else:
            print("entrada valida desde los 4 años")
edad1 = leer_edad()
if edad1 in range(15, 20) or edad1 in range(45, 67):
    descuento = 25
elif edad1 > 66 or edad1 in range(5, 15):
    descuento = 35
elif edad1 in range(20, 45):
    descuento = 10
def calcular_descuento(entrada1):
    return (entrada1 / 100) * precio
print(f"precio original {precio}")
print(f"precio descongtado {precio - calcular_descuento(descuento)}")


    

