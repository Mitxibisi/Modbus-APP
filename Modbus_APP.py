import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from modbus_tk import modbus_tcp

def agregar_texto(text_widget, texto):
    text_widget.insert(tk.END, texto + "\n")

def borrarlista():
	alarmas.delete("1.0",tk.END)

def connectar():
  try:
    # Intentar conectarse al servidor Modbus
    client.open()
    
    pedir_holding()
    pedir_bool()
    
    error.config(bg="lightgreen",text="Sin Error")
  
  except Exception as e:
    error.config(text="Error1: " + str(e), bg="red")
    agregar_texto(alarmas,f"Error2: {str(e)}")
  
  finally:
    client.close()  # Asegurarnos de cerrar la conexión Modbus si hay un error

def desconectar():
    client.close()

def parar(): #Funcion para detener runtime
    root.destroy()
    client.close()        
    
def pedir_bool(): #Funcion para actualizar los datos en pantalla
    valor = client.execute(slave=1, function_code= 1, starting_address= 0, quantity_of_x= 10) #Lee las bobinas correspondientes
    v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = valor #Desglosa la lista de booleanos separandolos en diferentes variables
    
    dat1.config(text="True" if v1 else "False", style="OK.TLabel" if v1 else "Error.TLabel")
    dat2.config(text="True" if v2 else "False", style="OK.TLabel" if v2 else "Error.TLabel")
    dat3.config(text="True" if v3 else "False", style="OK.TLabel" if v3 else "Error.TLabel")
    dat4.config(text="True" if v4 else "False", style="OK.TLabel" if v4 else "Error.TLabel")
    dat5.config(text="True" if v5 else "False", style="OK.TLabel" if v5 else "Error.TLabel")
    dat6.config(text="True" if v6 else "False", style="OK.TLabel" if v6 else "Error.TLabel")
    dat7.config(text="True" if v7 else "False", style="OK.TLabel" if v7 else "Error.TLabel")
    dat8.config(text="True" if v8 else "False", style="OK.TLabel" if v8 else "Error.TLabel")
    dat9.config(text="True" if v9 else "False", style="OK.TLabel" if v9 else "Error.TLabel")
    dat10.config(text="True" if v10 else "False", style="OK.TLabel" if v10 else "Error.TLabel")
    
    root.after(100, pedir_bool) 

def pedir_holding():
 try:
        # Leer valores de registros de retención
        holding_register_values = client.execute(slave=1, function_code=4, starting_address=0, quantity_of_x=10)
        
        # Actualizar etiquetas con los nuevos valores
        dat21.configure(text=holding_register_values[0])
        dat22.configure(text=holding_register_values[1])
        dat23.configure(text=holding_register_values[2])

 except Exception as e:
        print("Error al actualizar valores:", e)

    # Llamar a la función de actualización nuevamente después de un tiempo
 root.after(200, pedir_holding)


grande = ("Arial", 12, "bold")
peque = ("Comic Sans", 10, "bold")
peque1 = ("Arial Black", 8)
peque2 = ("Comic Sans", 10, "bold")
peque3 = ("Arial Black", 12)


root = tk.Tk() # Pantalla
root.title("DASHBOARD")


panel = ttk.Notebook(root)
panel.pack()

esc1 = ttk.Frame(panel)
esc2 = ttk.Frame(panel)
esc4 = ttk.Frame(panel)
esc5 = ttk.Frame(panel)

panel.add(esc1, text="Supervision")
panel.add(esc2, text="Planta")
panel.add(esc4, text="Alarmas")
panel.add(esc5, text="Comentarios")

esc = ttk.Frame(esc1)
esc.pack(padx=1,pady=1,fill="both",
         expand=True)

esc3 = ttk.Frame(esc)
esc3.grid(row=1, column=4,
          rowspan=3)

esc6 = ttk.Frame(esc,style="Marco.TFrame")
esc6.grid(row=1, column=0,
          rowspan=10, columnspan=2,
          padx=5)

style = ttk.Style()
style.configure("TButton",
                background="black",
                font=grande,
                padding=4,
                relief="raised")
style.configure("General.TLabel",
                background="#AEB6BF",
                font=peque2,
                relief="sunken",
                padding=4,
                borderwidth=4)
style.configure("General1.TLabel",
                background="#AEB6BF",
                font=peque2,
                relief="sunken",
                padding=4,
                borderwidth=4,
                width=6)
style.configure("Error.TLabel",
                background="red",
                font=peque2,
                relief="sunken",
                padding=4,
                borderwidth=4,
                width=6)
style.configure("OK.TLabel",
                background="lightgreen",
                font=peque2,
                relief="sunken",
                padding=4,
                borderwidth=4,
                width=6)
style.configure("Direccion.TLabel",
                background="#AEB6BF",
                relief="sunken",
                padding=2,
                borderwidth=2)
