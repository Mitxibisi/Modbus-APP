#Librerias
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from modbus_tk import modbus_tcp
import requests
from io import BytesIO

def agregar_texto(lista, texto): #Agrega texto de alarma a la lista
    lista.insert(tk.END, texto + "\n")

def borrarlista(): #Borra las alarmas de la lista
    alarmas.delete("1.0",tk.END)
    style.map("TNotebook.Tab",
        foreground=[("!selected","black")])
    alarmas.config(bg="lightgrey")


def conectar():
  try:
    # Intentar conectarse al servidor Modbus
    client.open()
    
    pedir_holding()
    pedir_bool()
    
    error.config(bg="lightgreen",text="Sin Error")
  
  except Exception as e: #Si aparece error lo almacena y registra
    error.config(text="ErrorConex: "+ str(e), bg="red")
    agregar_texto(alarmas,f"ErrorConex: {str(e)}")
    agregar_texto(alarmasrec,f"ErrorConex: {str(e)}")
    alarmas.config(bg="red")
    style.map("TNotebook.Tab",
              foreground=[("!selected","red")])
  
  finally:
    desconectar()  # Asegurarnos de cerrar la conexión Modbus si hay un error

def desconectar():
    client.close()

def parar(): #Funcion para detener runtime
    root.destroy()
    desconectar()        

def marcha():#Envia un flanco positivo para iniciar la marcha
    client.execute(slave=1, function_code=5, starting_address=30, output_value=1)
    client.execute(slave=1, function_code=5, starting_address=30, output_value=0)
    
def paro():#Envia un paro general
    client.execute(slave=1, function_code=5, starting_address=31, output_value=1) 

def rearme():#Desconecta el paro
    client.execute(slave=1, function_code=5, starting_address=31, output_value=0)

def pedir_bool(): #Funcion para actualizar los datos en pantalla
 try:
        valor = client.execute(slave=1, function_code= 1, starting_address= 0, quantity_of_x= 30)  #Lee las bobinas correspondientes
        
        for index in range(30):
            dat[index].config(text="True" if valor[index] else "False", style="OK.TLabel" if valor[index] else "Error.TLabel")
        
 except Exception as e:
     error.config(text="ErrorBools: "+ str(e),bg="red")
     agregar_texto(alarmas,f"ErrorBools: {str(e)}")
     agregar_texto(alarmasrec,f"ErrorBools: {str(e)}")
     alarmas.config(bg="red")
     style.map("TNotebook.Tab",
       foreground=[("!selected","red")])

 root.after(100, pedir_bool) 

def pedir_holding(): #Lee los holding registers
 try:
        # Leer valores de registros de retención
        holding = client.execute(slave=1, function_code=4, starting_address=0, quantity_of_x=30)
        
        # Actualizar etiquetas con los nuevos valores
        dat21.configure(text = holding[0],style="General2.TLabel")
        dat22.configure(text = holding[1],style="General2.TLabel")
        dat23.configure(text = holding[2],style="General2.TLabel")

 except Exception as e:
        error.config(text="ErrorHoldings: "+ str(e),bg="red")
        agregar_texto(alarmas,f"ErrorHoldings: {str(e)}")
        agregar_texto(alarmasrec,f"ErrorHoldings: {str(e)}")
        alarmas.config(bg="red")
        style.map("TNotebook.Tab",
          foreground=[("!selected","red")])

    # Llamar a la función de actualización nuevamente después de un tiempo
 root.after(200, pedir_holding)


grande = ("Arial", 12, "bold")
peque = ("Comic Sans", 10, "bold")
peque1 = ("Arial Black", 8)
peque2 = ("Comic Sans", 10, "bold")
peque3 = ("Arial Black", 12)
panel=("Arial Black",6,"bold")
panel1=("Arial Black",5,"bold")


root = tk.Tk() # Pantalla
root.title("DASHBOARD")
root.geometry("750x760")

