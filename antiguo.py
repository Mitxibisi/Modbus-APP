from pymodbus.client import ModbusTcpClient
import tkinter as tk

def parar(): #Funcion para detener runtime
    root.destroy()
    client.close()

def marcha(): #Funcion boton de start
    try:
        client.write_coil(10, True, slave=1) #Escribe en la bobina 10 el bit 1 == True
        result = client.read_coils(10, 1, slave=1) #Lee el dato antes escrito para comprobar correcto funcionamiento
        print(result.bits[0])
    except Exception as e:
        error.config(text= "Error3" + e)
   
def omarcha(): #Funcion de Start==0
    try:
        client.write_coil(10, False, slave=1) #Escribe en la bobina 10 el bit 0 == False
        result = client.read_coils(10, 1, slave=1) #Lee el dato antes escrito para comprobar correcto funcionamiento
        print(result.bits[0])
    except Exception as e:
        error.config(text= "Error2" + e)
       
def leer_bool():#Funcion leer boolenos y guardarlos en una lista
    resultado = client.read_coils(0, 9, slave=1) #Lee las bobinas correspondientes
    valor = [] #Crea una lista
    for bit in resultado.bits: #Cuenta los bits y ejecuta la accion la cantidad de datos que tenga
        valor.append(bit)  # Agrega cada booleano a la lista(Append == Añade el elemento correspondiente al final de la lista)
    return valor

def pedir_bool(): #Funcion para actualizar los datos en pantalla
    valor = leer_bool() #Pide la lista de booleanos
    v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, vm15, vm16 = valor #Desglosa la lista de booleanos separandolos en diferentes variables
   
    dat1.config(text="True" if v1 else "False",fg="#145A32" if v1 else "red")
    dat2.config(text="True" if v2 else "False",fg="#145A32" if v2 else "red")
    dat3.config(text="True" if v3 else "False",fg="#145A32" if v3 else "red")
    dat4.config(text="True" if v4 else "False",fg="#145A32" if v4 else "red")
    dat5.config(text="True" if v5 else "False",fg="#145A32" if v5 else "red")
    dat6.config(text="True" if v6 else "False",fg="#145A32" if v6 else "red")
    dat7.config(text="True" if v7 else "False",fg="#145A32" if v7 else "red")
    dat8.config(text="True" if v8 else "False",fg="#145A32" if v8 else "red")
    dat9.config(text="True" if v9 else "False",fg="#145A32" if v9 else "red")
    dat10.config(text="True" if v10 else "False",fg="#145A32" if v10 else "red")
   
    root.after(100, pedir_bool)

grande = ("Arial", 12, "bold")
peque = ("Comic Sans", 10, "bold")
peque1 = ("Arial Black", 8)
peque2 = ("Comic Sans", 10, "bold")

root = tk.Tk() # Pantalla
root.title("DASHBOARD")
root.config(bg="#85C1E9")

esc1 = tk.Frame(root, bg="black", bd=3) # Frames (Para crear un runtime más visual)
esc1.grid(row=0, column=0,padx=6,pady=6)

esc = tk.Frame(esc1, bg="#F4D03F", bd=0)
esc.grid(row=0, column=0,padx=1,pady=1)


# Defino las etiquetas bool en runtime
dat1 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat1.grid(row=0, column=1, pady=5, padx=0, sticky="w")
dat2 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat2.grid(row=1, column=1, pady=5, padx=0, sticky="w")
dat3 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat3.grid(row=2, column=1, pady=5, padx=0, sticky="w")
dat4 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat4.grid(row=3, column=1, pady=5, padx=0, sticky="w")
dat5 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat5.grid(row=4, column=1, pady=5, padx=0, sticky="w")
dat6 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat6.grid(row=5, column=1, pady=5, padx=0, sticky="w")
dat7 = tk.Label(esc, text= "", width=5, bg= "#AEB6BF", relief= "sunken", font=peque, bd=4)
dat7.grid(row=6, column=1, pady=5, padx=0, sticky="w")
dat8 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat8.grid(row=7, column=1, pady=5, padx=0, sticky="w")
dat9 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat9.grid(row=8, column=1, pady=5, padx=0, sticky="w")
dat10 = tk.Label(esc, text= "", width=5, bg="#AEB6BF", relief= "sunken", font=peque, bd=4)
dat10.grid(row=9, column=1, pady=5, padx=0, sticky="w")
error = tk.Label(esc, text= "Sin Error", width=25, bg= "lightgreen", relief= "sunken", bd=4)
error.grid(row=10, column=0, pady=5, padx=2, columnspan=2, sticky="nesw")


