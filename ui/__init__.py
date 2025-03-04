import pandas as pd

def mostrar_tabla(datos):
    # Convert the list of data to a pandas DataFrame
    df = pd.DataFrame(datos)
    
    if len(datos) == 0:
        print("No se encontraron datos para la consulta especificada.")
        return
        
    # Display the DataFrame
    print("\nResultados encontrados:")
    print(df)

def obtener_entrada():
    departamento = input("Ingrese el departamento: ").upper()
    municipio = input("Ingrese el municipio (o presione Enter para omitir): ").upper()
    cultivo = input("Ingrese el cultivo (o presione Enter para omitir): ").upper()
    
    while True:
        try:
            limite = int(input("Ingrese el límite de resultados: "))
            if limite > 0:
                break
            print("El límite debe ser un número positivo.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    return departamento, municipio, cultivo, limite