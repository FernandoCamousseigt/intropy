"""
Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT
""" 

print("===Atención: Ingrese solamente números enteros=== \n")

P = int(input("Introduzca el precio de suscripción: "))
Unormal = int(input("Introduzca el número de usuarios Normales:  "))
Upremium = int(input("Introduzca el número de usuarios Premium:  "))
GT = int(input("Introduzca el Gasto Total: "))

utilidades = P*Unormal + P*1.5*Upremium - GT

print("El valor de las utilidades esperadas es = {}".format(utilidades))