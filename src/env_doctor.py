"""Vérifie les versions des dépendances du package et fais une comparaison entre les versions installées et les versions attendues."""

import sys
import platform
import shutil

def get_python_version():
    """Retourne la version de Python"""
    return platform.python_version()

def get_interpreter_path():
    """Retourne la chemin vers l'interpreteur"""
    return sys.executable

def is_venv_active():
    """Retourne True si l'environnement virtuel venv est actif"""
    return sys.prefix != sys.base_prefix

def is_git_installed(get_version: bool = False) -> bool:
    """Retourne True si Git est installé"""
    if not get_version:
        return shutil.which("git") is not None

def print_report():
    """Imprime les resultats des foctions du programme"""
    python_version = get_python_version()
    interpreter_path = get_interpreter_path()
    is_venv_active_state = is_venv_active()
    is_git_installed_state = is_git_installed()

    print(f"La version de Python est : {python_version}")
    print(f"Le chemin de l'interpreteur est : {interpreter_path}")
    print(f"Venv est il actif : {is_venv_active_state}")
    print(f"Git est il installé : {is_git_installed_state}")

def main():
    """Gère le flux d'exécution principal du programme"""
    print_report()

if __name__ == "__main__":
    main()


