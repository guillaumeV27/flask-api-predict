import joblib
import os

# def load_model(path_to_models):
#     # 'model_selection.txt' contains the name of the joblib file we want to use
#     with open(os.path.join(path_to_models, 'model_selection.txt'), "r") as model_selection_file :
#         model_dump = model_selection_file.read()
# 
#     # Loads a model previously saved 
#     model = joblib.load(os.path.join(path_to_models, model_dump))
#     
#     return model

import os
import joblib

def load_model(path_to_models: str):
    """
    Charge un modèle depuis un répertoire donné.
    - Si un fichier 'model_selection.txt' est présent, il utilise le nom du modèle spécifié dedans.
    - Sinon, il tente automatiquement de charger le premier fichier .joblib ou .pkl trouvé.
    """
    # Essaye de lire le nom du modèle depuis model_selection.txt
    selection_path = os.path.join(path_to_models, 'model_selection.txt')
    if os.path.exists(selection_path):
        with open(selection_path, "r") as f:
            model_name = f.read().strip()
        model_path = os.path.join(path_to_models, model_name)
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Fichier spécifié dans model_selection.txt non trouvé : {model_path}")
    else:
        # Fallback automatique : cherche un fichier .joblib ou .pkl dans le dossier
        for filename in os.listdir(path_to_models):
            if filename.endswith(".joblib") or filename.endswith(".pkl"):
                model_path = os.path.join(path_to_models, filename)
                print(f"[INFO] Aucun fichier 'model_selection.txt'. Utilisation automatique de : {filename}")
                break
        else:
            raise FileNotFoundError("Aucun modèle trouvé dans le dossier. Assurez-vous qu’un fichier .joblib ou .pkl existe.")

    return joblib.load(model_path)
