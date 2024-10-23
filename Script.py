import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId  # Importar ObjectId

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Cambia si tu conexión es diferente
db = client['days']
collection = db['personas']

# Función para mostrar la información del registro específico
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

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Consultor MongoDB")
ventana.geometry("400x300")

# Botón para mostrar la información del registro
boton_mostrar_info = tk.Button(ventana, text="Mostrar información del registro", command=mostrar_info)
boton_mostrar_info.pack(pady=20)

# Ejecutar la ventana de la interfaz
ventana.mainloop()
