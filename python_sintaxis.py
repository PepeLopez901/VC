# ============================================================
#  GUÍA DE SINTAXIS DE PYTHON - Ejemplos prácticos
# ============================================================

# -------------------------
# 1. VARIABLES Y TIPOS DE DATOS
# -------------------------
entero      = 10
flotante    = 3.14
texto       = "Hola, mundo"
booleano    = True
nulo        = None

print(type(entero))     # <class 'int'>
print(type(flotante))   # <class 'float'>
print(type(texto))      # <class 'str'>
print(type(booleano))   # <class 'bool'>


# -------------------------
# 2. OPERADORES
# -------------------------
# Aritméticos
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3  (división entera)
print(10 % 3)   # 1  (módulo/resto)
print(2 ** 8)   # 256 (potencia)

# Comparación
print(5 == 5)   # True
print(5 != 3)   # True
print(5 >= 3)   # True

# Lógicos
print(True and False)  # False
print(True or False)   # True
print(not True)        # False


# -------------------------
# 3. CADENAS DE TEXTO (str)
# -------------------------
nombre = "Python"
print(nombre.upper())           # PYTHON
print(nombre.lower())           # python
print(nombre.replace("P", "J")) # Jython
print(len(nombre))              # 6
print(nombre[0])                # P  (indexación)
print(nombre[1:4])              # yth (slicing)

# f-strings (formato moderno)
version = 3.12
print(f"Lenguaje: {nombre}, versión: {version}")

# Multilínea
multi = """
Primera línea
Segunda línea
Tercera línea
"""
print(multi)


# -------------------------
# 4. LISTAS
# -------------------------
frutas = ["manzana", "pera", "uva", "mango"]
frutas.append("kiwi")       # agregar al final
frutas.insert(1, "limón")   # insertar en posición
frutas.remove("pera")       # eliminar por valor
print(frutas[0])            # manzana
print(frutas[-1])           # último elemento
print(frutas[1:3])          # sublista
print(len(frutas))          # cantidad de elementos

# Recorrer lista
for fruta in frutas:
    print(fruta)

# List comprehension
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]


# -------------------------
# 5. TUPLAS
# -------------------------
coordenada = (10, 20)
print(coordenada[0])  # 10
# Las tuplas son inmutables (no se pueden modificar)

x, y = coordenada   # desempaquetado
print(x, y)         # 10 20


# -------------------------
# 6. DICCIONARIOS
# -------------------------
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

print(persona["nombre"])        # Ana
print(persona.get("pais", "N/A"))  # N/A (valor por defecto)

persona["profesion"] = "Ingeniera"  # agregar clave
persona["edad"] = 31                # modificar valor
del persona["ciudad"]               # eliminar clave

for clave, valor in persona.items():
    print(f"{clave}: {valor}")


# -------------------------
# 7. CONJUNTOS (set)
# -------------------------
colores = {"rojo", "verde", "azul", "rojo"}  # sin duplicados
print(colores)

colores.add("amarillo")
colores.discard("verde")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # unión
print(a & b)   # intersección
print(a - b)   # diferencia


# -------------------------
# 8. CONDICIONALES
# -------------------------
edad = 18

if edad >= 18:
    print("Mayor de edad")
elif edad >= 13:
    print("Adolescente")
else:
    print("Niño")

# Operador ternario
estado = "mayor" if edad >= 18 else "menor"
print(estado)


# -------------------------
# 9. BUCLES
# -------------------------
# for con range
for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4
print()

# for con enumerate
animales = ["perro", "gato", "pez"]
for indice, animal in enumerate(animales):
    print(f"{indice}: {animal}")

# while
contador = 0
while contador < 5:
    print(contador, end=" ")
    contador += 1
print()

# break y continue
for n in range(10):
    if n == 3:
        continue    # salta el 3
    if n == 7:
        break       # termina al llegar a 7
    print(n, end=" ")
print()


# -------------------------
# 10. FUNCIONES
# -------------------------
def saludar(nombre, saludo="Hola"):
    """Función con parámetro por defecto."""
    return f"{saludo}, {nombre}!"

print(saludar("Carlos"))            # Hola, Carlos!
print(saludar("Laura", "Buenos días"))  # Buenos días, Laura!

# *args y **kwargs
def sumar(*numeros):
    return sum(numeros)

def mostrar_info(**datos):
    for k, v in datos.items():
        print(f"  {k} = {v}")

print(sumar(1, 2, 3, 4, 5))           # 15
mostrar_info(nombre="Luis", edad=25)

# Funciones lambda
doble = lambda x: x * 2
print(doble(7))   # 14

cuadrado = lambda x: x ** 2
numeros = [1, 2, 3, 4, 5]
print(list(map(cuadrado, numeros)))          # [1, 4, 9, 16, 25]
print(list(filter(lambda x: x > 2, numeros)))  # [3, 4, 5]


# -------------------------
# 11. CLASES Y OBJETOS (POO)
# -------------------------
class Animal:
    # Atributo de clase
    reino = "Animalia"

    def __init__(self, nombre, sonido):
        # Atributos de instancia
        self.nombre = nombre
        self.sonido = sonido

    def hablar(self):
        return f"{self.nombre} dice: {self.sonido}"

    def __str__(self):
        return f"Animal({self.nombre})"