panel = ttk.Notebook(root)
panel.pack()

principal = ttk.Frame(panel)
planta = ttk.Frame(panel)
Alarmero = ttk.Frame(panel)
Configura = ttk.Frame(panel)

panel.add(principal, text="Supervision")
panel.add(planta, text="Planta")
panel.add(Alarmero, text="Alarmas")
panel.add(Configura, text="Configuraciones")

alarmero = ttk.Notebook(Alarmero,style="1.Notebook.Tab")
alarmero.pack()

ASinRec = ttk.Frame(alarmero)
ARec = ttk.Frame(alarmero)

alarmero.add(ASinRec,text="Alarmas Sin Reconocer")
alarmero.add(ARec,text="Historico de alarmas")

esc = ttk.Frame(principal,style="Marco1.TFrame")
esc.pack(padx=1,pady=1,fill="both",
         expand=True)

datos = ttk.Frame(esc,style="Marco.TFrame")
datos.grid(row=1, column=0,
          columnspan=6,
          padx=5,pady=10)

style = ttk.Style()
style.configure("TButton",
                background="black",
                font=grande,
                relief="raised")
style.configure("Alarmas.TButton",
                background="black",
                bordercolor="red",
                foreground="black",
                font=grande,
                relief="raised")
style.configure("General.TLabel",
                background="#CACFD2",
                font=peque2,
                relief="sunken",
                padding=4,
                borderwidth=4)
style.configure("General1.TLabel",
                background="#CACFD2",
                font=peque2,
                relief="sunken",
                padding=4,
                borderwidth=4,
                width=6)
