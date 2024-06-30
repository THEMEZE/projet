import os
import fitz  # PyMuPDF
import pandas as pd

# Chemin vers le répertoire contenant les livres PDF
dossier_livres = '/Users/themezeguillaume/Desktop/Documents_Clef/Livres_vacances'

# Dictionnaire pour stocker les thèmes et les livres correspondants
livres_par_theme = {}

# Parcourir tous les fichiers PDF dans le répertoire
for fichier in os.listdir(dossier_livres):
    if fichier.endswith('.pdf'):
        chemin_pdf = os.path.join(dossier_livres, fichier)
        try:
            # Ouvrir le fichier PDF
            document = fitz.open(chemin_pdf)
            
            # Lire le titre (première page)
            titre = document.metadata.get('title', 'Titre inconnu')
            
            # Lire d'autres métadonnées ou contenu pour identifier le thème
            # Par exemple, rechercher des mots clés dans le texte ou les métadonnées

            # Stocker le livre sous le thème correspondant
            # Par exemple, supposons que le thème soit basé sur le titre ou les métadonnées
            theme = 'Physique classique'  # À remplacer par votre logique de catégorisation
            
            if theme not in livres_par_theme:
                livres_par_theme[theme] = []
            livres_par_theme[theme].append(titre)
            
            # Afficher le thème et le titre du livre
            print(f"Thème: {theme}, Livre: {titre}")
            
            # Fermer le document PDF
            document.close()
            
        except Exception as e:
            print(f"Erreur lors du traitement du fichier {fichier}: {str(e)}")

# Enregistrer les résultats dans un fichier texte
with open('livres_par_theme.txt', 'w', encoding='utf-8') as f:
    for theme, livres in livres_par_theme.items():
        f.write(f"{theme}:
")
        for livre in livres:
            f.write(f"  - {livre}
")
        f.write("\n")

# Enregistrer les résultats dans un fichier CSV (optionnel)
df = pd.DataFrame([(theme, livre) for theme, livres in livres_par_theme.items() for livre in livres], columns=['Thème', 'Livre'])
df.to_csv('livres_par_theme.csv', index=False, encoding='utf-8')

print("Classification des livres terminée. Fichiers créés : livres_par_theme.txt, livres_par_theme.csv")