style.configure("IMAGEN.TLabel")
style.configure("Marco.TFrame",
                borderwidth=4,
                relief="sunken",
                background="lightgrey")
style.configure("Direccion.TFrame",
                background="grey",
                relief="sunken")
style.configure("BOOL.TLabel",
                background="#AEB6BF",
                relief="sunken",
                font=peque,
                borderwidth=4)



image_path = "E:\\IMG_20240412_122837.jpg"
image = Image.open(image_path)
width, height = 620, 510  # Nuevas dimensiones de la imagen (cambia según sea necesario)
image = image.resize((width, height),Image.Resampling.LANCZOS )
photo = ImageTk.PhotoImage(image)

image_path1 = "E:\\08a9b98b23e992e872bdb0d2199395a5.png"
image1= Image.open(image_path1)

image1 = image1.resize((600, 200),Image.Resampling.LANCZOS )
photo1 = ImageTk.PhotoImage(image1)


label = ttk.Label(esc,
                  image=photo1,
                  style= "IMAGEN.TLabel")
label.grid(row= 0 ,
           column = 0,
           padx=10,
          pady=10,
          columnspan=5)

label1 = ttk.Label(esc2,
                   image=photo,
                   style="General.TLabel")
label1.pack(padx=10,
            pady=10)


text=tk.Text(esc5,height=30,bg="lightgrey")
text.pack()
alarmas=tk.Text(esc4,height=30,bg="lightgrey",font=peque3)
alarmas.grid(row=0,column=0,sticky="nesw")

IP = ttk.Entry(esc3)
IP.grid(row=0,column=1,sticky="nesw")
PORT = ttk.Entry(esc3)
PORT.grid(row=1,column=1,sticky="nesw")
IP = ttk.Label(esc3,text="Direccion IP:",style="General.TLabel")
IP.grid(row=0,column=0,sticky="nesw")
PORT = ttk.Label(esc3,text="PUERTO:",style="General.TLabel")
PORT.grid(row=1,column=0,sticky="nesw")


# Defino las etiquetas bool en runtime
dat1 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat1.grid(row=1, column=1, pady=5, padx=0, sticky="nesw")
dat2 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat2.grid(row=2, column=1, pady=5, padx=0, sticky="nesw")
dat3 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat3.grid(row=3, column=1, pady=5, padx=0, sticky="nesw")
dat4 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat4.grid(row=4, column=1, pady=5, padx=0, sticky="nesw")
dat5 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat5.grid(row=5, column=1, pady=5, padx=0, sticky="nesw")
dat6 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat6.grid(row=6, column=1, pady=5, padx=0, sticky="nesw")
dat7 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat7.grid(row=7, column=1, pady=5, padx=0, sticky="nesw")
dat8 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat8.grid(row=8, column=1, pady=5, padx=0, sticky="nesw")
dat9 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat9.grid(row=9, column=1, pady=5, padx=0, sticky="nesw")
dat10 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat10.grid(row=10, column=1, pady=5, padx=0, sticky="nesw")
dat11 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat11.grid(row=1, column=3, pady=5, padx=0, sticky="nesw")
dat12 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat12.grid(row=2, column=3, pady=5, padx=0, sticky="nesw")
dat13 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat13.grid(row=3, column=3, pady=5, padx=0, sticky="nesw")
dat14 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat14.grid(row=4, column=3, pady=5, padx=0, sticky="nesw")
dat15 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat15.grid(row=5, column=3, pady=5, padx=0, sticky="nesw")
dat16 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat16.grid(row=6, column=3, pady=5, padx=0, sticky="nesw")
dat17 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat17.grid(row=7, column=3, pady=5, padx=0, sticky="nesw")
dat18 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat18.grid(row=8, column=3, pady=5, padx=0, sticky="nesw")
dat19 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat19.grid(row=9, column=3, pady=5, padx=0, sticky="nesw")
dat20 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat20.grid(row=10, column=3, pady=5, padx=0, sticky="nesw")
dat21 = ttk.Label(esc6, text= "")
dat21.grid(row=11, column=0, pady=5, padx=0, sticky="nesw")
dat22 = ttk.Label(esc6, text= "")
dat22.grid(row=11, column=1, pady=5, padx=0, sticky="nesw")
dat23 = ttk.Label(esc6, text= "")
dat23.grid(row=11, column=2, pady=5, padx=0, sticky="nesw")

error = tk.Label(esc, text= "", width=25, bg= "lightgrey", relief= "sunken", bd=4)
error.grid(row=11, column=0, pady=5, padx=2, columnspan=5, sticky="nesw")


#Defino los nombres de las etiquetas
dt1 = ttk.Label(esc6,
                text= "Bool_Sh_Auto",
                style="General.TLabel")
dt1.grid(row=1, column=0, pady=5, padx=8, sticky="nesw")
dt2 = ttk.Label(esc6,
                text= "Bool_Sh_Hand",
                style="General.TLabel")
