# ===========================================
# CONVERSOR DE MONEDAS - VERSIÓN 3
# Autor(a): ALVARO YPORRE ALEJOS
# ===========================================

soles = float(input("Ingrese la cantidad en soles: "))

print("1. Dólares")
print("2. euros")
print("3. libras esterlinas")

opcion = input("Selecione una opción: ")

if opcion == "1":
    dolares = soles/3.60
    print("Equivale a ", dolares, "dolares.")
    
elif opcion == "2":
    euros = soles/4.20
    print("Equivale a ", euros, "euros.")

elif opcion=="3":
    libras = soles/4.80
    print("Equivale a ", libras, "libras.")

else:
    print("Opción no válida")
