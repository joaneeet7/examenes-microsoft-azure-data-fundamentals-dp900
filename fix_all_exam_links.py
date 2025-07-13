#!/usr/bin/env python3
import re
import os

def fix_links_in_file(filename):
    print(f"Corrigiendo enlaces en {filename}...")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Contador de cambios
    changes_made = 0
    
    # Cambiar todos los enlaces de /en-us/ a /es-es/
    pattern = r'https://learn\.microsoft\.com/en-us/([^"\s]+)'
    def replace_en_us(match):
        nonlocal changes_made
        changes_made += 1
        url = match.group(0)
        new_url = url.replace('/en-us/', '/es-es/')
        print(f"  - Cambiado a español: {url[:60]}... -> {new_url[:60]}...")
        return new_url
    
    content = re.sub(pattern, replace_en_us, content)
    
    # Cambiar también enlaces de docs.microsoft.com a learn.microsoft.com en español
    pattern2 = r'https://docs\.microsoft\.com/en-us/([^"\s]+)'
    def replace_docs(match):
        nonlocal changes_made
        changes_made += 1
        url = match.group(0)
        new_url = url.replace('docs.microsoft.com/en-us/', 'learn.microsoft.com/es-es/')
        print(f"  - Corregido docs->learn: {url[:60]}... -> {new_url[:60]}...")
        return new_url
    
    content = re.sub(pattern2, replace_docs, content)
    
    # Cambiar enlaces de azure.microsoft.com a learn.microsoft.com en español
    pattern3 = r'https://azure\.microsoft\.com/en-us/([^"\s]+)'
    def replace_azure(match):
        nonlocal changes_made
        changes_made += 1
        url = match.group(0)
        new_url = url.replace('azure.microsoft.com/en-us/', 'learn.microsoft.com/es-es/azure/')
        print(f"  - Corregido azure->learn: {url[:60]}... -> {new_url[:60]}...")
        return new_url
    
    content = re.sub(pattern3, replace_azure, content)
    
    # Escribir el archivo actualizado
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"  - {changes_made} enlaces corregidos en {filename}")

def fix_all_exam_links():
    exam_files = [
        "Practice Exam - DP-900 - Practice-Exam-2 (Spanish).toml",
        "Practice Exam - DP-900 - Practice-Exam-3 (Spanish).toml",
        "Practice Exam - DP-900 - Practice-Exam-4 (Spanish).toml"
    ]
    
    total_changes = 0
    
    for filename in exam_files:
        if os.path.exists(filename):
            fix_links_in_file(filename)
            # Contar cambios en este archivo
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
                en_us_count = len(re.findall(r'/en-us/', content))
                docs_count = len(re.findall(r'docs\.microsoft\.com', content))
                azure_count = len(re.findall(r'azure\.microsoft\.com', content))
                if en_us_count == 0 and docs_count == 0 and azure_count == 0:
                    print(f"  ✅ {filename} - Todos los enlaces corregidos")
                else:
                    print(f"  ⚠️  {filename} - Algunos enlaces pueden necesitar corrección manual")
        else:
            print(f"❌ Archivo {filename} no encontrado")
    
    print("\n¡Enlaces de todos los exámenes corregidos exitosamente!")

if __name__ == "__main__":
    fix_all_exam_links() 