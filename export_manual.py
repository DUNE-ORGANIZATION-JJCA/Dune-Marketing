# -*- coding: utf-8 -*-
"""
Script de exportación para el Manual del Jugador de Dune: Arrakis Dominion
Ejecutar: python export_manual.py
"""

import os
import sys

print("=" * 50)
print("EXPORTACIÓN MANUAL DUNE: ARRAKIS DOMINION")
print("=" * 50)

# Archivos a combinar
FILES = [
    "Dune_Manual_Jugador.md",
    "Dune_Manual_Appendice.md"
]

OUTPUT_FILE = "Dune_Manual_Completo.md"
PDF_OUTPUT = "Dune_Manual_Completo.pdf"

# 1. Leer y combinar archivos
print("\n[1] Leyendo archivos...")
combined_content = ""

for filename in FILES:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            combined_content += content + "\n\n---\n\n"
            print(f"   ✓ {filename}")
    else:
        print(f"   ✗ {filename} NO ENCONTRADO")

# 2. Guardar archivo combinado
print("\n[2] Guardando archivo combinado...")
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(combined_content)
print(f"   ✓ Guardado como: {OUTPUT_FILE}")

# 3. Verificar pandoc
print("\n[3] Verificando Pandoc...")
pandoc_available = os.system("pandoc --version > nul 2>&1") == 0

if pandoc_available:
    print("   ✓ Pandoc disponible")
    
    # 4. Exportar a PDF
    print("\n[4] Exportando a PDF...")
    cmd = f'pandoc "{OUTPUT_FILE}" -o "{PDF_OUTPUT}" --standalone --toc -V mainfont="Georgia" -V sansfont="Arial" -V geometry:margin=1in'
    
    result = os.system(cmd)
    
    if result == 0:
        print(f"   ✓ PDF creado: {PDF_OUTPUT}")
    else:
        print("   ✗ Error al crear PDF")
else:
    print("   ✗ Pandoc NO disponible")
    print("\n   INSTALLA PANDOC:")
    print("   - Windows: choco install pandoc")
    print("   - Mac: brew install pandoc")
    print("   - Linux: sudo apt install pandoc")
    print("\n   Luego ejecutá: pandoc Dune_Manual_Completo.md -o Dune_Manual_Completo.pdf")

print("\n" + "=" * 50)
print("EXPORTACIÓN COMPLETA")
print("=" * 50)

input("\nPresioná Enter para salir...")