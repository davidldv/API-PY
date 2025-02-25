import pandas as pd

def mostrar_tabla(datos):
    """Muestra los datos en formato tabular."""
    if datos.empty:
        print("No se encontraron resultados para la consulta.")
    else:
        print(datos.to_string(index=False))

def obtener_entrada():
    """Solicita al usuario los parámetros de búsqueda."""
    departamento = input("Ingrese el departamento: ")
    municipio = input("Ingrese el municipio: ")
    cultivo = input("Ingrese el cultivo: ")
    try:
        limite = int(input("Ingrese el número de registros a consultar: "))
    except ValueError:
        print("Valor inválido, usando límite predeterminado de 10.")
        limite = 10
    
    return departamento, municipio, cultivo, limite