from flask import Flask, render_template, request

# Da inicio a la aplicación Flask
app = Flask(__name__)

# --- RUTA PRINCIPAL (MENÚ) ---
@app.route('/')
def index():
    """Renderiza la plantilla principal con el menú."""
    return render_template('index.html')

# --- RUTA EJERCICIO 1 (NOTAS Y ESTADO) ---
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    """Muestra el formulario y procesa las notas y asistencia."""
# Si la solicitud es POST (se envia el formulario)
    if request.method == 'POST':
        try:
# 1. Recoger y convertir los datos a float
            nota1 = float(request.form.get('nota1'))
            nota2 = float(request.form.get('nota2'))
            nota3 = float(request.form.get('nota3'))
            asistencia = float(request.form.get('asistencia'))

# 2. Calcula el promedio
            promedio = (nota1 + nota2 + nota3) / 3

# 3. Determina el estado (APROBADO: Promedio >= 40 Y Asistencia >= 75%)
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

# 4. Mostrara el resultado
            return render_template('resultado1.html',
                                   promedio=f"{promedio:.1f}",  # Formatea a un decimal
                                   estado=estado)

        except ValueError:
# Manejo de errores si los datos no son numéricos
            return "Error: Por favor, ingrese valores numéricos válidos.", 400

# Si la solicitud es GET (nos mostrar el formulario)
    return render_template('ejercicio1.html')


# --- RUTA EJERCICIO 2 (NOMBRE MÁS LARGO) ---
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    """Muestra el formulario y encuentra el nombre con más caracteres."""
    if request.method == 'POST':
# 1. Recoger los 3 nombres
        nombre1 = request.form.get('nombre1', '').strip()
        nombre2 = request.form.get('nombre2', '').strip()
        nombre3 = request.form.get('nombre3', '').strip()

# 2. Encontrar el nombre con la longitud máxima (más caracteres)
        nombres_lista = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres_lista, key=len)
        largo_nombre = len(nombre_mas_largo)

# (Opcional: podemos eliminar el diccionario 'nombres' que no se usa)

# 3. Mostrar el resultado
        return render_template('resultado2.html',
                               nombre_mas_largo=nombre_mas_largo,
                               largo_nombre=largo_nombre)

# Si la solicitud es GET (mostrara el formulario)
    return render_template('ejercicio2.html')


# --- EJECUCIÓN DE LA APLICACIÓN ---
# Este bloque siempre debe ir al final
if __name__ == '__main__':
# Utilizamos debug=True para el desarrollo
    app.run(debug=True)