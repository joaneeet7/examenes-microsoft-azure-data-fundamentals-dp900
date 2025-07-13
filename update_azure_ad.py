#!/usr/bin/env python3
import re
import os

def update_azure_ad_references():
    exam_files = [
        "Practice Exam - DP-900 - Practice-Exam-1 (Spanish).toml",
        "Practice Exam - DP-900 - Practice-Exam-2 (Spanish).toml",
        "Practice Exam - DP-900 - Practice-Exam-3 (Spanish).toml",
        "Practice Exam - DP-900 - Practice-Exam-4 (Spanish).toml"
    ]
    
    for filename in exam_files:
        if os.path.exists(filename):
            print(f"Actualizando {filename}...")
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Reemplazar "Azure AD" por "Microsoft Entra ID"
            content = content.replace("Azure AD", "Microsoft Entra ID")
            
            # Reemplazar "Azure Active Directory (Azure AD)" por "Microsoft Entra ID (anteriormente Azure Active Directory)"
            content = content.replace("Azure Active Directory (Azure AD)", "Microsoft Entra ID (anteriormente Azure Active Directory)")
            
            # Reemplazar "Azure Active Directory" por "Microsoft Entra ID"
            content = content.replace("Azure Active Directory", "Microsoft Entra ID")
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"✅ {filename} actualizado")
        else:
            print(f"❌ Archivo {filename} no encontrado")
    
    print("\n¡Todas las referencias de Azure AD han sido actualizadas a Microsoft Entra ID!")

if __name__ == "__main__":
    update_azure_ad_references() 