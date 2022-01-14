"""
Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número
de usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del
año anterior Uanterior, todo esto mediante input(). El programa debe calcular las
utilidades actuales y mostrar la razón entre las utilidades actuales y las del año
anterior con dos decimales.
"""

print("===Atención: Ingrese solamente números enteros=== \n")

P = int(input("Introduzca el precio de suscripción: "))
U = int(input("Introduzca el número de usuarios:  "))
GT = int(input("Introduzca el Gasto Total: "))
Uanterior = int(input("Introduzca Utilidades del año anterior: "))

utilidades = P*U - GT

ratio = utilidades/Uanterior

print("El valor de las utilidades esperadas es = {}".format(utilidades))