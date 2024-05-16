# INFO-F310

## Membres du groupe

Romain Markowitch - 000540172

Noé Vekemans - 000475625

## Structure du projet

- `generate_model.py` : Script de génération des fichiers.lp
- `/rapport.pdf` : Le rapport du projet
- 
## Utilisation

En supposant qu'une base de données postgresql soit déjà installée et que le service soit lancé.

### 1. Lancer la création des tables

```bash
psql -h <host> -U <username> -d <database_name> -f ddl.sql
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

### 3. Lancer l'interface graphique

Cette partie requiert l'installation de Node.js et de Yarn.

```bash
cd web
yarn install
yarn dev
```
