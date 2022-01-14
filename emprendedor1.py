"""" 
P es precio p
U es numero usuarios
GT es gastos totales
"""

P = int(input("Ingrese el precio de la suscripción \n > "))
U = int(input("Ingrese el número de usuarios  \n > "))
GT= int(input("Ingrese gastos totales  \n > "))

utilidad = P * U - GT

print(f"La utilidad es: ${utilidad}.")
