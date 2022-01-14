""" 
Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades
del proyecto

P es precio p
U es numero usuarios
GT es Gasto total
"""
print("===Atención: Ingrese solamente números enteros=== \n")

P = int(input("Introduzca el precio de suscripción: "))
U = int(input("Introduzca el número de usuarios:  "))
GT = int(input("Introduzca el Gasto Total: "))

utilidades = P * U - GT

print("El valor de las utilidades esperadas es = {}".format(utilidades))

#option2: print(f"La utilidad es: ${utilidad}.")

