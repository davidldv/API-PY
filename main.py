import ui
import api

def main():
    departamento, municipio, cultivo, limite = ui.obtener_entrada()
    datos = api.consultar_datos(departamento, municipio, cultivo, limite)
    ui.mostrar_tabla(datos)

if __name__ == "__main__":
    main()
