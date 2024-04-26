
#Librerias
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from modbus_tk import modbus_tcp
import requests
from io import BytesIO

def agregar_texto(text_widget, texto): #Agrega texto de alarma a la lista
    text_widget.insert(tk.END, texto + "\n")

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
    
        dat1.config(text="True" if valor[0] else "False", style="OK.TLabel" if valor[0] else "Error.TLabel")
        dat2.config(text="True" if valor[1] else "False", style="OK.TLabel" if valor[1] else "Error.TLabel")
        dat3.config(text="True" if valor[2] else "False", style="OK.TLabel" if valor[2] else "Error.TLabel")
        dat4.config(text="True" if valor[3] else "False", style="OK.TLabel" if valor[3] else "Error.TLabel")
        dat5.config(text="True" if valor[4] else "False", style="OK.TLabel" if valor[4] else "Error.TLabel")
        dat6.config(text="True" if valor[5] else "False", style="OK.TLabel" if valor[5] else "Error.TLabel")
        dat7.config(text="True" if valor[6] else "False", style="OK.TLabel" if valor[6] else "Error.TLabel")
        dat8.config(text="True" if valor[7] else "False", style="OK.TLabel" if valor[7] else "Error.TLabel")
        dat9.config(text="True" if valor[8] else "False", style="OK.TLabel" if valor[8] else "Error.TLabel")
        dat10.config(text="True" if valor[9] else "False", style="OK.TLabel" if valor[9] else "Error.TLabel")
        dat11.config(text="True" if valor[10] else "False", style="OK.TLabel" if valor[10] else "Error.TLabel")
        dat12.config(text="True" if valor[11] else "False", style="OK.TLabel" if valor[11] else "Error.TLabel")
        dat13.config(text="True" if valor[12] else "False", style="OK.TLabel" if valor[12] else "Error.TLabel")
        dat14.config(text="True" if valor[13] else "False", style="OK.TLabel" if valor[13] else "Error.TLabel")
        dat15.config(text="True" if valor[14] else "False", style="OK.TLabel" if valor[14] else "Error.TLabel")
        dat16.config(text="True" if valor[15] else "False", style="OK.TLabel" if valor[15] else "Error.TLabel")
        dat17.config(text="True" if valor[16] else "False", style="OK.TLabel" if valor[16] else "Error.TLabel")
        dat18.config(text="True" if valor[17] else "False", style="OK.TLabel" if valor[17] else "Error.TLabel")
        dat19.config(text="True" if valor[18] else "False", style="OK.TLabel" if valor[18] else "Error.TLabel")
        dat20.config(text="True" if valor[19] else "False", style="OK.TLabel" if valor[19] else "Error.TLabel")
        dat24.config(text="True" if valor[20] else "False", style="OK.TLabel" if valor[20] else "Error.TLabel")
        dat25.config(text="True" if valor[21] else "False", style="OK.TLabel" if valor[21] else "Error.TLabel")
        dat26.config(text="True" if valor[22] else "False", style="OK.TLabel" if valor[22] else "Error.TLabel")
        dat27.config(text="True" if valor[23] else "False", style="OK.TLabel" if valor[23] else "Error.TLabel")
        dat28.config(text="True" if valor[24] else "False", style="OK.TLabel" if valor[24] else "Error.TLabel")
        dat29.config(text="True" if valor[25] else "False", style="OK.TLabel" if valor[25] else "Error.TLabel")
        dat30.config(text="True" if valor[26] else "False", style="OK.TLabel" if valor[26] else "Error.TLabel")
        dat31.config(text="True" if valor[27] else "False", style="OK.TLabel" if valor[27] else "Error.TLabel")
        dat32.config(text="True" if valor[28] else "False", style="OK.TLabel" if valor[28] else "Error.TLabel")
        dat33.config(text="True" if valor[29] else "False", style="OK.TLabel" if valor[29] else "Error.TLabel")
        
 except Exception as e:
     error.config(text="ErrorBools: "+ str(e),bg="red")
     agregar_texto(alarmas,f"ErrorBools: {str(e)}")
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


root = tk.Tk() # Pantalla
root.title("DASHBOARD")
root.geometry("750x760")

panel = ttk.Notebook(root)
panel.pack()

