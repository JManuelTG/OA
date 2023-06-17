# Standart library
import random
import os
import time
import re
import signal

# Extra libraries
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Función para manejar la señal de Ctrl+C
def signal_handler(signal, frame):
    """
    Function that prints a messege when program ends
    """
    print('\nPrograma detenido')
    exit(0)

# Función para obtener los datos de la tabla
def get_table_data():
    """
    Function that send an get petition and gets a table of the website
    """
    response = requests.get(url, timeout=None)

    # Analizar el contenido HTML de la página web
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar la tabla por su etiqueta <table> o cualquier otro selector adecuado
    table = soup.find("table")

    # Encontrar todas las filas de la tabla
    rows = table.find_all("tr")

    # Crear una lista de listas para almacenar los datos de la tabla
    list_of_data = []

    # Recorrer las filas e imprimir los datos de cada celda
    for line in rows:
        cells = line.find_all("td")
        if len(cells) >= 7:  # Verificar la longitud de la lista cells
            row_data = [
                cells[0].get_text(strip=True),
                cells[1].get_text(strip=True),
                cells[2].get_text(strip=True),
                cells[5].get_text(strip=True),
                cells[6].get_text(strip=True),
                cells[9].get_text(strip=True),
                cells[10].get_text(strip=True),
                cells[16].get_text(strip=True)
            ]
            list_of_data.append(row_data)

    return list_of_data

# Función para mostrar el tiempo transcurrido desde el inicio del programa
def show_elapsed_time(current_time):
    """
    Function that works as a clock to print in console the time since the program starts
    """
    elapsed_time = time.time() - current_time

    # Convertir el tiempo transcurrido a minutos y segundos
    if elapsed_time < 60:
        print("Tiempo transcurrido: {:.2f} segundos".format(elapsed_time))
    elif elapsed_time < 3600:
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        print("Tiempo transcurrido: {} minutos {} segundos".format(int(minutes), int(seconds)))
    else:
        hours = elapsed_time // 3600
        remaining_time = elapsed_time % 3600
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print("Tiempo transcurrido: {} horas {} minutos {} segundos".format(int(hours),
                                                                            int(minutes),
                                                                            int(seconds)))

# Función auxiliar para formatear los valores de las columnas "CUPOS" y "DIS" con colores
def format_value_with_color(data):
    """
    Fuction that gives color dependid the type of data
    """
    try:
        # Verifica si el valor es un numero
        if data.isdigit():
            data = int(data)
            # Cacha el NRC de la materia
            if len(str(data)) > 3:
                return Fore.MAGENTA + str(data)
            elif data > 0:
                return Fore.GREEN + str(data)
            else:
                return Fore.RED + str(data)
        elif re.search(r"^[A-Z]{1,2}\d+",data):
            return Fore.BLUE + str(data)
        else:
            return Fore.WHITE + str(data)
    except ValueError:
        return data

centros = {
    '3':"C. U. DE TLAJOMULCO.",
    'A':"C.U. DE ARTE, ARQ. Y DISEÑO.",
    'B':"C.U. DE CS. BIOLOGICO Y AGR.",
    'C':"C.U. DE CS. ECONOMICO-ADMVAS.",
    'D':"C.U. DE CS. EXACTAS E ING.",
    'E':"C.U. DE CS. DE LA SALUD.",
    'F':"C.U. DE CS. SOCIALES Y HUM.",
    'G':"C.U. DE LOS ALTOS.",
    'H':"C.U. DE LA CIENEGA.",
    'I':"C.U. DE LA COSTA.",
    'J':"C.U. DE LA COSTA SUR."
}

if __name__ == "__main__":
    # Centros universitarios
    print("CENTROS UNIVERSITARIOS\n")
    for key, value in centros.items():
        print(f"{key} = {value}")

    # Obtener centro universitario
    centro = str(input("\nIngrese el numero/letra del centro: ")).upper().strip()
    if not centro:
        centro = "D"

    # Limpia la consola antes de imprimir la siguiente iteración
    os.system('cls' if os.name == 'nt' else 'clear')

    # Ciclos escolares
    print("CICLOS\n")
    print("202320 = Calendario B.")
    print("202310 = Calendario A.")
    print("NOTA: Solo se agrega un 20 al anio en caso de que el calendario sea B"
          "o un 10 si es el calendario A")

    # Obtener ciclo del cual se quiere checar la oferta
    ciclo = str(input("Ingrese el ciclo escolar (Default 202320 ---> 2023B): ")).strip()
    if not ciclo:
        ciclo = "202320"

    # Limpia la consola antes de imprimir la siguiente iteración
    os.system('cls' if os.name == 'nt' else 'clear')

    # Obtener ciclo del cual se quiere checar la oferta
    materia = str(input("Ingrese clave de materia: ")).strip()
    if not materia:
        raise ValueError("Error, no ingresaste una materia")

    print(f"Recibiendo informacion de: {centros[centro]}, Ciclo: {ciclo}, Materia: {materia}")

    # Obtener el contenido HTML de la página
    base_url = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?"
    url = base_url + f"ciclop={ciclo}&cup={centro}&crsep={materia}"

    # Establecer el manejador de señal para Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Contador de veces que se revisa la oferta
    iter_count = 0

    # Headers de las columnas que se van a imprimir
    headers = ["NRC", "CLAVE", "MATERIA", "CUPOS", "DIS", "HORARIO", "DIAS", "MAESTRO"]

    try:
        # Iniciar el temporizador
        start_time = time.time()
        while True:
            # Esperar 5 segundos
            time.sleep(random.randint(2, 5))

            # Limpia la consola antes de imprimir la siguiente iteración
            os.system('cls' if os.name == 'nt' else 'clear')

            # Obtener y mostrar los datos actualizados de la tabla
            table_data = get_table_data()
            formatted_table_data = []
            for row in table_data:
                formatted_row = [format_value_with_color(value) for value in row]
                formatted_table_data.append(formatted_row)

            print(tabulate(formatted_table_data, headers=headers, tablefmt="simple"))
            print(f"Iteraciones: {iter_count}")
            iter_count += 1

            # Mostrar el tiempo transcurrido
            show_elapsed_time(start_time)
            print("Presiona CTRL + C para cerrar el programa")

    except KeyboardInterrupt:
        print('\nPrograma detenido')
