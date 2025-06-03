# Realizar el siguiente ejercicio con la instrucción if..elif..else. El almacén “viste con estilo” requiere de su ayuda para construir un programa que permita calcular la talla de ropa acorde a la altura ingresada así (la altura debe capturarse en centímetros):
# Rango de estaturas de acuerdo con la talla.
# Si la altura es menor o igual a 150 cm, la talla asignada es S.
# Si la altura es mayor a 150 cm y menor a 170 cm, corresponde la talla M.
# Si la altura es mayor o igual a 170 cm y menor a 180 cm, se asigna la talla L.
# Finalmente, si la altura es mayor o igual a 180 cm, la talla es XL.
talla = "" # Inicializacion de la variable como una cadena vacia.
# Solicitar la talla del usuario.
altura = float(input("ingrese su altura en centimetros: "))
# Determinar la talla del usuario usando if..elif..else.
if altura <= 150:
    talla = "S"
elif altura > 150 and altura < 170:
    talla = "M"
elif altura >= 170 and altura < 180:
    talla = "L"
else:
    talla = "XL"
# Mostrar la talla correspondiente
print(f"La talla correspondiente a su altura es: {talla}")