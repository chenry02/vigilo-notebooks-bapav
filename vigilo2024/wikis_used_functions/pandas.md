# Fonctions et Méthodes utilisées de la Librairie Pandas

La librairie Pandas est une bibliothèque open-source permettant l'analyse et la manipulation de données en Python. Elle propose des structures de données performantes et flexibles, ainsi que des outils pour le traitement de données numériques et tabulaires.

## 1. `pd.DataFrame(data=None, index=None, columns=None)`

Classe permettant de créer un objet DataFrame à partir de données existantes.

- `data`: Les données à utiliser pour créer le DataFrame. Peut être spécifié sous forme de dictionnaire, de listes, de séries, ou de tableaux NumPy.
- `index`: Les étiquettes à utiliser pour l'index (étiquette de ligne) du DataFrame.
- `columns`: Les étiquettes à utiliser pour les colonnes du DataFrame.

## 2. `pd.DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)`

Méthode permettant de définir un nouvel index (étiquette de ligne) pour le DataFrame.

- `keys`: Les étiquettes à utiliser pour l'index.
- `drop`: Booléen indiquant s'il faut supprimer les colonnes utilisées comme nouvel index.
- `append`: Booléen indiquant s'il faut ajouter les colonnes utilisées comme nouvel index aux colonnes existantes.
- `inplace`: Booléen indiquant s'il faut modifier le DataFrame d'origine ou retourner une copie modifiée.
- `verify_integrity`: Booléen indiquant s'il faut vérifier si les nouvelles étiquettes d'index sont uniques.

## 3. `pd.DataFrame.rename(columns=None, inplace=False)`

Méthode permettant de renommer les colonnes d'un DataFrame.

- `columns`: Un dictionnaire ou une fonction pour renommer les colonnes.
- `inplace`: Booléen indiquant s'il faut modifier le DataFrame d'origine ou retourner une copie modifiée.

## 4. `pd.DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')`

Méthode permettant de supprimer des lignes ou des colonnes d'un DataFrame en fonction des étiquettes spécifiées.

- `labels`: Les étiquettes des lignes ou des colonnes à supprimer.
- `axis`: L'axe le long duquel supprimer (0 pour les lignes, 1 pour les colonnes).
- `index`: Synonyme de `labels`.
- `columns`: Synonyme de `labels`.
- `level`: Le niveau dans le cas d'un index hiérarchique.
- `inplace`: Booléen indiquant s'il faut modifier le DataFrame d'origine ou retourner une copie modifiée.
- `errors`: Contrôle le comportement lorsqu'une étiquette n'est pas trouvée (raise pour lever une exception, ignore pour ignorer).

## 5. `pd.DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.')`

Méthode permettant de sauvegarder le DataFrame au format CSV.

- `path_or_buf`: Le chemin du fichier ou un objet fichier pour écrire.
- `sep`: Le séparateur de champ.
- `na_rep`: La représentation à utiliser pour les valeurs NaN.
- `float_format`: La chaîne de format pour les nombres flottants.
- `columns`: Les colonnes à écrire.
- `header`: Booléen ou liste de chaînes à écrire en tant qu'en-têtes de colonne.
- `index`: Booléen indiquant s'il faut écrire l'index.
- `index_label`: Le nom de la colonne à utiliser pour l'index.
- `mode`: Le mode d'écriture.
- `encoding`: L'encodage du fichier.
- `compression`: La méthode de compression.
- `quoting`: La stratégie de citation.
- `quotechar`: Le caractère de citation.
- `line_terminator`: Le séparateur de ligne.
- `chunksize`: La taille des morceaux à écrire à la fois.
- `date_format`: Le format de date.
- `doublequote`: Booléen indiquant s'il faut échapper les caractères de citation.
- `escapechar`: Le caractère d'échappement.
- `decimal`: Le séparateur décimal.

## 6. `pd.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=True)`

Fonction permettant de convertir l'argument en un objet DateTime.

- `arg`: L'argument à convertir en objet DateTime.
- `errors`: Contrôle le comportement en cas d'erreur de conversion.
- `dayfirst`: Booléen indiquant si le format de date utilise le jour en premier.
- `yearfirst`: Booléen indiquant si le format de date utilise l'année en premier.
- `utc`: Booléen ou chaîne indiquant si l'objet DateTime doit être considéré comme étant en temps universel coordonné.
- `format`: Le format de date à utiliser pour la conversion.
- `exact`: Booléen indiquant si une correspondance exacte est requise pour la conversion.
- `unit`: L'unité de temps à utiliser pour l'argument.
- `infer_datetime_format`: Booléen indiquant si le format de date doit être déduit automatiquement.
- `origin`: L'origine à utiliser pour les valeurs de temps Unix.
- `cache`: Booléen indiquant s'il faut mettre en cache les résultats de la conversion.