dt2.grid(row=2, column=0, pady=5, padx=8, sticky="nesw")
dt3 = ttk.Label(esc6,
                text= "Bool_Sh_Pieza",
                style="General.TLabel")
dt3.grid(row=3, column=0, pady=5, padx=8, sticky="nesw")
dt4 = ttk.Label(esc6,
                text= "Bool_Sh_Stack",
                style="General.TLabel")
dt4.grid(row=4, column=0, pady=5, padx=8, sticky="nesw")
dt5 = ttk.Label(esc6,
                text= "Bool_Sh_Start",
                style="General.TLabel")
dt5.grid(row=5, column=0, pady=5, padx=8, sticky="nesw")
dt6 = ttk.Label(esc6,
                text= "Bool_Sh_Stop",
                style="General.TLabel")
dt6.grid(row=6, column=0, pady=5, padx=8, sticky="nesw")
dt7 = ttk.Label(esc6,
                text= "Bool_Sh_L_Iron",
                style="General.TLabel")
dt7.grid(row=7, column=0, pady=5, padx=8, sticky="nesw")
dt8 = ttk.Label(esc6,
                text= "Bool_Sh_L_Black",
                style="General.TLabel")
dt8.grid(row=8, column=0, pady=5, padx=8, sticky="nesw")
dt9 = ttk.Label(esc6,
                text= "Bool_Sh_L_White",
                style="General.TLabel")
dt9.grid(row=9, column=0, pady=5, padx=8, sticky="nesw")
dt10 = ttk.Label(esc6,
                 text= "Bool_Marcha",
                 style="General.TLabel")
dt10.grid(row=10, column=0, pady=5, padx=8, sticky="nesw")
dt11 = ttk.Label(esc6,
                 text= "Bool_Sh_Auto",
                 style="General.TLabel")
dt11.grid(row=1, column=2, pady=5, padx=8, sticky="nesw")
dt12 = ttk.Label(esc6,
                 text= "Bool_Sh_Hand",
                 style="General.TLabel")
dt12.grid(row=2, column=2, pady=5, padx=8, sticky="nesw")
dt13 = ttk.Label(esc6,
                 text= "Bool_Sh_Pieza",
                 style="General.TLabel")
dt13.grid(row=3, column=2, pady=5, padx=8, sticky="nesw")
dt14 = ttk.Label(esc6,
                 text= "Bool_Sh_Stack",
                 style="General.TLabel")
dt14.grid(row=4, column=2, pady=5, padx=8, sticky="nesw")
dt15 = ttk.Label(esc6,
                 text= "Bool_Sh_Start",
                 style="General.TLabel")
dt15.grid(row=5, column=2, pady=5, padx=8, sticky="nesw")
dt16 = ttk.Label(esc6,
                 text= "Bool_Sh_Stop",
                 style="General.TLabel")
dt16.grid(row=6, column=2, pady=5, padx=8, sticky="nesw")
dt17 = ttk.Label(esc6,
                 text= "Bool_Sh_L_Iron",
                 style="General.TLabel")
dt17.grid(row=7, column=2, pady=5, padx=8, sticky="nesw")
dt18 = ttk.Label(esc6, 
                 text= "Bool_Sh_L_Black",
                 style="General.TLabel")
dt18.grid(row=8, column=2, pady=5, padx=8, sticky="nesw")
dt19 = ttk.Label(esc6,
                 text= "Bool_Sh_L_White",
                 style="General.TLabel")
dt19.grid(row=9, column=2, pady=5, padx=8, sticky="nesw")
dt20 = ttk.Label(esc6,
                 text= "Bool_Marcha",
                 style="General.TLabel")
dt20.grid(row=10, column=2, pady=5, padx=8, sticky="nesw")


# Defino los botones en runtime
boton_con = ttk.Button(esc, text="Conectar",command=connectar)
boton_con.grid(row=5, column=4, padx=4, sticky="nesw")
boton_desc = ttk.Button(esc, text="Desconectar",command=desconectar)
boton_desc.grid(row=6, column=4, padx=4, sticky="nesw")
boton_1 = ttk.Button(esc, text="MARCHA")
boton_1.grid(row=7, column=4, padx=5, sticky="nesw")
boton_2 = ttk.Button(esc, text="PARO")
boton_2.grid(row=8, column=4, padx=5, sticky="nesw")
boton_3 = ttk.Button(esc, text="REARME")
boton_3.grid(row=9, column=4, padx=5, sticky="nesw")
boton_cerrar = ttk.Button(esc, text="EXIT", command=parar)
boton_cerrar.grid(row=10, column=4, padx=4, sticky="nesw")
Rex = tk.Button(esc4,text= "prueba",command=borrarlista)
Rex.grid(row=1,column=0,sticky="nesw")


# Definir el cliente Modbus
client = modbus_tcp.TcpMaster(host="192.168.1.145",port=502)

root.mainloop()  # Ejecutar runtime

