# Env doctor

## Description
Ce programme a pour but de faire un diagnostique complet de l'environnement de travail pour un data scientist, la présence et la version de Python, venv activé ou pas, Git installé ou pas, les bibliothèques présentes sont elles dans la bonne version ?

## Prérequis
Vous aurez besoins des outils suivants avant de lancer le programme
* Python 3.10 ou plus
* Git

## Installation
L'installation du programme dans votre ordinateur (clone, venv, activation sous Windows et sous macOS/Linux).
Ouvrez le terminal et tapez les commandes suivantes dans l'ordre:

git clone https://github.com/glody-kalombo/env-doctor.git
cd env-doctor
python -m venv .venv
source .venv/Scripts/activate
Windows (Git Bash) source : .venv/bin/activate
MacOS / Linux pip install : -r requirements.txt

## Utilisation
L'utilisation, avec un exemple de sortie réel dans le terminal

python src/env_doctor.py requirements.txt

```
$ python src/env_doctor.py requirements.txt
La version de Python est : 3.13.7
Le chemin de l'interpreteur est : C:\Users\Glody\projects\projects-by-step\env-doctor\.venv\Scripts\python.exe
Venv est il actif : True
Git est il installé : True
Vérification des dépendances (requirements.txt) :
    - certifi==2026.10.19 : MANQUANT
    - charset-normalizer==3.5.2 : MANQUANT
    - idna==3.20 : MANQUANT
    - requests==2.34.2 : MANQUANT
    - urllib3==2.8.0 : MANQUANT

Diagnostic complet : ECHEC (Dépendances manquantes ou incorrectes)
(.venv)
```

## Licence.

Ce projet est sous licence MIT, voir [LICENSE](LICENSE).
