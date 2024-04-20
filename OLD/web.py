from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página de inicio
@app.route('/')
def index():
    return '¡Hola, mundo! Este es mi iniciador web con Flask.'

# Si ejecutamos este script directamente, arrancará el servidor web
if __name__ == '__main__':
    app.run(debug=True)