#Defino los nombres de las etiquetas
dt1 = tk.Label(esc, text= "Bool_Sh_Auto", bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt1.grid(row=0, column=0, pady=5, padx=8, sticky="w")
dt2 = tk.Label(esc, text= "Bool_Sh_Hand", bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt2.grid(row=1, column=0, pady=5, padx=8, sticky="w")
dt3 = tk.Label(esc, text= "Bool_Sh_Pieza", bg="#AEB6BF", font=peque, relief="sunken", width=15)
dt3.grid(row=2, column=0, pady=5, padx=8, sticky="w")
dt4 = tk.Label(esc, text= "Bool_Sh_Stack", bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt4.grid(row=3, column=0, pady=5, padx=8, sticky="w")
dt5 = tk.Label(esc, text= "Bool_Sh_Start", bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt5.grid(row=4, column=0, pady=5, padx=8, sticky="w")
dt6 = tk.Label(esc, text= "Bool_Sh_Stop", bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt6.grid(row=5, column=0, pady=5, padx=8, sticky="w")
dt7 = tk.Label(esc, text= "Bool_Sh_L_Iron",bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt7.grid(row=6, column=0, pady=5, padx=8, sticky="w")
dt8 = tk.Label(esc, text= "Bool_Sh_L_Black",bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt8.grid(row=7, column=0, pady=5, padx=8, sticky="w")
dt9 = tk.Label(esc, text= "Bool_Sh_L_White",bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt9.grid(row=8, column=0, pady=5, padx=8, sticky="w")
dt10 = tk.Label(esc, text= "Bool_Marcha", bg="#AEB6BF", font=peque2, relief="sunken", width=15)
dt10.grid(row=9, column=0, pady=5, padx=8, sticky="w")


# Defino los botones en runtime
boton_1 = tk.Button(esc, text="MARCHA", width=8, height=1, bg="lightgreen", relief="raised", command=marcha, font=grande, bd=4)
boton_1.grid(row=4, column=3, padx=5)
boton_2 = tk.Button(esc, text="PARO", width=8, height=1, bg="red", relief="raised", command=omarcha, font=grande, bd=4)
boton_2.grid(row=6, column=3, padx=5)
boton_3 = tk.Button(esc, text="REARME", width=8, height=1, bg="lightblue", relief="raised", command=parar, font=grande, bd=4)
boton_3.grid(row=5, column=3, padx=5)
boton_cerrar = tk.Button(esc, text="CERRAR", width=6, height=1, bg="lightgrey",fg="black", relief="raised", command=parar, font=peque1, bd=4)
boton_cerrar.grid(row=10, column=3, padx=4, sticky="ne")

# Definir el cliente Modbus
client = ModbusTcpClient('192.168.1.145', port=502)

try:
    # Intentar conectarse al servidor Modbus
    client.connect()

    if client.connect():
       
        pedir_bool()
   
    else:
        error.config(text="Error al conectar", bg="red")

    # Configurar el tamaño de la ventana principal para que se ajuste automáticamente al tamaño del contenido

    root.mainloop()  # Ejecutar runtime

except Exception as e:
    error.config(text="Error1: " + e, bg="red")

finally:
    client.close()  # Asegurarnos de cerrar la conexión Modbus si hay un error
