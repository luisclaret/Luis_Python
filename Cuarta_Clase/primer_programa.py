# Calculador

# suma, resta, multiplicacion, division, exponencia y modulo.
# Solo operaciones entre dos numeros


# Funcion para introducir numeros
def introducir_numero():
    x = input("Introduzca numero: ")
    return x


def introducir_operacion():
    x = input(
        "Introduzca la operacion a realizar: \n"
        "1. Suma \n"
        "2. Resta \n"
        "3. Multiplicacion \n"
        "4. Division \n"
        "5. Exponencia \n"
        "6. Modulo \n"
        "Recuerde introducir el numero correspondiente a la operacion: \n"
    )
    return x


def operar(a, b, op):
    if op == 1:  # 1 - suma
        return suma(a, b)
    elif op == 2:  # 2 - resta
        return resta(a, b)
    elif op == 3:  # 3 - multiplicacion
        return multiplicacion(a, b)
    elif op == 4:  # 4 - division
        return division(a, b)
    elif op == 5:  # 5 - exponencia
        return exponencia(a, b)
    elif op == 6:  # 6 - modulo
        return modulo(a, b)
    else:
        raise ValueError("Operacion no identificada")


# Funcion suma
def suma(a, b):
    return a + b


# Funcion resta
def resta(a, b):
    return a - b


# Funcion multiplicacion
def multiplicacion(a, b):
    return a * b


# Funcion division
def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir entre 0")


# Funcion exponencia
def exponencia(a, b):
    return a**b


# Funcion modulo
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        raise ValueError("No se puede dividir entre 0")


print("Bienvenido al programa de calculadora - Version #1")


x_1 = introducir_numero()
x_2 = introducir_numero()
op = introducir_operacion()
resultado = operar(int(x_1), int(x_2), int(op))
print("El resultado es: ", resultado)
