# Realizar el siguiente ejercicio con la instrucción if..else mediante condicionales anidados (es decir dentro de la instrucción else colocar una nueva condición if..else). La empresa Netflix desea saber cuál es el género favorito de streaming entre 5 personas. Para esto, le ha solicitado su ayuda para desarrollar un programa para saber cuál es el género con más votos entre: acción y ciencia ficción. El programa debe capturar la preferencia de las 5 personas y mostrar cuál de los géneros es el favorito.
# Inicializamos los contadores de votos.
accion = 0
ciencia_ficcion = 0
# Capturar la preferecia de 5 personas.
for i in range(1, 6):
    print(f"persona {i}:")
    preferencia = input("¿Cual es tu genero favorito? (accion / ciencia ficcion):").strip().lower()
    if preferencia == "accion":
        accion += 1
    else:
        if preferencia == "ciencia ficcion":
            ciencia_ficcion += 1
        else:
            print("Opcion no valida. No se contara este voto.")
# Mostramos el resultado utilizando condicionales anidados.
print("\nResultado:")
if accion > ciencia_ficcion:
    print("El genero favorito es accion")
else:
    if ciencia_ficcion > accion:
        print("El genero favorito es ciencia ficcion")
    else:
        print("Hay un empate entre accion y ciencia ficcion")