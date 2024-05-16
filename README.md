# INFO-F310

## Membres du groupe

Romain Markowitch - 000540172

Noé Vekemans - 000475625

## Structure du projet

- `generate_model.py` : Script de génération des fichiers.lp
- `rapport.pdf` : Le rapport scientifique du projet.
  
## Utilisation

En supposant que le dossier instances soit au même niveau que le fichier generate_model.py

### 1. Lancer la génération des modèles

- instance_name : représente le problème à modéliser (doit se trouver dans le dossier instances).
- p : 0 pour un modèle agrégé et 1 pour un modèle désagrégé

```bash
python3 genrate_model.py instance_name.txt p
```

### 2. Lancer la résolution des problèmes

Une fois le fichier.lp (au format CPLEX LP) généré, il ne reste plus qu'a le résoudre.

```bash
glpsol --lp instance_name.lp -o instance_name_p.sol
```

ATTENTION : 
- instance_name doit être le nom d'un fichier.lp existant
- p doit être la valeur du modèle existant.
