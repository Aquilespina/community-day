import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Cambia si tu conexión es diferente
db = client['days']
collection = db['personas']

# Función principal para mostrar toda la información del registro
def mostrar_info():
    registro_id = "67187c5eb357e61d731f8bbf"  # ID del registro que quieres mostrar
    try:
        persona = collection.find_one({"_id": ObjectId(registro_id)})  # Convertir a ObjectId
        if persona:
            resultado = (
                f"ID: {persona.get('_id')}\n"
                f"No: {persona.get('No', 'No disponible')}\n"
                f"Captura: {persona.get('Captura ', 'No disponible')}\n"
                f"Nombre: {persona.get('Nombre ', 'No disponible')}\n"
                f"Fecha: {persona.get('Fecha ', 'No disponible')}\n"
                f"Teléfono: {persona.get('Teléfono ', {}).get('$numberLong', 'No disponible')}\n"
                f"Alcaldía: {persona.get('AlcaldÃ­a', 'No disponible')}\n"
                f"Edad: {persona.get('Edad ', 'No disponible')}\n"
                f"Entrevista: {persona.get('Entrevista', 'No disponible')}\n"
                f"Observaciones 1: {persona.get('Observaciones 1', 'No disponible')}\n"
                f"Observaciones 2: {persona.get('Observaciones 2', 'No disponible')}\n"
            )
        else:
            resultado = "Registro no encontrado."
    except Exception as e:
        resultado = f"Error al buscar el registro: {e}"
    
    messagebox.showinfo("Información del Registro", resultado)

# Función para mostrar solo la alcaldía a partir de un archivo CSV
def mostrar_alcaldia():
    archivo_csv = "Preregistros.csv"  # Especifica la ruta de tu archivo CSV
    try:
        # Leer el archivo CSV
        data = pd.read_csv(archivo_csv)
        
        # Filtrar solo las alcaldías
        if "AlcaldÃ­a" in data.columns:
            alcaldias = data["AlcaldÃ­a"].dropna().unique()  # Obtiene alcaldías únicas, eliminando valores nulos
            resultado = "Alcaldías encontradas:\n" + "\n".join(alcaldias)
        else:
            resultado = "No se encontró la columna 'AlcaldÃ­a' en el archivo CSV."
    except Exception as e:
        resultado = f"Error al leer el archivo CSV: {e}"
    
    messagebox.showinfo("Alcaldías del Archivo CSV", resultado)

# Función para el botón de "Gráficas" - gráfica de dispersión entre Alcaldía y Edad
def mostrar_graficas():
    archivo_csv = "Preregistros.csv"  # Especifica la ruta de tu archivo CSV
    try:
        data = pd.read_csv(archivo_csv)
        
        # Verificar que el archivo tenga las columnas necesarias
        if "Edad" in data.columns and "AlcaldÃ­a" in data.columns:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=data, x="AlcaldÃ­a", y="Edad", hue="AlcaldÃ­a", palette="Set2")
            plt.title("Gráfica de Dispersión entre Edad y Alcaldía")
            plt.xlabel("Alcaldía")
            plt.ylabel("Edad")
            plt.xticks(rotation=45)
            plt.show()
        else:
            messagebox.showerror("Error", "El archivo CSV no contiene las columnas 'Edad' y 'AlcaldÃ­a'.")
    except Exception as e:
        messagebox.showerror("Error al generar la gráfica", f"{e}")

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Consultor MongoDB")
ventana.geometry("400x300")

# Botón para mostrar la información completa del registro
boton_mostrar_info = tk.Button(ventana, text="Primer registro ", command=mostrar_info)
boton_mostrar_info.pack(pady=10)

# Botón para mostrar solo la alcaldía del archivo CSV
boton_mostrar_alcaldia = tk.Button(ventana, text="Mostrar Alcaldías", command=mostrar_alcaldia)
boton_mostrar_alcaldia.pack(pady=10)

# Botón para la funcionalidad de gráficas
boton_graficas = tk.Button(ventana, text="Gráficas", command=mostrar_graficas)
boton_graficas.pack(pady=10)

# Ejecutar la ventana de la interfaz
ventana.mainloop()
