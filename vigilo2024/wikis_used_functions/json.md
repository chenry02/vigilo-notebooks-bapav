# Fonctions Utilisées de la Librairie JSON

Le code utilise la librairie `json` de Python pour manipuler des données au format JSON (JavaScript Object Notation). Le JSON est un format de données léger, facile à lire et à écrire pour les humains, et facile à analyser et à générer pour les machines. Il est largement utilisé pour échanger des données structurées sur le web.

## 1. `json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`

Cette fonction prend une chaîne JSON `s` et la convertit en objet Python.

- `s`: La chaîne JSON à décoder.
- `encoding`: L'encodage à utiliser pour décoder la chaîne JSON.
- `cls`: Une classe de décodeur personnalisée utilisée pour décoder la chaîne JSON.
- `object_hook`: Un dictionnaire ou une fonction appelée lors de la conversion d'un objet JSON en un objet Python.
- `parse_float`: Une fonction qui sera appelée avec la chaîne représentant chaque nombre à virgule flottante.
- `parse_int`: Une fonction qui sera appelée avec la chaîne représentant chaque nombre entier.
- `parse_constant`: Une fonction qui sera appelée avec l'une des chaînes "null", "true" ou "false".
- `object_pairs_hook`: Une fonction qui sera appelée avec la liste des paires d'objets JSON.
- `**kw`: Des arguments supplémentaires pouvant être fournis pour personnaliser le processus de décodage.

## 2. `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`

Cette fonction prend un objet Python `obj` et le convertit en une chaîne JSON.

- `obj`: L'objet Python à encoder.
- `skipkeys`: Booléen indiquant s'il faut ignorer les clés non définies lors de l'encodage.
- `ensure_ascii`: Booléen indiquant s'il faut échapper à tous les caractères non-ASCII lors de l'encodage.
- `check_circular`: Booléen indiquant s'il faut vérifier les références circulaires lors de l'encodage.
- `allow_nan`: Booléen indiquant s'il faut autoriser la sérialisation de valeurs NaN, infinies et -infinies.
- `cls`: Une classe d'encodeur personnalisée utilisée pour encoder l'objet Python.
- `indent`: La chaîne utilisée pour l'indentation dans la sortie JSON.
- `separators`: Un tuple contenant les séparateurs à utiliser pour les différentes parties de la sortie JSON.
- `default`: Une fonction appelée pour les objets qui ne sont pas sérialisables.
- `sort_keys`: Booléen indiquant s'il faut trier les clés de l'objet JSON.
- `**kw`: Des arguments supplémentaires pouvant être fournis pour personnaliser le processus d'encodage.

Ces deux fonctions sont essentielles pour lire et écrire des données au format JSON dans le code Python utilisé.