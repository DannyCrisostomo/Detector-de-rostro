"""
Detector de Rostros con Tkinter

Este script utiliza OpenCV para la detección de rostros en tiempo real desde una cámara
y utiliza Tkinter para crear una interfaz gráfica simple con dos botones: uno para iniciar
la detección de rostros y otro para cerrar la aplicación.

Requisitos:
- OpenCV (cv2)
- Tkinter

Instrucciones:
1. Asegúrate de tener OpenCV y Tkinter instalados.
2. Ejecuta el script.

Controles:
- Presiona 'q' o 'Q' para detener la detección de rostros y cerrar la aplicación.

"""
import cv2
import tkinter as tk
from tkinter import ttk

def Detectar_rostro():
    """
    Inicia la detección de rostros utilizando la cámara en tiempo real.

    Instrucciones:
    - Asegúrate de tener OpenCV instalado.
    - Presiona 'q' o 'Q' para detener la detección de rostros y cerrar la aplicación.

    Controles:
    - Presiona 'q' o 'Q' para detener la detección de rostros y cerrar la aplicación.

    """
    try:
        # Intenta cargar el clasificador Haar Cascade preentrenado
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    except cv2.error as e:
        # Captura la excepción en caso de error al cargar el clasificador
        print(f"Error al cargar el clasificador Haar Cascade: {e}")
        return
    # Iniciar la captura de video desde la cámara (puedes cambiar el número 0 si tienes varias cámaras)
    cap = cv2.VideoCapture(0)
    while True:
        # Leer el fotograma de la cámara
        ret, frame = cap.read()
        # Convertir la imagen a escala de grises (esto mejora la eficiencia del detector)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detectar rostros en la imagen
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # Dibujar un rectángulo alrededor de los rostros detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 128), 2)
        # Mostrar la imagen resultante
        cv2.imshow('Detector de Rostros', frame)

        # Romper el bucle si se presiona la tecla 'q' o 'Q'
        if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
            break
    # Liberar los recursos fuera del bucle
    cap.release()
    cv2.destroyAllWindows()

def cerrar_ventana():
    """
    Cierra la ventana principal de la aplicación.
    """
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Detectar Rostro")
ventana.geometry("300x300")
ventana.resizable(False, False)
ventana.configure(bg="#161616")
# Centrar la ventana en la pantalla
ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()
posicion_x = int((ventana.winfo_screenwidth() - ancho_ventana) / 2)
posicion_y = int((ventana.winfo_screenheight() - alto_ventana) / 2)
ventana.geometry(f"+{posicion_x}+{posicion_y}")

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