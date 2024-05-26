# Fonctions Utilisées de la Librairie Overpy

La librairie Overpy est une interface Python pour l'API Overpass d'OpenStreetMap, permettant d'interroger et de récupérer des données géographiques à partir de la base de données OpenStreetMap.

## `overpy.Overpass()`

Cette classe est utilisée pour effectuer des requêtes à l'API Overpass d'OpenStreetMap.

- Aucun argument spécifique n'est requis pour initialiser cette classe.

## `overpy.Overpass.parse_xml(data)`

Cette méthode est utilisée pour analyser les données XML renvoyées par l'API Overpass et les convertir en un objet Python.

- `data`: Les données XML renvoyées par l'API Overpass.

Elle retourne un objet Python représentant les données analysées.

## `overpy.OverpassQueryBuilder(area, query, responseformat=None)`

Cette classe est utilisée pour construire des requêtes à l'API Overpass.

- `area`: L'aire géographique sur laquelle la requête sera appliquée.
- `query`: La requête Overpass à exécuter.
- `responseformat`: Le format de la réponse de la requête (par exemple, 'json' ou 'xml').

## `overpy.ResultWays`

Cette classe représente un ensemble de chemins (ways) renvoyés par une requête Overpass.

## `overpy.ResultNodes`

Cette classe représente un ensemble de nœuds (nodes) renvoyés par une requête Overpass.

## `overpy.ResultRelations`

Cette classe représente un ensemble de relations renvoyées par une requête Overpass.

La librairie Overpy offre une interface Python puissante pour interagir avec l'API Overpass d'OpenStreetMap, permettant aux développeurs d'accéder facilement aux données géographiques de la base de données OpenStreetMap.