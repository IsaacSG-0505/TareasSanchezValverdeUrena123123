# codigos de errores unicos
# codigo           error
#  1       valor ingresado no es numero entero
#  2       parametro operacion fuera de rango
#  3        Division por cero
#  4       valor ingresado no es un string
#  5       parametro opciones fuera de rango

# funcion que permite recibir tres parámetros:
#  Operando 1, Operando 2 y Operación, verifica sean números
#  enteros y validos, y realiza la operacion solicitada.
def basic_operations(Operando1, Operando2, Operacion):

    # Se define resultado como un int
    resultado = int
    # Se reciben los tres parametros, verificando que sean
    #  enteros de lo contrario se retorna codigo de error unico
    try:
        # Condicional if que permite relizar
        # la operacion solicitada, suma, resta o division
        if int(Operacion) == 1:
            resultado = int(Operando1) + int(Operando2)

        elif int(Operacion) == 2:
            resultado = int(Operando1) - int(Operando2)

        elif int(Operacion) == 3:
            # Condicional if que revisa si el dividendo
            # de ingresado es cero dando o el resultado de la division
            if int(Operando2) == 0:
                print("ERROR 3")
            else:
                resultado = int(Operando1) / int(Operando2)
        else:
            # Se indica no se ingreso ningun operando valido de parametro
            print("ERROR 2")
    except int(Operacion):
        # Indica no se ingreso un numero entero como operando
        print("Error 1")
    return (resultado)

# Funcion que permite recibe un único parámetro
# de entrada, verifica es un string.
# Cuenta la cantidad de caracteres y retorna
#  el número de caracteres al usuario.


def count_char(oracion):
    # Define contador en 0
    contador = 0
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # Ciclo que permite contar la contidad de caracteres ingresados
    for i in str(oracion):
        if i in numeros:
            # Indica no se ingreso un string
            print("ERROR 4")

        else:
            # Suma valor al contador
            contador = contador + 1
    return (contador)
