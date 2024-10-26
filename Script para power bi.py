import pandas as pd

# Ruta del archivo CSV que deseas modificar
archivo_csv = "C:/Users/aquil/OneDrive/Documents/community days/community-day/Preregistros.csv"  # Cambia la ruta si es necesario

# Diccionario de reemplazos
reemplazos = {
    "No.": "No",
    "Captura ": "Captura",
    "Nombre ": "Nombre",
    "Fecha ": "Fecha",
    "TÃ©lefono": "Telefono",
    "AlcaldÃ­a": "Alcaldia",
    "Edad ": "Edad",
    "Escolaridad o trabajo": "Escolaridad_o_trabajo",
    "Entrevista": "Entrevista",
    "Observaciones 1": "Observaciones_1",
    "Observaciones 2": "Observaciones_2"
}

# Leer el archivo CSV
try:
    data = pd.read_csv(archivo_csv)
    
    # Renombrar las columnas según el diccionario de reemplazos
    data.rename(columns=reemplazos, inplace=True)

    # Guardar el DataFrame modificado en un nuevo archivo CSV
    nuevo_archivo_csv = "C:/Users/aquil/OneDrive/Documents/community days/community-day/Preregistros_modificado.csv"
    data.to_csv(nuevo_archivo_csv, index=False)

    print(f"Archivo modificado guardado como: {nuevo_archivo_csv}")
except Exception as e:
    print(f"Error al procesar el archivo CSV: {e}")
