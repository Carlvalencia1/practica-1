import re
import tkinter as tk
from tkinter import scrolledtext, messagebox

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


def mostrar_tokens_ventana(ruta_salida):
    try:
        with open(ruta_salida, "r", encoding="utf-8") as f:
            lines = [l.rstrip("\n") for l in f if l.strip()]
    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró: {ruta_salida}")
        return

    # Parsear líneas: saltar cabecera si existe
    rows = []
    for line in lines:
        if line.strip().lower().startswith("token"):
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            token, lexema = parts[0].strip(), parts[1].strip()
        else:
            parts = line.split()
            if len(parts) >= 2:
                token, lexema = parts[0].strip(), parts[1].strip()
            else:
                continue
        rows.append((token, lexema))

    root = tk.Tk()
    root.title("Tokens de salida - " + ruta_salida)
    root.geometry("520x420")

    # Contenedor con scroll
    container = tk.Frame(root)
    container.pack(fill="both", expand=True, padx=8, pady=8)

    canvas = tk.Canvas(container)
    vsb = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    hsb = tk.Scrollbar(container, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    canvas.pack(side="left", fill="both", expand=True)

    table_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=table_frame, anchor="nw")

    header_font = ("Consolas", 11, "bold")
    cell_font = ("Consolas", 11)

    # Cabeceras
    lbl_h1 = tk.Label(table_frame, text="Token", relief="solid", borderwidth=1,
                      width=20, anchor="center", font=header_font, bg="#e8e8e8")
    lbl_h1.grid(row=0, column=0, sticky="nsew")
    lbl_h2 = tk.Label(table_frame, text="Lexema", relief="solid", borderwidth=1,
                      width=30, anchor="center", font=header_font, bg="#e8e8e8")
    lbl_h2.grid(row=0, column=1, sticky="nsew")

    # Filas
    for i, (token, lexema) in enumerate(rows, start=1):
        l_token = tk.Label(table_frame, text=token, relief="solid", borderwidth=1,
                           width=20, anchor="w", font=cell_font, padx=4, pady=2)
        l_token.grid(row=i, column=0, sticky="nsew")
        l_lex = tk.Label(table_frame, text=lexema, relief="solid", borderwidth=1,
                         width=30, anchor="w", font=cell_font, padx=4, pady=2)
        l_lex.grid(row=i, column=1, sticky="nsew")

    # Ajustes de comportamiento de columnas y scrollregion
    table_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    table_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(1, weight=1)

    # Botón cerrar
    btn_frame = tk.Frame(root)
    btn_frame.pack(fill="x", padx=8, pady=(0,8))
    tk.Button(btn_frame, text="Cerrar", command=root.destroy).pack(side="right")

    # Permitir scroll con la rueda del ratón
    def _on_mousewheel(event):
        canvas.yview_scroll(-int(event.delta / 120), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    root.mainloop()

if __name__ == "__main__":
    dic = cargar_diccionario("diccionario.txt")
    analizar_texto(dic, "texto_entrada.txt", "tokens_salida.txt")
    print("✔ Análisis léxico completado. Revisa tokens_salida.txt")

    # Mostrar ventana con los tokens generados
    mostrar_tokens_ventana("tokens_salida.txt")
