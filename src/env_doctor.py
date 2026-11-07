"""Vérifie les versions des dépendances du package et fait une comparaison entre les versions installées et les versions attendues."""

import sys
import platform
import shutil
from pathlib import Path
import importlib.metadata


def get_python_version():
    """Retourne la version de Python"""
    return platform.python_version()


def get_interpreter_path():
    """Retourne le chemin vers l'interpréteur"""
    return sys.executable


def is_venv_active():
    """Retourne True si l'environnement virtuel venv est actif"""
    return sys.prefix != sys.base_prefix


def is_git_installed() -> bool:
    """Retourne True si Git est installé"""
    return shutil.which("git") is not None


def parse_requirements(requirements_path):
    """Lit le fichier et retourne une liste de paires (nom, version_attendue) """
    req_file = Path(requirements_path)
    if not req_file.exists():
        raise FileNotFoundError(f"Le fichier '{requirements_path}' est introuvable. ")

    dependencies = []
    with open(req_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if "==" in line:
                pkg_name, expected_version = line.split("==", 1)
                dependencies.append((pkg_name.strip(), expected_version.strip()))
            else:
                dependencies.append((line.strip(), None))

    return dependencies


def check_package(name, expected_version):
    """Vérifie un seul paquet et retourne un statut et la version installée"""
    try:
        installed_version = importlib.metadata.version(name)
        if expected_version is None or installed_version == expected_version:
            return "OK", installed_version
        else:
            return "VERSION_DIFFERENTE", installed_version
    except importlib.metadata.PackageNotFoundError:
        return "MANQUANT", None


def print_report():
    """Imprime les résultats des fonctions du programme"""

    if len(sys.argv) < 2:
        print("Erreur : Veuillez spécifier le chemin du fichier de requirements en argument.")
        print("Usage: python src/env_doctor.py <chemin_vers_requirements.txt>")
        sys.exit(1)

    requirements_argument = sys.argv[1]

    # 1. Infos Système
    python_version = get_python_version()
    interpreter_path = get_interpreter_path()
    is_venv_active_state = is_venv_active()
    is_git_installed_state = is_git_installed()
    print(f"La version de Python est : {python_version}")
    print(f"Le chemin de l'interpréteur est : {interpreter_path}")
    print(f"Venv est il actif : {'Oui' if is_venv_active_state else 'Non'}")
    print(f"Git est il installé : {'Oui' if is_git_installed_state else 'Non'}")

    # 2. Lecture et analyse du fichier passé en argument
    try:
        dependencies = parse_requirements(requirements_argument)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    print(f"Vérification des dépendances ({requirements_argument}) :")
    global_success = True

    # 3. Boucle d'affichage et de decision
    for pkg_name, expected_version in dependencies:
        status, installed_version = check_package(pkg_name, expected_version)

        if status == "OK":
            version_str = f" ({expected_version})" if expected_version else f" (v{installed_version}) "
            print(f"    - {pkg_name}{version_str} : OK")

        elif status == "VERSION_DIFFERENTE":
            print(f"    - {pkg_name} : VERSION DIFFÉRENTE (Demandée: {expected_version}, Installée: {installed_version})")
            global_success = False

        elif status == "MANQUANT":
            print(f"    - {pkg_name} : MANQUANT")
            global_success = False

    # 4. Code de sortie final
    if global_success:
        print("\nDiagnostic complet : TOUT EST OK")
        sys.exit(0)
    else:
        print("\nDiagnostic complet : ÉCHEC (Dépendances manquantes ou incorrectes)")
        sys.exit(1)


def main():
    """Gère le flux d'exécution principal du programme"""
    print_report()


if __name__ == "__main__":
    main()