## 7. `pd.DataFrame.astype(dtype, copy=True, errors='raise')`

Méthode permettant de convertir le type de données d'un DataFrame en un type de données spécifié.

- `dtype`: Le type de données cible.
- `copy`: Booléen indiquant s'il faut retourner une copie du DataFrame ou modifier l'original.
- `errors`: Contrôle le comportement en cas d'erreur de conversion.

## 8. `pd.DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)`

Méthode permettant de supprimer les doublons du DataFrame.

- `subset`: Les colonnes à considérer pour identifier les doublons.
- `keep`: Contrôle quel doublon conserver.
- `inplace`: Booléen indiquant s'il faut modifier le DataFrame d'origine ou retourner une copie modifiée.
- `ignore_index`: Booléen indiquant s'il faut réinitialiser les index après suppression des doublons.

## 9. `pd.DataFrame.from_dict(data, orient='columns', dtype=None, columns=None)`

Méthode permettant de créer un DataFrame à partir d'un dictionnaire.

- `data`: Le dictionnaire contenant les données à utiliser pour créer le DataFrame.
- `orient`: La disposition des données dans le dictionnaire.
- `dtype`: Le type de données à utiliser pour le DataFrame.
- `columns`: Les étiquettes de colonne à utiliser pour le DataFrame.

## 10. `pd.DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=<object object>, observed=False, dropna=True)`

Méthode permettant de regrouper les données d'un DataFrame en fonction des valeurs d'une ou plusieurs colonnes.

- `by`: Les colonnes à utiliser pour le regroupement.
- `axis`: L'axe le long duquel regrouper.
- `level`: Le niveau dans le cas d'un index hiérarchique.
- `as_index`: Booléen indiquant si les colonnes de regroupement doivent être traitées comme un index.
- `sort`: Booléen indiquant s'il faut trier les clés de regroupement.
- `group_keys`: Booléen indiquant s'il faut ajouter les clés de regroupement à l'index.
- `squeeze`: Booléen indiquant s'il faut réduire le DataFrame de résultat en une série si possible.
- `observed`: Booléen indiquant s'il faut uniquement observer les valeurs réelles lors du regroupement.
- `dropna`: Booléen indiquant s'il faut supprimer les lignes contenant des valeurs NaN lors du regroupement.

## 11. `pd.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, ...`

Fonction permettant de lire un fichier CSV dans un DataFrame.

- `filepath_or_buffer`: Le chemin du fichier CSV ou un objet de type fichier ouvert.
- `sep`: Le séparateur de champ dans le fichier CSV.
- `delimiter`: Un alias pour `sep`.
- `header`: La ligne à utiliser comme en-tête des colonnes.
- `names`: La liste des noms de colonnes à utiliser si `header` est None.
- `index_col`: La colonne à utiliser comme index des lignes.
- `usecols`: La liste des colonnes à charger dans le DataFrame.
- (et plusieurs autres arguments pour contrôler le comportement de lecture)

## 12. `pd.DataFrame.to_json(path_or_buf=None, orient=None, date_format=None, double_precision=10, force_ascii=True, ...`

Méthode permettant de convertir le DataFrame en une chaîne JSON.

- `path_or_buf`: Le chemin du fichier JSON ou un objet de type fichier ouvert.
- `orient`: La disposition des données JSON.
- `date_format`: Le format de date à utiliser pour la sérialisation.
- `double_precision`: Le nombre de décimales à conserver pour les valeurs à virgule flottante.
- `force_ascii`: Booléen indiquant s'il faut forcer l'utilisation d'ASCII pour la sortie JSON.
- (et d'autres arguments pour contrôler le format JSON)

## 13. `pd.DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)`

Méthode permettant de définir un nouvel index pour le DataFrame.

- `keys`: Les étiquettes à utiliser comme nouvel index.
- `drop`: Booléen indiquant s'il faut supprimer les colonnes utilisées comme nouvel index.
- `append`: Booléen indiquant s'il faut ajouter les nouvelles étiquettes à l'index existant.
- `inplace`: Booléen indiquant s'il faut modifier le DataFrame d'origine ou retourner une copie modifiée.
- `verify_integrity`: Booléen indiquant s'il faut vérifier l'intégrité de l'index après la définition.

## 14. `pd.DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, ...`

Méthode permettant de sauvegarder le DataFrame au format CSV.

- `path_or_buf`: Le chemin du fichier CSV ou un objet de type fichier ouvert.
- `sep`: Le séparateur de champ dans le fichier CSV.
- `na_rep`: La représentation à utiliser pour les valeurs NaN.
- `float_format`: Le format à utiliser pour les valeurs à virgule flottante.
- `columns`: La liste des colonnes à sauvegarder dans le fichier CSV.
- `header`: Booléen indiquant s'il faut inclure une ligne d'en-tête dans le fichier CSV.
- (et d'autres arguments pour contrôler le format CSV)
