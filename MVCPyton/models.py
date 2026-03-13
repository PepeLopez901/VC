# ============================================================
#  CAPA MODEL — models.py
#  Representa los datos y la lógica de negocio.
#  En un proyecto real esto se conectaría a una base de datos
#  (SQLAlchemy, Django ORM, etc.). Aquí usamos datos en memoria.
# ============================================================

class Producto:
    """Modelo que representa un Producto."""

    def __init__(self, id, nombre, precio, categoria):
        self.id        = id
        self.nombre    = nombre
        self.precio    = precio
        self.categoria = categoria

    def to_dict(self):
        """Convierte el objeto a diccionario (útil para JSON / templates)."""
        return {
            "id":        self.id,
            "nombre":    self.nombre,
            "precio":    self.precio,
            "categoria": self.categoria
        }

    def __repr__(self):
        return f"Producto({self.id}, {self.nombre}, ${self.precio})"


# -------------------------------------------------------
# "Base de datos" simulada en memoria
# -------------------------------------------------------
_productos = [
    Producto(1, "Laptop",   15000.00, "Electrónica"),
    Producto(2, "Teclado",    850.00, "Electrónica"),
    Producto(3, "Escritorio", 3200.00, "Muebles"),
    Producto(4, "Silla",      2100.00, "Muebles"),
    Producto(5, "Monitor",    6500.00, "Electrónica"),
]


# -------------------------------------------------------
# Funciones del modelo (acceso a datos)
# -------------------------------------------------------

def obtener_todos():
    """Devuelve todos los productos."""
    return _productos


def obtener_por_id(id):
    """Busca un producto por su ID. Retorna None si no existe."""
    return next((p for p in _productos if p.id == id), None)


def obtener_por_categoria(categoria):
    """Filtra productos por categoría (búsqueda insensible a mayúsculas)."""
    return [p for p in _productos if p.categoria.lower() == categoria.lower()]


def agregar(nombre, precio, categoria):
    """Agrega un nuevo producto y devuelve el objeto creado."""
    nuevo_id = max(p.id for p in _productos) + 1
    nuevo = Producto(nuevo_id, nombre, precio, categoria)
    _productos.append(nuevo)
    return nuevo


def eliminar(id):
    """Elimina un producto por ID. Retorna True si se eliminó, False si no existe."""
    global _productos
    original = len(_productos)
    _productos = [p for p in _productos if p.id != id]
    return len(_productos) < original
