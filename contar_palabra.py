
# Uso: python contar_palabra.py archivo.txt palabra

import sys

# Entrada 
nombre_archivo = sys.argv[1]
palabra = sys.argv[2]

# Proceso
archivo = open(nombre_archivo, "r", encoding="utf-8")
texto = archivo.read()
archivo.close()
repeticiones = texto.count(palabra)

# Salida
print(palabra + ": " + str(repeticiones))