style.configure("General2.TLabel",
                background="#AED6F1",
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
style.configure("IMAGEN.TLabel",
                background="#CACFD2",
                borderwidth=1,
                relief="raised")
style.configure("BOOL.TLabel",
                background="#AEB6BF",
                relief="sunken",
                font=peque,
                borderwidth=4)
style.configure("Marco.TFrame",
                borderwidth=4,
                relief="sunken",
                background="#AAB7B8")
style.configure("Marco1.TFrame",
                borderwidth=4,
                relief="sunken",
                background="#BDC3C7")
style.configure("TNotebook.Tab",
                font=panel)
style.configure("1.TNotebook.Tab",
                font=panel1)


url = "https://img.interempresas.net/fotos/4149029.jpeg"
respuesta = requests.get(url)
image = Image.open((BytesIO(respuesta.content)))
image = image.resize((734, 748),Image.Resampling.LANCZOS )
photo = ImageTk.PhotoImage(image)

url1 = "https://www.laudioalde.eus/wp-content/uploads/2020/02/logo.png"
respuesta1 = requests.get(url1)
image1 = Image.open((BytesIO(respuesta1.content)))
image1 = image1.resize((720, 200),Image.Resampling.LANCZOS )
photo1 = ImageTk.PhotoImage(image1)


label = ttk.Label(esc,
                  image=photo1,
                  style= "IMAGEN.TLabel")
label.grid(row= 0 ,
           column = 0,
           padx=10,
          pady=10,
          columnspan=6)

label1 = ttk.Label(planta,
                   image=photo,
                   style="General.TLabel")
label1.pack(fill="both",
            expand=True)

alarmas=tk.Text(ASinRec,bg="lightgrey",font=peque3)
alarmas.pack(fill="both",
            expand=True)
alarmasrec=tk.Text(ARec,bg="lightgrey",font=peque3)
alarmasrec.pack(fill="both",
            expand=True)

IP = ttk.Entry(Configura)
IP.grid(column=1,row=0)
PORT = ttk.Entry(Configura)
PORT.grid(column=1,row=1)
IP = ttk.Label(Configura,text="Direccion IP:",style="General.TLabel")
IP.grid(column=0,row=0)
PORT = ttk.Label(Configura,text="PUERTO:",style="General.TLabel")
PORT.grid(column=0,row=1)

# Crear una lista de etiquetas vacía
dat = []

for index in range(34):
    if index not in (21, 22, 23):
        column = (index // 10) * 2 + 1  # Cada 10 elementos, cambia de columna
        row = (index % 10) + 1  # Mantiene el rango de filas de 1 a 10

        # Crear la etiqueta
        label = ttk.Label(datos, text="", style="General1.TLabel")
        label.grid(row=row, column=column, pady=5, padx=8, sticky="nesw")

        # Agregar la etiqueta a la lista
        dat.append(label)

#Holding registers
dat21 = ttk.Label(datos, text= "",style="General1.TLabel")
dat21.grid(row=11, column=1, pady=5, padx=5, sticky="nesw")
dat22 = ttk.Label(datos, text= "",style="General1.TLabel")
dat22.grid(row=11, column=3, pady=5, padx=5, sticky="nesw")
dat23 = ttk.Label(datos, text= "",style="General1.TLabel")
dat23.grid(row=11, column=5, pady=5, padx=5, sticky="nesw")

error = tk.Label(esc, text= "¡Hello World!", bg= "#95A5A6", relief= "sunken", bd=5)
error.grid(row=4, column=0, pady=5, padx=5, columnspan=6, sticky="nesw")

Labels = ["Sh_ExD_Fuera","Sh_ExI_Fuera","Sh_Sensor_IND","Sh_Sensor_OPT","Sh_ExD_DENTRO","Sh_ExI_DENTRO",
          "Sh_ExC_FUERA","Sh_S1","Sh_S3","Sh_Auto","Sh_Iron","Sh_S4","Sh_S2","Sh_START","Sh_Quit","Sh_Hand",
          "Sh_Fin_Linea","Sh_Al_Fuera","Sh_Al_Dentro","Sh_Pieza_Alim","Sh_Sensor D","Sh_Black","Sh_S5","Sh_S6",
          "Sh_SENSOR_C","Sh_SENSOR_I","Sh_Sensor_ULT","Sh_STOP","Sh_L_Iron","Sh_L_Black","Sh_L_White","Sh_ExC_DENTRO","Sh_White"]

for index, label_text in enumerate(Labels):
    column = (index // 10) * 2  # Cada 10 elementos, cambia de columna
    row = (index % 10) + 1  # Mantiene el rango de filas de 1 a 10

    # Crear la etiqueta
    label = ttk.Label(datos, text=label_text, style="General.TLabel")
    label.grid(row=row, column=column, pady=5, padx=8, sticky="nesw")

    # Agregar a la lista
    dat.append(label)


# Defino los botones en runtime
boton_con = ttk.Button(esc, text="CONECTAR",command=conectar)
boton_con.grid(row=3, column=0, padx=5, sticky="nesw")
boton_desc = ttk.Button(esc, text="DESCONECTAR",command=desconectar)
boton_desc.grid(row=3, column=1, padx=5, sticky="nesw")
boton_M = ttk.Button(esc, text="MARCHA",command=marcha)
boton_M.grid(row=3, column=2, padx=5, sticky="nesw")
boton_P = ttk.Button(esc, text="PARO",command=paro)
boton_P.grid(row=3, column=3, padx=5, sticky="nesw")
boton_R = ttk.Button(esc, text="REARME",command=rearme)
boton_R.grid(row=3, column=4, padx=5, sticky="nesw")
boton_cerrar = ttk.Button(esc, text="EXIT", command=parar)
boton_cerrar.grid(row=3, column=5, padx=5, sticky="nesw")
Rec = ttk.Button(ASinRec,text= "RECONOCER ALARMAS",command=borrarlista,style="Alarmas.TButton")
Rec.pack(fill="both",
            expand=True)

# Definir el cliente Modbus
client = modbus_tcp.TcpMaster(host="192.168.1.31",port=502)

root.mainloop()  # Ejecutar runtime