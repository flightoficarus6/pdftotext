# Archivo: extraer_texto_pdf.py
# Autor: Suanes Ignacio
# Descripción: Extrae texto plano de todos los archivos PDF de una carpeta y los concatena en un archivo .txt
# Esta es un test 

import os
import fitz  # PyMuPDF

def extraer_texto_de_pdfs(directorio_pdfs, archivo_salida):
    texto_total = ""
    for archivo in os.listdir(directorio_pdfs):
        if archivo.lower().endswith(".pdf"):
            ruta_pdf = os.path.join(directorio_pdfs, archivo)
            print(f"Procesando: {archivo}")
            doc = fitz.open(ruta_pdf)
            for pagina in doc:
                texto_total += pagina.get_text()
            doc.close()
            texto_total += "\n\n"  # Separador entre archivos

    with open(archivo_salida, "w", encoding="utf-8") as salida:
        salida.write(texto_total)

    print(f"\n✅ ¡Texto extraído con éxito! Guardado en: {archivo_salida}")

# CONFIGURACIÓN
directorio = "C:\\pdf"
archivo_txt = "C:\\resultado.txt"

# EJECUCIÓN
extraer_texto_de_pdfs(directorio, archivo_txt)
