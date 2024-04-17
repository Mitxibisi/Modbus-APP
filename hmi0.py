
from pymodbus.client import ModbusTcpClient

# Configuración del cliente Modbus
cliente_modbus = ModbusTcpClient('192.168.1.145', 502)

try:
    # Conectar al servidor Modbus
    cliente_modbus.connect()
    cliente_modbus.write_coil(1,True)
    # Leer el registro donde se encuentra la variable compartida booleana
    resultado = cliente_modbus.read_coils(0, 1,slave=1)  # Leemos 1 coil empezando desde el registro 0

    if resultado.isError():
        print("Error al leer registros.")
    else:
        valor_booleano = resultado.bits[0]  # Obtenemos el valor booleano del primer registro
        print("Valor booleano:", valor_booleano)

except Exception as e:
    print("Error:", e)

finally:
    # Desconectar del servidor Modbus
    cliente_modbus.close()