import re

# =============================
# TAREA 2.1 - LECTOR DE DICCIONARIO
# =============================

def cargar_diccionario(ruta):
    dic = {}
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split()
            if len(partes) == 2:
                token, lexema = partes
                dic[lexema] = token
            else:
                dic["IDENTIFICADOR"] = "IDENTIFICADOR"
    return dic


# =============================
# TAREA 2.2 - REGEX IDENTIFICADOR
# =============================

# Patrón diferente al original:
# Comienza con letra o _, seguido de letras, números o _
regex_identificador = r"[a-z_][a-z0-9_]*"


# =============================
# TAREA 2.3 - ANALIZADOR LÉXICO
# =============================

def analizar_texto(diccionario, ruta_entrada, ruta_salida):
    with open(ruta_entrada, "r", encoding="utf-8") as f:
        palabras = f.read().split()

    with open(ruta_salida, "w", encoding="utf-8") as salida:
        salida.write("Token\tLexema\n\n")
        
        for palabra in palabras:

            if palabra in diccionario:  # Palabra clave
                salida.write(f"{diccionario[palabra]}\t{palabra}\n")
                continue

            if re.fullmatch(regex_identificador, palabra):  # Identificador
                salida.write(f"IDENTIFICADOR\t{palabra}\n")
                continue

            salida.write(f"ERROR_LEXICO\t{palabra}\n")  # Error


if __name__ == "__main__":
    dic = cargar_diccionario("diccionario.txt")
    analizar_texto(dic, "texto_entrada.txt", "tokens_salida.txt")
    print("✔ Análisis léxico completado. Revisa tokens_salida.txt")