class Perro(Animal):
    """Clase que hereda de Animal."""

    def __init__(self, nombre):
        super().__init__(nombre, "Guau")

    def buscar(self, objeto):
        return f"{self.nombre} busca {objeto}!"


mi_perro = Perro("Rex")
print(mi_perro.hablar())       # Rex dice: Guau
print(mi_perro.buscar("pelota"))  # Rex busca pelota!
print(mi_perro.reino)          # Animalia
print(mi_perro)                # Animal(Rex)


# -------------------------
# 12. MANEJO DE EXCEPCIONES
# -------------------------
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero"
    except TypeError as e:
        return f"Error de tipo: {e}"
    else:
        return resultado
    finally:
        print("Operación finalizada")

print(dividir(10, 2))    # 5.0
print(dividir(10, 0))    # Error: no se puede dividir entre cero


# -------------------------
# 13. MÓDULOS ÚTILES DE LA LIBRERÍA ESTÁNDAR
# -------------------------
import math
import random
import datetime

# math
print(math.sqrt(144))          # 12.0
print(math.pi)                 # 3.14159...
print(math.floor(3.7))         # 3

# random
print(random.randint(1, 100))  # número aleatorio entre 1 y 100
print(random.choice(frutas))   # elemento aleatorio de la lista

# datetime
hoy = datetime.date.today()
ahora = datetime.datetime.now()
print(f"Hoy: {hoy}")
print(f"Ahora: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")


# -------------------------
# 14. COMPRENSIONES (avanzado)
# -------------------------
# Dict comprehension
cuadros = {x: x**2 for x in range(1, 6)}
print(cuadros)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension
pares = {x for x in range(10) if x % 2 == 0}
print(pares)    # {0, 2, 4, 6, 8}

# Generador (lazy evaluation)
gen = (x**2 for x in range(1, 6))
print(next(gen))  # 1
print(next(gen))  # 4


# -------------------------
# 15. LECTURA/ESCRITURA DE ARCHIVOS
# -------------------------
# Escribir archivo
with open("ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")

# Leer archivo completo
with open("ejemplo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# Leer línea por línea
with open("ejemplo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())



# ============================================================
# 16. AJAX DESDE JAVASCRIPT (referencia incluida en este archivo)
#     Nota: este bloque es JavaScript, no Python.
#     Se incluye aquí como referencia complementaria.
# ============================================================

"""
// -------------------------------------------------------
// OPCIÓN 1 — XMLHttpRequest (forma clásica)
// -------------------------------------------------------

const xhr = new XMLHttpRequest();
xhr.open("GET", "https://jsonplaceholder.typicode.com/users/1", true);

xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        const datos = JSON.parse(xhr.responseText);
        console.log(datos);
    }
};

xhr.send();


// -------------------------------------------------------
// OPCIÓN 2 — fetch() con GET (forma moderna)
// -------------------------------------------------------

fetch("https://jsonplaceholder.typicode.com/users/1")
    .then(response => {
        if (!response.ok) {
            throw new Error("Error en la petición: " + response.status);
        }
        return response.json();
    })
    .then(datos => {
        console.log(datos);
    })
    .catch(error => {
        console.error("Error:", error);
    });


// -------------------------------------------------------
// OPCIÓN 3 — fetch() con POST y JSON en el cuerpo
// -------------------------------------------------------

const nuevoUsuario = {
    nombre: "Juan",
    correo: "juan@example.com"
};

fetch("https://jsonplaceholder.typicode.com/users", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(nuevoUsuario)
})
    .then(response => response.json())
    .then(data => {
        console.log("Usuario creado:", data);
    })
    .catch(error => {
        console.error("Error:", error);
    });


// -------------------------------------------------------
// OPCIÓN 4 — async / await (la más limpia y recomendada)
// -------------------------------------------------------

async function obtenerUsuario(id) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const usuario = await response.json();
        console.log(usuario);
        return usuario;

    } catch (error) {
        console.error("Error al obtener usuario:", error);
    }
}

obtenerUsuario(1);


// -------------------------------------------------------
// OPCIÓN 5 — async / await con POST
// -------------------------------------------------------

async function crearPost(titulo, cuerpo) {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title: titulo, body: cuerpo, userId: 1 })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        const resultado = await response.json();
        console.log("Post creado:", resultado);

    } catch (error) {
        console.error("Error al crear post:", error);
    }
}

crearPost("Mi título", "Contenido del post");


// -------------------------------------------------------
// OPCIÓN 6 — jQuery AJAX 
//            (requiere incluir jQuery en el HTML:
//             <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>)
// -------------------------------------------------------

// GET con jQuery
$.ajax({
    url: "https://jsonplaceholder.typicode.com/users/1",
    method: "GET",
    success: function (data) {
        console.log("Éxito:", data);
    },
    error: function (xhr, status, error) {
        console.error("Error:", error);
    }
});

// POST con jQuery
$.ajax({
    url: "https://jsonplaceholder.typicode.com/posts",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({ title: "Hola", body: "Mundo", userId: 1 }),
    success: function (data) {
        console.log("Creado:", data);
    },
    error: function (xhr, status, error) {
        console.error("Error:", error);
    }
});
"""

# ============================================================
# FIN DEL ARCHIVO
# ============================================================
