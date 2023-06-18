import random
import os
import time
import re
import signal
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)

def signal_handler(signal, frame):
    """
    Manejador de señal para Ctrl+C. Imprime un mensaje y finaliza el programa.
    """
    print('\nPrograma detenido')
    exit(0)

def get_table_data(url):
    """
    Obtiene los datos de la tabla de la página web especificada por la URL.
    Devuelve una lista de listas que representa los datos de la tabla.
    """
    response = requests.get(url, timeout=None)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    list_of_data = []
    for line in rows:
        cells = line.find_all("td")
        if len(cells) >= 7:
            row_data = [cells[0].get_text(strip=True), cells[1].get_text(strip=True),
                        cells[2].get_text(strip=True), cells[5].get_text(strip=True),
                        cells[6].get_text(strip=True), cells[9].get_text(strip=True),
                        cells[10].get_text(strip=True), cells[16].get_text(strip=True)]
            list_of_data.append(row_data)
    return list_of_data

def show_elapsed_time(current_time):
    """
    Muestra el tiempo transcurrido desde el inicio del programa en minutos y segundos.
    """
    elapsed_time = time.time() - current_time
    if elapsed_time < 60:
        print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")
    elif elapsed_time < 3600:
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        print(f"Tiempo transcurrido: {int(minutes)} minutos {int(seconds)} segundos")
    else:
        hours = elapsed_time // 3600
        remaining_time = elapsed_time % 3600
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"Tiempo transcurrido: {int(hours)} horas {int(minutes)} minutos {int(seconds)} segundos")

def format_value_with_color(data):
    """
    Da formato al valor con color dependiendo del tipo de dato.
    """
    try:
        if data.isdigit():
            data = int(data)
            if len(str(data)) > 3:
                return Fore.MAGENTA + str(data)
            elif data > 0:
                return Fore.GREEN + str(data)
            else:
                return Fore.RED + str(data)
        elif re.search(r"^[A-Z]{1,2}\d+", data):
            return Fore.BLUE + str(data)
        else:
            return Fore.WHITE + str(data)
    except ValueError:
        return data

centros = {
    '3': "C. U. DE TLAJOMULCO.",
    'A': "C.U. DE ARTE, ARQ. Y DISEÑO.",
    'B': "C.U. DE CS. BIOLOGICO Y AGR.",
    'C': "C.U. DE CS. ECONOMICO-ADMVAS.",
    'D': "C.U. DE CS. EXACTAS E ING.",
    'E': "C.U. DE CS. DE LA SALUD.",
    'F': "C.U. DE CS. SOCIALES Y HUM.",
    'G': "C.U. DE LOS ALTOS.",
    'H': "C.U. DE LA CIENEGA.",
    'I': "C.U. DE LA COSTA.",
    'J': "C.U. DE LA COSTA SUR."
}

if __name__ == "__main__":
    print("CENTROS UNIVERSITARIOS\n")
    for key, value in centros.items():
        print(f"{key} = {value}")

    centro = input("\nIngrese el número/letra del centro: ").strip().upper() or "D"
    os.system('cls' if os.name == 'nt' else 'clear')

    print("CICLOS\n")
    print("202320 = Calendario B.")
    print("202310 = Calendario A.")
    print("NOTA: Solo se agrega un 20 al año en caso de que el calendario sea B"
          "o un 10 si es el calendario A")

    ciclo = input("Ingrese el ciclo escolar (Default 202320 ---> 2023B): ").strip() or "202320"
    os.system('cls' if os.name == 'nt' else 'clear')

    materia = input("Ingrese clave de materia: ").strip()
    if not materia:
        raise ValueError("Error, no ingresaste una materia")

    print(f"Recibiendo información de: {centros[centro]}, Ciclo: {ciclo}, Materia: {materia}")

    base_url = "http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?"
    url = base_url + f"ciclop={ciclo}&cup={centro}&crsep={materia}"

    signal.signal(signal.SIGINT, signal_handler)
    iter_count = 1
    headers = ["NRC", "CLAVE", "MATERIA", "CUPOS", "DIS", "HORARIO", "DIAS", "MAESTRO"]

    try:
        start_time = time.time()
        while True:
            time.sleep(random.randint(2, 5))
            os.system('cls' if os.name == 'nt' else 'clear')
            table_data = get_table_data(url)
            formatted_table_data = [[format_value_with_color(value) for value in row] for row in table_data]
            print(tabulate(formatted_table_data, headers=headers, tablefmt="simple"))
            print(f"Iteraciones: {iter_count}")
            iter_count += 1
            show_elapsed_time(start_time)
            print("Presiona CTRL + C para cerrar el programa")

    except KeyboardInterrupt:
        print('\nPrograma detenido')
