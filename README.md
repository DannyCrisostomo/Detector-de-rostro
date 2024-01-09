# Detector de Rostros con Tkinter y OpenCV

Este script utiliza OpenCV para la detección de rostros en tiempo real desde una cámara y utiliza Tkinter para crear una interfaz gráfica simple con dos botones: uno para iniciar la detección de rostros y otro para cerrar la aplicación.

## Requisitos
- OpenCV (cv2)
- Tkinter

## Instrucciones
1. Asegúrate de tener OpenCV y Tkinter instalados.
2. Ejecuta el script.

## Controles
- Presiona 'q' o 'Q' para detener la detección de rostros y cerrar la aplicación.

## Código Fuente

```python
import cv2
import tkinter as tk
from tkinter import ttk

# ... (Resto del código)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Detectar Rostro")
ventana.geometry("300x300")
ventana.resizable(False, False)
ventana.configure(bg="#161616")

# Estilo para los botones
estilo = ttk.Style()
estilo.configure("TButton", padding=5, font=("Arial", 12), background="#FFC0CB")

# Crear botón para detectar rostros
boton_detectar_rostro = ttk.Button(ventana, text="Detectar Rostros", command=Detectar_rostro, style="TButton", width=20)
boton_detectar_rostro.pack(pady=(90, 10), ipady=10)

# Crear botón para salir
boton_salir = ttk.Button(ventana, text="Salir", command=cerrar_ventana, style="TButton", width=20)
boton_salir.pack(pady=10, ipady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
```
##Muestra del codigo
https://github.com/DannyCrisostomo/Detector-de-rostro/blob/d00774c8ed6152b069790109fb9255324bca5e84/Detector%20de%20rostro.png
