import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    print(f"\nIntentando abrir: {ruta_script_absoluta}")
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            print("\n--- Resultado de la ejecución ---\n")
            exec(codigo, globals())
    except FileNotFoundError:
        print(" El archivo no se encontró.")
    except Exception as e:
        print(f" Ocurrió un error al leer o ejecutar el archivo: {e}")

def mostrar_menu():
    # Subimos dos niveles hasta el directorio raíz del proyecto
    ruta_base = os.path.abspath(os.path.join(os.getcwd(), '..', '..'))

    opciones = {
        '1': [
            'Parcial 01/Semana 02/Ejemplo de abstraccion.py',
            'Parcial 01/Semana 02/Ejemplo de Encapsulacion.py',
            'Parcial 01/Semana 02/Ejemplo de Herencia.py',
            'Parcial 01/Semana 02/Ejemplo de Polimorfismo.py'
        ],

        '2': [
            'Parcial 01/semana 03/Programación Orientada a Objetos (POO).py',
            'Parcial 01/semana 03/Programación Tradicional.py'
        ],
        '3': 'Parcial 01/Semana 04/EjemplosMundoReal_POO.py',
        '4': 'Parcial 01/Semana 05/Calcular area de un rectangulo.py',
        '5': 'Parcial 01/Semana 06/.Aplicación de Conceptos de POO en Python.py',
        '6': 'Parcial 01/Semana 07/Implementación de Constructores y Destructores en Python.py',
    }

    while True:
        print("\n Menú Principal - Dashboard")
        for key, value in opciones.items():
            label = f"{len(value)} archivos" if isinstance(value, list) else value
            print(f"{key} - {label}")
        print("0 - Salir")

        eleccion = input("Elige una opción para ver su(s) script(s) o '0' para salir: ")
        if eleccion == '0':
            print("¡Hasta luego!")
            break
        elif eleccion in opciones:
            rutas = opciones[eleccion]
            if isinstance(rutas, list):
                for ruta_relativa in rutas:
                    ruta_script = os.path.join(ruta_base, ruta_relativa)
                    mostrar_codigo(ruta_script)
            else:
                ruta_script = os.path.join(ruta_base, rutas)
                mostrar_codigo(ruta_script)
        else:
            print(" Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
