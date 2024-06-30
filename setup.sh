#!/bin/bash

# Détecter l'OS
OS="`uname`"
case $OS in
  'Linux')
    OS='Linux'
    ;;
  'Darwin') 
    OS='Mac'
    ;;
  'CYGWIN'* | 'MINGW32'* | 'MSYS'* | 'MINGW'*) 
    OS='Windows'
    ;;
  *) 
    OS='unknown'
    ;;
esac

# Créer et activer l'environnement virtuel
if [ $OS == 'Windows' ]; then
  python -m venv venv
  source venv/Scripts/activate
else
  python3 -m venv venv
  source venv/bin/activate
fi

# Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

# Initialiser un dépôt Git local
git init

# Ajouter tous les fichiers et faire un premier commit
git add .
git commit -m "Initial commit"

# Demander l'URL du dépôt distant
read -p "Entrez l'URL du dépôt Git distant : " repo_url

# Ajouter le dépôt distant et pousser le commit initial
git remote add origin $repo_url
git branch -M main
git push -u origin main

echo "L'environnement virtuel est créé, les dépendances sont installées, et le dépôt Git est configuré."
echo "Pour activer l'environnement virtuel, utilisez :"
if [ $OS == 'Windows' ]; then
  echo "venv\Scripts\activate"
else
  echo "source venv/bin/activate"
fi
