import tkinter as tk
def cerrar_ventana():
    root.destroy()
def actualizar_dato(): # Funcion llamada para reemplazar el text de las etiquetas con la variable correspondiente
    
    # Variables definidas
    a = int(input("Numero 1: "))
    b = int(input("Numero 2: "))
    c = a + b
    
    # Configuracion para las etiquetas reemplaza el text=variable o caracter seleccionado
    sub0.config(text=a)
    sub1.config(text="+")
    sub2.config(text=b)
    sub3.config(text="=")
    sub4.config(text=c)
    
# Inicio de pantalla y parametros (nombre,color)
root = tk.Tk()
root.title("Pantalla")
root.configure(bg="lightblue")

# Crear etiquetas en la pantalla para mostrar el texto seleccionado
    # .pack compila las etiquetas en un formato vertical
    # .grid compila las etiquetas en un formato de lineas y columnas permite mayor control y orden
    # fb="" permite cambiar el color de la letra
    #bg="" permite cambiar el color del fondo de la letra
sub0 = tk.Label(root, text="",fg="green",bg="lightblue")
sub0.grid(row=0,column=0)
sub1 = tk.Label(root, text="",bg="lightblue")
sub1.grid(row=0,column=1)
sub2 = tk.Label(root, text="",fg="green",bg="lightblue")
sub2.grid(row=0,column=2)
sub3 = tk.Label(root, text="",bg="lightblue")
sub3.grid(row=0,column=3)
sub4 = tk.Label(root, text="",fg="red",bg="lightblue")
sub4.grid(row=0,column=4)
boton_cerrar = tk.Button(root, text="cerrar",command= cerrar_ventana)
boton_cerrar.grid(row=1,column=2)

actualizar_dato()  # Llamada a la funci�n despu�s de definir las etiquetas y actualiza estas mismas con sus valores definidos previamente

root.mainloop()# Ejecutar ventana

