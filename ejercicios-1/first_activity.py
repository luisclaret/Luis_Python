def hello():
    """
    TODO:
    - Retorna 'Hello, World!'
    """
    return "Hello, World!"


def concat_two_strings(str1, str2):
    """
    TODO:
    - Retorna la concatenación de str1 y str2
    """
    return str1 + str2


def add_two_numbers(a, b):
    """
    TODO:
    - Retorna el resultado de a + b
    """
    return a + b


def subtract_two_numbers(a, b):
    """
    TODO:
    - Retorna el resultado de a - b
    """
    return a - b


def multiply_two_numbers(a, b):
    """
    TODO:
    - Retorna el resultado de a * b
    """
    return a * b


def area_of_triangle(base, height):
    """
    TODO:
    - Retorna el area del triángulo
    """
    return (base * height) / 2


def area_of_rectangle(length, width):
    """
    TODO:
    - Retorna el area del rectángulo
    """
    return length * width


def area_of_square(side):
    """
    TODO:
    - Retorna el area del cuadrado
    """
    return side**2


def pythagorean_theorem(a, b):
    """
    TODO:
    - Retorna la hipotenusa usando el teorema de Pitágoras
    """
    return (a**2 + b**2) ** 0.5


def convert_to_celsius(f):
    """
    TODO:
    - Retorna la conversión de Fahrenheit a Celsius
    """
    return (f - 32) / 1.8


def convert_to_fahrenheit(c):
    """
    TODO:
    - Retorna la conversión de Celsius a Fahrenheit
    """
    return (c * 1.8) + 32


def quadratic_formula(a, b, c):
    """
    TODO:
    - Retorna las dos soluciones de la ecuación cuadrática ax^2 + bx + c = 0
    """
    det = b**2 - 4 * a * c
    if det == 0:
        x = (-b) / (2 * a)
        return x
    elif det > 0:
        x1 = (-b + ((b**2 - 4 * a * c) ** 0.5)) / (2 * a)
        x2 = (-b - ((b**2 - 4 * a * c) ** 0.5)) / (2 * a)
        return x1, x2
    else:
        raise ValueError("Raices imaginarias en la funcion")


def sum_two_numbers_if_even(a, b):
    """
    TODO:
    - Retorna la suma de a y b si ambos son pares, de lo contrario retorna 0
    """
    if (a % 2) == 0 and (b % 2) == 0:
        return a + b
    else:
        return 0


def calculate_first_right_digit(n):
    """
    TODO:
    - Retorna el primer dígito a la derecha de n
    """
    return abs(n) % 10


def divide_two_numbers(a, b):
    """
    TODO:
    - Retorna el resultado de la división a y b
    """
    try:
        return a / b
    except:
        raise ValueError("Division por 0 no se puede")


def is_even(a):
    """
    TODO:
    - Retorna True si a es par, de lo contrario False
    """
    return (a % 2) == 0


def is_odd(a):
    """
    TODO:
    - Retorna True si a es impar, de lo contrario False
    """
    return (a % 2) != 0


def is_divisible_by_x(n, x):
    """
    TODO:
    - Retorna True si n es divisible por x, de lo contrario False
    """
    return (n % x) == 0


def is_leap_year(year):
    """
    TODO:
    - Retorna True si year es un año bisiesto, de lo contrario False
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
