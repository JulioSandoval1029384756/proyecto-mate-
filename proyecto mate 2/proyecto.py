import tkinter as tk

def calcular_placas():
    digitos = 3
    letras = 26
    placas = 1

    for _ in range(digitos):
        placas *= 10

    for _ in range(3):
        placas *= letras

    return placas

def operacion_conjuntos(A, B):
    resultado = []

    for elemento in A:
        if elemento not in B:
            resultado.append(elemento)

    return resultado

def euclidean_algorithm(a, b):
    procedure = []
    while b:
        q = a // b
        r = a % b
        procedure.append(f"{a} = {b} * {q} + {r}")
        a, b = b, r

    return a, procedure

def calcular_resultados():
    # Calcular resultados y procedimientos para cada ejercicio
    total_placas = calcular_placas()
    resultado_A_B = operacion_conjuntos(A, B)
    mcd, procedure = euclidean_algorithm(num1, num2)

    # Mostrar los resultados y procedimientos en orden
    resultados_procedimientos = []

    resultados_procedimientos.append(f"1. Placas emitidas en Guatemala: {total_placas}")
    resultados_procedimientos.append("Procedimiento del ejercicio 1 (Cálculo del total de placas):")
    resultados_procedimientos.append("1.1. Se multiplican 3 dígitos por 10 posibles dígitos (0-9) para obtener 1000 combinaciones.")
    resultados_procedimientos.append("1.2. Luego, se multiplican 3 letras por 26 posibles letras (A-Z) para obtener 17576 combinaciones.")
    resultados_procedimientos.append("1.3. Finalmente, se multiplican los resultados anteriores para obtener el total de placas: 1000 * 17576 = 17,576,000")
    
    resultados_procedimientos.append(f"2. Resultado de A - B: {resultado_A_B}")
    resultados_procedimientos.append("Procedimiento del ejercicio 2 (Operación de conjuntos A - B):")
    resultados_procedimientos.append("2.1. Comparamos los elementos de A con los elementos de B.")
    resultados_procedimientos.append("2.2. Cualquier elemento que esté en A pero no en B se incluye en el resultado.")
    resultados_procedimientos.append("2.3. Resultado de A - B: {2, 3, 4, 5, 6, 7, k, m}")

    resultados_procedimientos.append(f"3. MCD de 19 y 35: {mcd}")
    resultados_procedimientos.append("Procedimiento del ejercicio 3 (Cálculo del MCD usando el Algoritmo de Euclides):")
    resultados_procedimientos.extend(procedure)

    resultado_label.config(text="\n\n".join(resultados_procedimientos))

# Crear la ventana principal
window = tk.Tk()
window.title("Resultados de Ejercicios")

# Ajustar el tamaño de la ventana
window.geometry("1000x800")  # Ancho x Alto

# Ajustar el tamaño de fuente
font = ("Arial", 12)

# Definir los conjuntos y números
A = {'a', 2, 'c', 3, 'e', 4, 'g', 5, 'i', 6, 'k', 7, 'm'}
B = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
num1 = 19
num2 = 35

# Botón para calcular resultados
calcular_button = tk.Button(window, text="Calcular Resultados", command=calcular_resultados, font=font)
calcular_button.pack(pady=10)

# Etiqueta para mostrar los resultados
resultado_label = tk.Label(window, text="", justify="left", font=font)
resultado_label.pack(padx=10)

window.mainloop()





