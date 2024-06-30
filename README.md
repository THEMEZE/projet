# Classification de Livres PDF par Thème

## Installation

1. Exécutez le script de configuration :

    ```sh
    ./setup.sh
    ```

2. Pour activer l'environnement virtuel après l'installation :

    - Sur macOS/Linux :

      ```sh
      source venv/bin/activate
      ```

    - Sur Windows :

      ```sh
      venv\Scripts\activate
      ```

## Utilisation

1. Placez vos fichiers PDF dans le répertoire spécifié dans le script (`dossier_livres`).
2. Exécutez le script :

    ```sh
    python classify_books.py
    ```

3. Les résultats seront enregistrés dans `livres_par_theme.txt` et `livres_par_theme.csv`.

## Mise à jour des dépendances

Pour ajouter de nouvelles dépendances ou mettre à jour les existantes, modifiez votre environnement virtuel puis mettez à jour `requirements.txt` :

```sh
pip freeze > requirements.txt
