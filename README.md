# Oferta Académica - Documentación

Este script accede a la oferta académica de cursos de una universidad y muestra en la consola los cupos disponibles, horarios, claves de materia y nombres de los maestros.

![Pantallazo del script funcionando](https://github.com/JManuelTG/OfertaAcademica/assets/111461062/958535a1-8c6e-4667-ade0-9e6cdd666489)
Pantallazo del script fuincionando

## Dependencias

El script utiliza las siguientes bibliotecas externas:

- `requests`: Para enviar solicitudes HTTP y obtener el contenido HTML de la página web de la oferta académica.
- `BeautifulSoup`: Para analizar el contenido HTML y extraer los datos relevantes de la tabla.
- `tabulate`: Para formatear los datos en forma de tabla y mostrarlos en la consola.
- `colorama`: Para agregar color a los valores de las columnas "CUPOS" y "DIS" en la consola.

Asegúrate de tener estas bibliotecas instaladas antes de ejecutar el script.

## Funciones principales

El script consta de las siguientes funciones principales:

- `signal_handler(signal, frame)`: Función para manejar la señal de Ctrl+C y detener el programa correctamente.
- `get_table_data()`: Función que obtiene los datos de la tabla de la página web de la oferta académica.
- `show_elapsed_time(current_time)`: Función que muestra el tiempo transcurrido desde el inicio del programa.
- `format_value_with_color(data)`: Función auxiliar que formatea los valores de las columnas "CUPOS" y "DIS" con colores.

## Uso

1. Asegúrate de tener todas las dependencias instaladas.
2. Ejecuta el script en un entorno de Python.
3. El programa solicitará la información necesaria:
   - Centro universitario: Ingresa el número o letra correspondiente al centro universitario.
   - Ciclo escolar: Ingresa el ciclo escolar en el formato adecuado (ejemplo: 202320).
   - Clave de materia: Ingresa la clave de la materia que deseas consultar en la oferta académica.
4. El programa mostrará en la consola los datos actualizados de la oferta académica, incluyendo cupos disponibles, horarios, claves de materia y nombres de los maestros.
5. El programa continuará actualizando y mostrando los datos en la consola cada cierto intervalo de tiempo hasta que se presione Ctrl+C para detenerlo.

## Notas

- Asegúrate de ajustar las variables y configuraciones del script según las particularidades de la página web de la oferta académica de tu universidad.
- Ten en cuenta que este script es solo un esqueleto y puede requerir modificaciones adicionales para que funcione correctamente con tu universidad y los datos específicos que deseas obtener.
- No olvides respetar los términos y condiciones de uso de la página web de la oferta académica de tu universidad al utilizar este script.
