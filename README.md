# Practica-1-automatas

# Analizador Léxico en Python

## 1. Objetivo del Proyecto

El objetivo de este proyecto es desarrollar un programa que funcione como la **primera fase de un compilador**, conocida como **Analizador Léxico o Scanner**. El programa implementa un analizador capaz de:

- Separar un texto en unidades léxicas (tokens)
- Validar palabras contra un diccionario de palabras reservadas
- Clasificar palabras válidas e identificadores
- Detectar errores léxicos (palabras no reconocidas)
- Generar un archivo de salida con los tokens clasificados

## 2. ¿Cómo Funciona?

### 2.1 Flujo General del Programa

El programa ejecuta estos pasos en orden:

1. **Carga del diccionario** → Lee el archivo `diccionario.txt` con palabras reservadas
2. **Lectura del texto** → Abre el archivo de entrada `texto_entrada.txt`
3. **Tokenización** → Separa el texto en palabras individuales usando `split()`
4. **Clasificación** → Asigna un tipo a cada palabra según reglas específicas
5. **Generación de salida** → Guarda los resultados en `tokens_salida.txt`

### 2.2 Componentes Principales

#### A. Expresiones Regulares
```python
regex_identificador = r'^[a-z_][a-z0-9_]*$'  # Identificadores válidos
```
Define un patrón que acepta:
- Letras minúsculas (a-z)
- Guiones bajos (_) al inicio
- Números (0-9) después del primer carácter

#### B. Función `cargar_diccionario()`
- Lee el archivo `diccionario.txt`
- Extrae pares `TOKEN LEXEMA` (ej: `KW_LUZ luz`)
- Construye un diccionario: `{lexema: token}`
- Permite búsquedas rápidas O(1) de palabras reservadas

#### C. Función `analizar_texto()`
Para cada palabra del texto, aplica esta lógica de clasificación:

```
¿Está en el diccionario?
  ✓ Sí → Escribir su TOKEN correspondiente
  
¿Coincide con regex_identificador?
  ✓ Sí → Clasificar como "IDENTIFICADOR"
  
Si no cumple ninguno:
  → Clasificar como "ERROR_LEXICO"
```

#### D. Función `guardar_salida()`
- Escribe en `tokens_salida.txt`
- Formato: `TOKEN    lexema` (separados por tabulación)
- Preserva el orden de análisis

## 3. Ejemplo de Ejecución

### Entrada ([texto_entrada.txt](texto_entrada.txt)):
```
luz tierra agua fuego variable123 xyz
```

### Proceso de Clasificación:

| Palabra | ¿En diccionario? | ¿Es identificador válido? | Clasificación | Razón |
|---------|------------------|--------------------------|----------------|-------|
| luz | ✓ Sí | - | KW_LUZ | Está en el diccionario |
| tierra | ✓ Sí | - | KW_TIERRA | Está en el diccionario |
| agua | ✓ Sí | - | KW_AGUA | Está en el diccionario |
| fuego | ✗ No | ✓ Sí | IDENTIFICADOR | Coincide con la expresión regular |
| variable123 | ✗ No | ✓ Sí | IDENTIFICADOR | Coincide con la expresión regular |
| xyz | ✗ No | ✓ Sí | IDENTIFICADOR | Coincide con la expresión regular |

### Salida ([tokens_salida.txt](tokens_salida.txt)):
```
KW_LUZ	luz
KW_TIERRA	tierra
KW_AGUA	agua
IDENTIFICADOR	fuego
IDENTIFICADOR	variable123
IDENTIFICADOR	xyz
```

## 4. Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| [analizador_lexico.py](analizador_lexico.py) | Script principal con toda la lógica del analizador |
| [diccionario.txt](diccionario.txt) | Base de datos de palabras reservadas (formato: `TOKEN LEXEMA`) |
| [texto_entrada.txt](texto_entrada.txt) | Archivo de entrada con el texto a analizar |
| [tokens_salida.txt](tokens_salida.txt) | Archivo de salida con los tokens clasificados |
| [README.md](README.md) | Este archivo con la documentación |

### Formato del Diccionario
```
KW_LUZ luz
KW_TIERRA tierra
KW_AGUA agua
KW_FUEGO fuego
```

## 5. Funcionalidades

✅ **Analizador Léxico**: Separa texto en tokens individuales  
✅ **Validación de Palabras Reservadas**: Verifica contra diccionario  
✅ **Reconocedor de Identificadores**: Detecta variables y nombres válidos  
✅ **Detección de Errores Léxicos**: Marca palabras no reconocidas  
✅ **Generación de Salida**: Almacena resultados en archivo con formato estructurado  

## 6. Tecnologías Utilizadas

- **Lenguaje**: Python 3.6+
- **Librerías**: `re` (expresiones regulares)
- **Archivos**: Texto plano (.txt)

## 7. Cómo Usar

1. **Preparar entrada**: Coloca tu texto en `texto_entrada.txt`
2. **Configurar diccionario**: Asegúrate que `diccionario.txt` contiene tus palabras reservadas
3. **Ejecutar el programa**:
   ```bash
   python analizador_lexico.py
   ```
4. **Ver resultados**: Consulta `tokens_salida.txt`

## 8. Tipos de Tokens Posibles

El programa genera líneas con formato `TOKEN    lexema`:

| Token | Significado | Ejemplo |
|-------|-------------|---------|
| `KW_*` | Palabra reservada del diccionario | `KW_LUZ`, `KW_TIERRA` |
| `IDENTIFICADOR` | Variable o nombre válido | `variable`, `xyz`, `temp_1` |
| `ERROR_LEXICO` | Palabra no reconocida | `@palabra`, `12abc` |

## 9. Limitaciones y Mejoras Sugeridas

### Limitaciones Actuales:
- ❌ La separación usa `split()`, por lo que signos pegados generan error (ej: `luz,` → `ERROR_LEXICO`)
- ❌ Solo acepta letras minúsculas en identificadores
- ❌ No reconoce números como tokens válidos
- ❌ No maneja caracteres especiales (puntuación, símbolos)

### Mejoras Propuestas:
1. Usar expresiones regulares avanzadas para tokenizar signos de puntuación
2. Expandir `regex_identificador` para aceptar mayúsculas: `r'^[a-zA-Z_][a-zA-Z0-9_]*$'`
3. Agregar reconocimiento de números como tipo de token
4. Implementar manejo de operadores (+, -, *, /, etc.)
5. Soportar comentarios en el texto de entrada

## 10. Complejidad y Características

| Aspecto | Valor |
|--------|-------|
| **Complejidad Temporal** | O(n) donde n = número de palabras |
| **Complejidad Espacial** | O(m) donde m = palabras en diccionario |
| **Búsqueda en Diccionario** | O(1) mediante hash (diccionario Python) |
| **Validación Regex** | O(k) donde k = longitud de la palabra |

## 11. Diagrama de Flujo

```
INICIO
  │
  ├─→ Cargar diccionario (diccionario.txt)
  │
  ├─→ Leer texto (texto_entrada.txt)
  │
  ├─→ Para cada palabra:
  │    ├─→ ¿Está en diccionario?
  │    │    └─→ SÍ: Escribir TOKEN
  │    │
  │    ├─→ ¿Coincide regex_identificador?
  │    │    └─→ SÍ: Escribir IDENTIFICADOR
  │    │
  │    └─→ NO: Escribir ERROR_LEXICO
  │
  ├─→ Guardar salida (tokens_salida.txt)
  │
  └─→ FIN
```