esc1 = ttk.Frame(panel)
esc2 = ttk.Frame(panel)
esc4 = ttk.Frame(panel)
esc5 = ttk.Frame(panel)

panel.add(esc1, text="Supervision")
panel.add(esc2, text="Planta")
panel.add(esc4, text="Alarmas")
panel.add(esc5, text="Configuraciones")

esc = ttk.Frame(esc1,style="Marco1.TFrame")
esc.pack(padx=1,pady=1,fill="both",
         expand=True)

esc6 = ttk.Frame(esc,style="Marco.TFrame")
esc6.grid(row=1, column=0,
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


url = "https://img.interempresas.net/fotos/4149029.jpeg"
response = requests.get(url)
image = Image.open((BytesIO(response.content)))
image = image.resize((734, 748),Image.Resampling.LANCZOS )
photo = ImageTk.PhotoImage(image)

url1 = "https://www.laudioalde.eus/wp-content/uploads/2020/02/logo.png"
response1 = requests.get(url1)
image1 = Image.open((BytesIO(response1.content)))
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

label1 = ttk.Label(esc2,
                   image=photo,
                   style="General.TLabel")
label1.pack(fill="both",
            expand=True)

alarmas=tk.Text(esc4,bg="lightgrey",font=peque3)
alarmas.pack(fill="both",
            expand=True)

IP = ttk.Entry(esc5)
IP.pack()
PORT = ttk.Entry(esc5)
PORT.pack()
IP = ttk.Label(esc5,text="Direccion IP:",style="General.TLabel")
IP.pack()
PORT = ttk.Label(esc5,text="PUERTO:",style="General.TLabel")
PORT.pack()


# Defino las etiquetas bool en runtime
dat1 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat1.grid(row=1, column=1, pady=5, padx=5, sticky="nesw")
dat2 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat2.grid(row=2, column=1, pady=5, padx=5, sticky="nesw")
dat3 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat3.grid(row=3, column=1, pady=5, padx=5, sticky="nesw")
dat4 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat4.grid(row=4, column=1, pady=5, padx=5, sticky="nesw")
dat5 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat5.grid(row=5, column=1, pady=5, padx=5, sticky="nesw")
dat6 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat6.grid(row=6, column=1, pady=5, padx=5, sticky="nesw")
dat7 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat7.grid(row=7, column=1, pady=5, padx=5, sticky="nesw")
dat8 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat8.grid(row=8, column=1, pady=5, padx=5, sticky="nesw")
dat9 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat9.grid(row=9, column=1, pady=5, padx=5, sticky="nesw")
dat10 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat10.grid(row=10, column=1, pady=5, padx=5, sticky="nesw")

dat11 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat11.grid(row=1, column=3, pady=5, padx=5, sticky="nesw")
dat12 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat12.grid(row=2, column=3, pady=5, padx=5, sticky="nesw")
dat13 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat13.grid(row=3, column=3, pady=5, padx=5, sticky="nesw")
dat14 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat14.grid(row=4, column=3, pady=5, padx=5, sticky="nesw")
dat15 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat15.grid(row=5, column=3, pady=5, padx=5, sticky="nesw")
dat16 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat16.grid(row=6, column=3, pady=5, padx=5, sticky="nesw")
dat17 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat17.grid(row=7, column=3, pady=5, padx=5, sticky="nesw")
dat18 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat18.grid(row=8, column=3, pady=5, padx=5, sticky="nesw")
dat19 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat19.grid(row=9, column=3, pady=5, padx=5, sticky="nesw")
dat20 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat20.grid(row=10, column=3, pady=5, padx=5, sticky="nesw")

dat24 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat24.grid(row=1, column=5, pady=5, padx=5, sticky="nesw")
dat25 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat25.grid(row=2, column=5, pady=5, padx=5, sticky="nesw")
dat26 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat26.grid(row=3, column=5, pady=5, padx=5, sticky="nesw")
dat27 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat27.grid(row=4, column=5, pady=5, padx=5, sticky="nesw")
dat28 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat28.grid(row=5, column=5, pady=5, padx=5, sticky="nesw")
dat29 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat29.grid(row=6, column=5, pady=5, padx=5, sticky="nesw")
dat30 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat30.grid(row=7, column=5, pady=5, padx=5, sticky="nesw")
dat31 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat31.grid(row=8, column=5, pady=5, padx=5, sticky="nesw")
dat32 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat32.grid(row=9, column=5, pady=5, padx=5, sticky="nesw")
dat33 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat33.grid(row=10, column=5, pady=5, padx=5, sticky="nesw")




#Holding registers
dat21 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat21.grid(row=11, column=1, pady=5, padx=5, sticky="nesw")
dat22 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat22.grid(row=11, column=3, pady=5, padx=5, sticky="nesw")
dat23 = ttk.Label(esc6, text= "",style="General1.TLabel")
dat23.grid(row=11, column=5, pady=5, padx=5, sticky="nesw")

error = tk.Label(esc, text= "¡Hello World!", bg= "#95A5A6", relief= "sunken", bd=5)
error.grid(row=4, column=0, pady=5, padx=5, columnspan=6, sticky="nesw")


#Defino los nombres de las etiquetas
dt1 = ttk.Label(esc6,
                text= "ExD_Fuera",
                style="General.TLabel")
dt1.grid(row=1, column=0, pady=5, padx=8, sticky="nesw")
dt2 = ttk.Label(esc6,
                text= "ExI_Fuera",
                style="General.TLabel")
dt2.grid(row=2, column=0, pady=5, padx=8, sticky="nesw")
dt3 = ttk.Label(esc6,
                text= "Sensor_IND",
                style="General.TLabel")
dt3.grid(row=3, column=0, pady=5, padx=8, sticky="nesw")
dt4 = ttk.Label(esc6,
                text= "Sensor_OPT",
                style="General.TLabel")
dt4.grid(row=4, column=0, pady=5, padx=8, sticky="nesw")
dt5 = ttk.Label(esc6,
                text= "ExD_DENTRO",
                style="General.TLabel")
dt5.grid(row=5, column=0, pady=5, padx=8, sticky="nesw")
dt6 = ttk.Label(esc6,
                text= "ExI_DENTRO",
                style="General.TLabel")
dt6.grid(row=6, column=0, pady=5, padx=8, sticky="nesw")
dt7 = ttk.Label(esc6,
                text= "ExC_FUERA",
                style="General.TLabel")
dt7.grid(row=7, column=0, pady=5, padx=8, sticky="nesw")
dt8 = ttk.Label(esc6,
                text= "Sh_S1",
                style="General.TLabel")
dt8.grid(row=8, column=0, pady=5, padx=8, sticky="nesw")
dt9 = ttk.Label(esc6,
                text= "Sh_S3",
                style="General.TLabel")
dt9.grid(row=9, column=0, pady=5, padx=8, sticky="nesw")
dt10 = ttk.Label(esc6,
                 text= "Sh_Auto",
                 style="General.TLabel")
dt10.grid(row=10, column=0, pady=5, padx=8, sticky="nesw")
dt32 = ttk.Label(esc6,
                 text= "Sh_Iron",
                 style="General.TLabel")
dt32.grid(row=11, column=0, pady=5, padx=8, sticky="nesw")

dt11 = ttk.Label(esc6,
                 text= "Sh_S4",
                 style="General.TLabel")
dt11.grid(row=1, column=2, pady=5, padx=8, sticky="nesw")
dt12 = ttk.Label(esc6,
                 text= "Sh_S2",
                 style="General.TLabel")
dt12.grid(row=2, column=2, pady=5, padx=8, sticky="nesw")
dt13 = ttk.Label(esc6,
                 text= "Sh_START",
                 style="General.TLabel")
dt13.grid(row=3, column=2, pady=5, padx=8, sticky="nesw")
dt14 = ttk.Label(esc6,
                 text= "Sh_Quit",
                 style="General.TLabel")
dt14.grid(row=4, column=2, pady=5, padx=8, sticky="nesw")
dt15 = ttk.Label(esc6,
                 text= "Sh_Hand",
                 style="General.TLabel")
dt15.grid(row=5, column=2, pady=5, padx=8, sticky="nesw")
dt16 = ttk.Label(esc6,
                 text= "Fin_Linea",
                 style="General.TLabel")
dt16.grid(row=6, column=2, pady=5, padx=8, sticky="nesw")
dt17 = ttk.Label(esc6,
                 text= "Al_Fuera",
                 style="General.TLabel")
dt17.grid(row=7, column=2, pady=5, padx=8, sticky="nesw")
dt18 = ttk.Label(esc6, 
                 text= "Al_Dentro",
                 style="General.TLabel")
dt18.grid(row=8, column=2, pady=5, padx=8, sticky="nesw")
dt19 = ttk.Label(esc6,
                 text= "Pieza_Alim",
                 style="General.TLabel")
dt19.grid(row=9, column=2, pady=5, padx=8, sticky="nesw")
dt20 = ttk.Label(esc6,
                 text= "Sensor D",
                 style="General.TLabel")
dt20.grid(row=10, column=2, pady=5, padx=8, sticky="nesw")
dt31 = ttk.Label(esc6,
                 text= "Sh_Black",
                 style="General.TLabel")
dt31.grid(row=11, column=2, pady=5, padx=8, sticky="nesw")


dt21 = ttk.Label(esc6,
                 text= "Sh_S5",
                 style="General.TLabel")
dt21.grid(row=1, column=4, pady=5, padx=8, sticky="nesw")
dt22 = ttk.Label(esc6,
                 text= "Sh_S6",
                 style="General.TLabel")
dt22.grid(row=2, column=4, pady=5, padx=8, sticky="nesw")
dt23 = ttk.Label(esc6,
                 text= "SENSOR_C",
                 style="General.TLabel")
dt23.grid(row=3, column=4, pady=5, padx=8, sticky="nesw")
dt24 = ttk.Label(esc6,
                 text= "SENSOR_I",
                 style="General.TLabel")
dt24.grid(row=4, column=4, pady=5, padx=8, sticky="nesw")
dt25 = ttk.Label(esc6,
                 text= "Sensor_ULT",
                 style="General.TLabel")
dt25.grid(row=5, column=4, pady=5, padx=8, sticky="nesw")
dt26 = ttk.Label(esc6,
                 text= "Sh_STOP",
                 style="General.TLabel")
dt26.grid(row=6, column=4, pady=5, padx=8, sticky="nesw")
dt27 = ttk.Label(esc6,
                 text= "Sh_L_Iron",
                 style="General.TLabel")
dt27.grid(row=7, column=4, pady=5, padx=8, sticky="nesw")
dt28 = ttk.Label(esc6, 
                 text= "Sh_L_Black",
                 style="General.TLabel")
dt28.grid(row=8, column=4, pady=5, padx=8, sticky="nesw")
dt29 = ttk.Label(esc6,
                 text= "Sh_L_White",
                 style="General.TLabel")
dt29.grid(row=9, column=4, pady=5, padx=8, sticky="nesw")
dt30 = ttk.Label(esc6,
                 text= "ExC_DENTRO",
                 style="General.TLabel")
dt30.grid(row=10, column=4, pady=5, padx=8, sticky="nesw")
dt33 = ttk.Label(esc6,
                 text= "Sh_White",
                 style="General.TLabel")
dt33.grid(row=11, column=4, pady=5, padx=8, sticky="nesw")

# Defino los botones en runtime
boton_con = ttk.Button(esc, text="CONECTAR",command=conectar)
boton_con.grid(row=3, column=0, padx=5, sticky="nesw")
boton_desc = ttk.Button(esc, text="DESCONECTAR",command=desconectar)
boton_desc.grid(row=3, column=1, padx=5, sticky="nesw")
boton_1 = ttk.Button(esc, text="MARCHA",command=marcha)
boton_1.grid(row=3, column=2, padx=5, sticky="nesw")
boton_2 = ttk.Button(esc, text="PARO",command=paro)
boton_2.grid(row=3, column=3, padx=5, sticky="nesw")
boton_3 = ttk.Button(esc, text="REARME",command=rearme)
boton_3.grid(row=3, column=4, padx=5, sticky="nesw")
boton_cerrar = ttk.Button(esc, text="EXIT", command=parar)
boton_cerrar.grid(row=3, column=5, padx=5, sticky="nesw")
Rex = ttk.Button(esc4,text= "RECONOCER ALARMAS",command=borrarlista,style="Alarmas.TButton")
Rex.pack(fill="both",
            expand=True)


# Definir el cliente Modbus
client = modbus_tcp.TcpMaster(host="192.168.1.145",port=502)

root.mainloop()  # Ejecutar runtime