## Fonctions utilisées de la librairie Pandas

Pandas est une librairie Python essentielle pour travailler avec des données tabulaires. Elle offre une structure de données appelée DataFrame, qui est similaire à une feuille de calcul ou à une table de base de données. Avec Pandas, nous pouvons facilement charger, nettoyer, manipuler et analyser des données sous forme de tableaux, ce qui en fait un outil indispensable pour l'analyse de données.

## DataFrame

La fonction `DataFrame` crée un nouveau DataFrame à partir des données fournies.

- `data`: Les données à utiliser pour créer le DataFrame. Cela peut être un dictionnaire, une liste de listes, un tableau NumPy, etc.

```python
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
```

## set_index

La méthode `set_index` définit une ou plusieurs colonnes comme index du DataFrame.

- `keys`: Le nom ou les noms des colonnes à utiliser comme index.
- `inplace`: Un booléen indiquant si les modifications doivent être apportées directement au DataFrame d'origine ou si une nouvelle version doit être renvoyée sans modifier l'objet d'origine.

```python
df.set_index(keys='A', inplace=True)
```

## to_datetime

La fonction `to_datetime` convertit une colonne en type de données de date et heure.

- `arg`: La colonne ou le DataFrame à convertir en type de données de date et heure.
- `errors`: Contrôle la manière dont les erreurs sont gérées. Par défaut, 'raise' lève une exception en cas d'erreur.

```python
df['date'] = pd.to_datetime(arg=df['date_column'], errors='raise')
```

## astype

La méthode `astype` convertit le type de données d'une colonne en un autre type.

- `dtype`: Le type de données auquel convertir la colonne.

```python
df['B'] = df['B'].astype(dtype=float)
```

## rename

La méthode `rename` renomme les colonnes du DataFrame.

- `columns`: Un dictionnaire de correspondance entre les anciens noms de colonnes et les nouveaux noms de colonnes.
- `inplace`: Un booléen indiquant si les modifications doivent être apportées directement au DataFrame d'origine ou si une nouvelle version doit être renvoyée sans modifier l'objet d'origine.

```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)
```

## drop

La méthode `drop` supprime des lignes ou des colonnes du DataFrame.

- `labels`: Le nom ou les noms des lignes ou des colonnes à supprimer.
- `inplace`: Un booléen indiquant si les modifications doivent être apportées directement au DataFrame d'origine ou si une nouvelle version doit être renvoyée sans modifier l'objet d'origine.

```python
df.drop(labels='B', inplace=True)
```

## from_dict

La fonction `from_dict` crée un DataFrame à partir d'un dictionnaire.

- `data`: Le dictionnaire contenant les données à utiliser pour créer le DataFrame.

```python
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame.from_dict(data)
```

## to_csv

La méthode `to_csv` écrit les données d'un DataFrame dans un fichier CSV.

- `path_or_buf`: Le chemin du fichier CSV dans lequel écrire les données.
- `index`: Un booléen indiquant s'il faut inclure l'index du DataFrame dans le fichier CSV.

```python
df.to_csv(path_or_buf='data.csv', index=False)
