# ============================================================
#  CAPA CONTROLLER — controllers.py
#  Recibe las peticiones, llama al Model y selecciona la View.
#  Actúa como intermediario entre datos y presentación.
# ============================================================

from flask import render_template, request, redirect, url_for, jsonify
import models


# -------------------------------------------------------
# Controlador: Página principal — lista todos los productos
# -------------------------------------------------------
def index():
    productos = models.obtener_todos()
    return render_template("index.html", productos=productos)


# -------------------------------------------------------
# Controlador: Detalle de un producto por ID
# -------------------------------------------------------
def detalle(id):
    producto = models.obtener_por_id(id)
    if producto is None:
        return render_template("error.html", mensaje=f"Producto con ID {id} no encontrado."), 404
    return render_template("detalle.html", producto=producto)


# -------------------------------------------------------
# Controlador: Filtrar por categoría
# -------------------------------------------------------
def por_categoria(categoria):
    productos = models.obtener_por_categoria(categoria)
    return render_template("index.html", productos=productos, categoria=categoria)


# -------------------------------------------------------
# Controlador: Crear nuevo producto (POST)
# -------------------------------------------------------
def crear():
    if request.method == "POST":
        nombre    = request.form.get("nombre", "").strip()
        precio    = request.form.get("precio", 0)
        categoria = request.form.get("categoria", "").strip()

        if not nombre or not categoria:
            return render_template("formulario.html", error="Nombre y categoría son obligatorios.")

        try:
            precio = float(precio)
        except ValueError:
            return render_template("formulario.html", error="El precio debe ser un número.")

        models.agregar(nombre, precio, categoria)
        return redirect(url_for("lista"))   # redirige al index después de crear

    # GET: muestra el formulario vacío
    return render_template("formulario.html")


# -------------------------------------------------------
# Controlador: Eliminar producto (POST con ID)
# -------------------------------------------------------
def eliminar(id):
    eliminado = models.eliminar(id)
    if not eliminado:
        return render_template("error.html", mensaje=f"No se encontró el producto {id}."), 404
    return redirect(url_for("lista"))


# -------------------------------------------------------
# Controlador: API REST — devuelve productos en JSON
# -------------------------------------------------------
def api_productos():
    productos = models.obtener_todos()
    return jsonify([p.to_dict() for p in productos])


def api_producto(id):
    producto = models.obtener_por_id(id)
    if producto is None:
        return jsonify({"error": "No encontrado"}), 404
    return jsonify(producto.to_dict())
