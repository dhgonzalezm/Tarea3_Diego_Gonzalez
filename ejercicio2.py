# Realizar el siguiente ejercicio con la instrucción if..else Construir un programa que permita verificar si una persona es mayor de edad. Para esto debe solicitar el año de nacimiento, calcular la edad y si la edad es mayor o igual a 18 mostrar un mensaje por consola que indique que la persona es mayor de edad, de lo contrario que muestre un mensaje indicando que es menor de edad.
# Solicitar el añp de nacimiento al usuario.
from datetime import date
# "datetime" es un modulo que nos permite trabajar con fechas y horas.
# "date" importamos date del modulo datetime para obtener la fecha actual.
año_nacimiento = int(input("Ingrese su año de nacimiento (####) "))
mes_nacimiento = int(input("Ingrese su mes de nacimiento (##) "))
dia_nacimiento = int(input("Ingrese su dia de nacimiento (##) "))
# "año_nacimiento" es la variable que almacena el año de nacimiento ingresado por el usuario.
# "mes_nacimiento" es la variable que almacena el mes de nacimiento ingresado por el usuario.
# "dia_nacimiento" es la variable que almacena el dia de nacimiento ingresado por el usuario.
# "input()" Este nos permite mostrar un mensaje en pantalla y que el usuario ingrese algun dato.
# "int()" Convierte el valor ingresado en un numero entero.
# Obtenemos la fecha actual.
hoy = date.today()
# Calcualmos la edad.
fecha_nacimiento = date(año_nacimiento,mes_nacimiento,dia_nacimiento)
# Se calcula la edad inicial.
edad = hoy.year - fecha_nacimiento.year
# Se calcula la edad inicial restando la fecha de nacimeinto al año actual.
# Verificamos si el usuario no ha cumplido años este año
if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day): edad -= 1
# Verificamos si es mayo de edad.
if edad >= 18:
    print(f"Tienes {edad} años. Eres mayor de edad.")
else:
    print(f"Tienes {edad} años. Eres menor de edad.")
# f"Tienes {edad} años. Eres menor de edad." es una f-string, utilizada anteriormente en el ejercicio 1 y nos sirve para incluir una variable dentro de un texto