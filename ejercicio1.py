# Realizar el siguiente ejercicio con la instrucción if..else La escuela ECAPMA de la UNAD está desarrollando un estudio para verificar el cambio climático en su ciudad. Para esto, le ha pedido su ayuda en la construcción de un programa que solicite las temperaturas de los últimos 5 días y muestre el promedio de temperaturas si el promedio es mayor o igual a 22 grados, debe informar que el clima es cálido si es menor que es frio.
# Solicitar las temperaturas de los ultimos 5 dias
print("Ingrese las temperaturas de los ultimos 5 dias:")
temperaturas = [] # Lista vacia para almacenas las temperaturas
for t in range (1,6): # Este es un bucle "for" que se repite 5 veces, desde el dia 1 hasta el dia 5
    temperatura = float(input(f"Temperatura del dia {t}:")) # "float" convierte el dato en un numero decimal, "imput" pide la temperatura al usuario
    temperaturas.append(temperatura) # "append" guarda ese numero en la lista "temperaturas" que declaramos en la fila 5
promedio = sum(temperaturas) / len(temperaturas) # "sum" suma todos los valores dela lista "temperaturas" y "len" cuenta cuantos elementos hay de la lista "temperatura" osea 5 datos, de esta manera se calcula el promedio
print(f"\El promedio de las temperaturas es: {promedio:.2f}°C") # f"\ TEXTO {VARIABLE:.2f} Este formato nos permite añadir un texto y al mismo tiempo llamar una variable entre llaves para que esta se reconozca y "2f" implementa que el resultado se de con 2 decimales
if promedio >= 22: # Esta es la logica del programa solicitado para el ejercicio #1
    print("El clima es calido")
else:
    print("El clima es frio")