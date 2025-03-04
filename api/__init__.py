import pandas as pd

def consultar_datos(departamento, municipio, cultivo, limite):
    try:
        # Asumiendo que el archivo Excel está en la carpeta data
        df = pd.read_excel("c:/Users/david/Dev/API-PY/data/laboratorio_suelo.xlsx")
        
        # Aplicar filtros
        mask = df['Departamento'].str.upper() == departamento.upper()
        if municipio:
            mask &= df['Municipio'].str.upper() == municipio.upper()
        if cultivo:
            mask &= df['Cultivo'].str.upper() == cultivo.upper()
            
        resultados = df[mask].head(limite)
        return resultados.to_dict('records')
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo Excel")
        return []
    except Exception as e:
        print(f"Error al leer los datos: {str(e)}")
        return []