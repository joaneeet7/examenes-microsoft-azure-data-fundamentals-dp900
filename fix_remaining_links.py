#!/usr/bin/env python3
import re

def fix_remaining_links():
    # Corregir enlaces específicos que quedaron sin corregir
    
    # Examen 2 - enlace en-gb
    filename2 = "Practice Exam - DP-900 - Practice-Exam-2 (Spanish).toml"
    with open(filename2, "r", encoding="utf-8") as f:
        content2 = f.read()
    
    # Reemplazar enlace en-gb por es-es
    old_link2 = "https://docs.microsoft.com/en-gb/azure/architecture/data-guide/big-data/non-relational-data"
    new_link2 = "https://learn.microsoft.com/es-es/azure/architecture/data-guide/big-data/non-relational-data"
    
    if old_link2 in content2:
        content2 = content2.replace(old_link2, new_link2)
        print(f"✅ Corregido enlace en-gb en examen 2")
    
    with open(filename2, "w", encoding="utf-8") as f:
        f.write(content2)
    
    # Examen 3 - enlace con parámetros docs.microsoft.com
    filename3 = "Practice Exam - DP-900 - Practice-Exam-3 (Spanish).toml"
    with open(filename3, "r", encoding="utf-8") as f:
        content3 = f.read()
    
    # Reemplazar enlace con parámetros docs.microsoft.com
    old_link3 = "https://learn.microsoft.com/es-es/azure/cosmos-db/table-support?toc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fstorage%2Ftables%2Ftoc.json&bc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fazure%2Fbread%2Ftoc.json"
    new_link3 = "https://learn.microsoft.com/es-es/azure/cosmos-db/table-support"
    
    if old_link3 in content3:
        content3 = content3.replace(old_link3, new_link3)
        print(f"✅ Corregido enlace con parámetros docs.microsoft.com en examen 3")
    
    with open(filename3, "w", encoding="utf-8") as f:
        f.write(content3)
    
    print("¡Enlaces restantes corregidos exitosamente!")

if __name__ == "__main__":
    fix_remaining_links() 