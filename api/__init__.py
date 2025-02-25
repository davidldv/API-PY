from sodapy import Socrata
import pandas as pd

def consultar_datos(departamento, municipio, cultivo, limite):
    client = Socrata("www.datos.gov.co", None)
    resultados = client.get("ch4u-f3i5", limit=limite)
    df = pd.DataFrame.from_records(resultados)
    
    if df.empty:
        return pd.DataFrame()
    
    # Filtrar por departamento, municipio y cultivo
    df_filtrado = df[(df["departamento"] == departamento) &
                     (df["municipio"] == municipio) &
                     (df["cultivo"] == cultivo)]
    
    if df_filtrado.empty:
        return pd.DataFrame()
    
    # Seleccionar columnas de interés
    columnas = ["departamento", "municipio", "cultivo", "topologia", "ph", "fosforo_p", "potasio_k"]
    df_filtrado = df_filtrado[columnas]
    
    # Convertir valores numéricos
    df_filtrado[["ph", "fosforo_p", "potasio_k"]] = df_filtrado[["ph", "fosforo_p", "potasio_k"]].apply(pd.to_numeric, errors='coerce')
    
    # Calcular la mediana de las variables edáficas
    medianas = df_filtrado[["ph", "fosforo_p", "potasio_k"]].median()
    df_medianas = pd.DataFrame(medianas).T
    df_medianas.insert(0, "departamento", departamento)
    df_medianas.insert(1, "municipio", municipio)
    df_medianas.insert(2, "cultivo", cultivo)
    df_medianas.insert(3, "topologia", df_filtrado["topologia"].mode()[0] if not df_filtrado["topologia"].mode().empty else "Desconocido")
    
    return df_medianas
