# practica-1

Objetivo General Desarrollar un programa que funcione como la primera fase de un compilador (Analizador Léxico o Scanner), utilizando un conjunto predefinido de palabras válidas (una base de datos)

# Descripción
Pequeño analizador léxico (scanner) que clasifica palabras de entrada en tokens usando:
- Un diccionario de palabras reservadas en [diccionario.txt](diccionario.txt).
- Una expresión regular para identificar identificadores en el código: [`analizador_lexico.regex_identificador`](analizador_lexico.py).
- Funciones principales en [`analizador_lexico.py`](analizador_lexico.py): [`analizador_lexico.cargar_diccionario`](analizador_lexico.py) y [`analizador_lexico.analizar_texto`](analizador_lexico.py).

# Archivos
- [analizador_lexico.py](analizador_lexico.py): implementación del lector de diccionario y del análisis léxico.
- [diccionario.txt](diccionario.txt): lista token lexema (ej: `KW_LUZ luz`). La línea `IDENTIFICADOR` aparece sola en este archivo y se maneja de forma especial en el cargador.
- [texto_entrada.txt](texto_entrada.txt): texto de ejemplo de entrada.
- [tokens_salida.txt](tokens_salida.txt): archivo de salida con token y lexema producidos por el analizador.

# Cómo funciona (resumen)
1. [`analizador_lexico.cargar_diccionario`](analizador_lexico.py) lee [diccionario.txt](diccionario.txt) y construye un mapa lexema -> token.
2. [`analizador_lexico.analizar_texto`](analizador_lexico.py) lee [texto_entrada.txt](texto_entrada.txt), separa por espacios y para cada palabra:
   - Si la palabra está en el diccionario, escribe su token.
   - Si coincide con [`analizador_lexico.regex_identificador`](analizador_lexico.py) escribe `IDENTIFICADOR`.
   - En otro caso escribe `ERROR_LEXICO`.
3. El resultado se escribe en [tokens_salida.txt](tokens_salida.txt).

# Ejecución
Ejecutar desde la raíz del proyecto:
```sh
python analizador_lexico.py
```
Al terminar se crea/actualiza [tokens_salida.txt](tokens_salida.txt).

# Notas y mejoras sugeridas
- La separación actual usa `str.split()`, por lo que signos de puntuación pegados a palabras (por ejemplo `lu,z` o `tierra..`) generan `ERROR_LEXICO`. Se puede mejorar usando tokenización con expresiones regulares para separar identificadores y símbolos.
- La expresión regular actual (`[`analizador_lexico.regex_identificador`](analizador_lexico.py)`) acepta solo letras minúsculas y `_` al inicio. Si se desea admitir mayúsculas, actualizar el patrón.
- El lector de diccionario trata líneas con una sola palabra de forma especial (la línea `IDENTIFICADOR` en [diccionario.txt](diccionario.txt)). Revisar `cargar_diccionario` si se requiere otro formato.

# Ejemplo
Entrada: [texto_entrada.txt](texto_entrada.txt)  
Salida generada: [tokens_salida.txt](tokens_salida.txt)
