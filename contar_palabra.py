# Problema: contar cuántas veces aparece una palabra en un archivo de texto.
# Uso: python contar_palabra.py archivo.txt palabra

import sys

# Entrada (argumentos al ejecutar el script)
nombre_archivo = sys.argv[1]
palabra = sys.argv[2]

# Proceso
archivo = open(nombre_archivo, "r", encoding="utf-8")
texto = archivo.read()
archivo.close()
repeticiones = texto.count(palabra)

# Salida
print(palabra + ": " + str(repeticiones))
