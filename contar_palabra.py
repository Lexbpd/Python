import sys

nombre_archivo = sys.argv[1]
palabra = sys.argv[2]

archivo = open(nombre_archivo, "r", encoding="utf-8")
texto = archivo.read()
archivo.close()

texto = texto.lower()
palabra_buscada = palabra.lower()

signos = '.,;:!?¡¿"\'«»()-—…'
for signo in signos:
    texto = texto.replace(signo, " ")

lista_palabras = texto.split()
repeticiones = lista_palabras.count(palabra_buscada)

print(palabra + ": " + str(repeticiones))