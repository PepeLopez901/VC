# ============================================================
#  PUNTO DE ENTRADA — app.py
#  Configura Flask y registra las rutas (URLs → Controllers).
#
#  Instalación previa:
#      pip install flask
#
#  Ejecutar:
#      python app.py
#
#  Luego abrir en el navegador:
#      http://127.0.0.1:5000
# ============================================================

from flask import Flask
import controllers

app = Flask(__name__)


# -------------------------------------------------------
# RUTAS  (URL → función del controlador)
# -------------------------------------------------------

# Página principal: lista de productos
app.add_url_rule("/",               "lista",        controllers.index)

# Detalle de un producto
app.add_url_rule("/producto/<int:id>", "detalle",   controllers.detalle)

# Filtrar por categoría: /categoria/Electronica
app.add_url_rule("/categoria/<string:categoria>", "categoria", controllers.por_categoria)

# Crear producto (GET = formulario, POST = guardar)
app.add_url_rule("/nuevo",          "nuevo",        controllers.crear,   methods=["GET", "POST"])

# Eliminar producto
app.add_url_rule("/eliminar/<int:id>", "eliminar",  controllers.eliminar, methods=["POST"])

# -------------------------------------------------------
# RUTAS API REST (devuelven JSON)
# -------------------------------------------------------
app.add_url_rule("/api/productos",        "api_productos", controllers.api_productos)
app.add_url_rule("/api/productos/<int:id>", "api_producto", controllers.api_producto)


# -------------------------------------------------------
# INICIO DE LA APLICACIÓN
# -------------------------------------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("  Servidor MVC con Flask iniciado")
    print("  Abre: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True)
