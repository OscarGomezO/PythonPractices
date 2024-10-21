

def days_in_month(month, year):
    """
    Determines the number of days in a given month and year.

    Args:
        year (int): The year.
        month (int): The month (1-12).

    Returns:
        int: The number of days in the given month and year.
    """

    # Check for February and leap year
    if month == 2 and is_leap_year(year):
        return 29
    elif month == 2:
        return 28

    # Handle other months
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def is_leap_year(year):
    """
    Checks if a given year is a leap year.

    Args:
        year (int): The year.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "El año es Bisiesto."
    else:
        return "El año no es Bisiesto."
   # return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(year, month, day):
    """Calcula el día del año para una fecha dada.

    Args:
        year: El año.
        month: El mes (1-12).
        day: El día del mes.

    Returns:
        El día del año.
    """

    if month >= 1 or month <= 12 or day >= 1 or day <= days_in_month(year, month):
        total_days = day
        for m in range(1, month):
            total_days += days_in_month(m, year)

        return total_days
    else:
        return"Fecha inválida"

    """
    # Validar que la fecha sea válida
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return"Fecha inválida"

    # Sumar los días de los meses anteriores y el día del mes actual
    total_days = day
    for m in range(1, month):
        total_days += days_in_month(m, year)

    return total_days
    """

#Ingreso de datos

day = int(input("Por favor ingrese el día: "))
month = int(input("Por favor ingrese el numero del mes: "))
year = int(input("Por favor ingrese el año: "))

print(f"\nLa fecha ingresada es:  {day}-{month}-{year}")
print(f"La fecha registrada tiene", day_of_year(year, month, day), "dias")
print(is_leap_year(year))
print(f"El mes {month} tiene", days_in_month(month, year), "dias.\n")


#Prueba automatica
"""
day = 31
month = 12
year = 1999

print(f"\nLa fecha ingresada es:    ",{day},"-",{month},"-",{year})
print(f"La fecha registrada tiene", day_of_year(year, month, day), "dias")
print(is_leap_year(year))
print(f"El mes {month} tiene", days_in_month(month, year), "dias.\n")
"""


"""
month = int(input("Por favor ingrese el numero del mes: "))
year = int(input("Por favor ingrese el año: "))
print(is_leap_year(year))
print(f"El mes {month} tiene", days_in_month(month, year), "dias.")
"""
