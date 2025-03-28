# Analizador de Textos Literarios 📚

Este proyecto es una herramienta desarrollada en Python para el análisis y corrección de estilo en textos literarios, especialmente útil para escritores que desean mejorar la fluidez y claridad de sus escritos sin alterar su voz autoral.

---

## ✨ Funcionalidades principales

- 📝 Análisis de adverbios, adjetivos y preposiciones
- 💬 División por oraciones con análisis individual
- 🔁 Detección de palabras repetidas
- 📏 Contador de caracteres y palabras
- 🔎 Detección de palabras terminadas en `-mente`
- ❗ Identificación del uso redundante de "su/sus"
- 📂 Generación de informes automáticos en `.txt`
- 📄 Carga de textos desde `.docx`, `.txt` o introducción manual

---

## 📁 Estructura esperada de archivos

La aplicación carga varios ficheros `.csv` desde la carpeta `DICCIONARIO/`, con listas de palabras clasificadas por tipo:

- `ad_fich.csv` → Adverbios  
- `adj_fich.csv` → Adjetivos  
- `art_fich.csv` → Artículos  
- `prep_fich.csv` → Preposiciones  
- `pron_fich.csv` → Pronombres  
- `sus_fich.csv` → Sustantivos  
- `AlfabetoPunto.csv` → Abreviaturas y siglas

---

## ▶️ Cómo usarlo

1. Asegúrate de tener Python 3.10+ instalado.
2. Instala la dependencia necesaria para leer archivos `.docx`:

```bash
pip install python-docx