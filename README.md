# INFO-F310

## Membres du groupe

Romain Markowitch - 000540172

Noé Vekemans - 000475625

## Structure du projet

- `generate_model.py` : Script de génération des fichiers.lp
- `rapport.pdf` : Le rapport du projet
  
## Utilisation

En supposant que le dossier instances soit au même niveau que le fichier generate_model.py

### 1. Lancer la génération des modèles

- instance_name : représente le problème à modéliser (doit se trouver dans le dossier instances).
- p : 0 pour un modèle agrégé et 1 pour un modèle désagrégé

```bash
python3 genrate_model.py instance_name.txt p
```

<!-- psql -h 127.0.0.1 -d polmarnette -f ddl.sql

psql -h 127.0.0.1 -d romain -f ddl.sql

psql -h 127.0.0.1 -U postgres -d postgres -f ddl.sql
mdp = x ou 12345 -->

### 2. Lancer les scripts d'importation des données

Cette partie requiert l'installation de Python 3 avec les modules [psycopg2](https://pypi.org/project/psycopg2/).

```bash
python3 imports/import_all.py
```
