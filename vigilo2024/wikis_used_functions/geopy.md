# Fonctions Utilisées de la Librairie Geopy

La librairie Geopy est une bibliothèque Python qui fournit des fonctionnalités de géocodage, de géolocalisation et de calcul de distance entre des points géographiques.

## `geopy.distance.distance(coord1, coord2)`

Cette fonction calcule la distance entre deux coordonnées géographiques.

- `coord1`: Un tuple contenant les coordonnées géographiques (latitude, longitude) du premier point.
- `coord2`: Un tuple contenant les coordonnées géographiques (latitude, longitude) du deuxième point.

Elle retourne la distance entre les deux points sous une forme spécifique définie par l'utilisateur.

## `geopy.geocoders.Nominatim(user_agent=None, timeout=1, proxies=None, domain_name='nominatim.openstreetmap.org', scheme='https', user_agent_headers=None, ssl_context=None, adapter_factory=None)`

Cette classe permet de géocoder des adresses en utilisant le service Nominatim d'OpenStreetMap.

- `user_agent`: Une chaîne de caractères identifiant l'application utilisant le service (par défaut, 'geopy/2.x.x'). Il est recommandé de fournir une valeur personnalisée.
- `timeout`: Le délai d'attente pour les requêtes HTTP (en secondes).
- `proxies`: Un dictionnaire contenant des proxies à utiliser pour les requêtes HTTP.
- `domain_name`: Le nom de domaine du service Nominatim.
- `scheme`: Le schéma de l'URL pour les requêtes (HTTP ou HTTPS).
- `user_agent_headers`: Un dictionnaire de headers HTTP supplémentaires à inclure dans les requêtes.
- `ssl_context`: Le contexte SSL à utiliser pour les requêtes HTTPS.
- `adapter_factory`: Une fonction ou une classe utilisée pour créer un adaptateur personnalisé pour les requêtes HTTP.

Cette classe est utilisée pour obtenir des informations géographiques (comme les coordonnées géographiques) à partir d'une adresse donnée.

Les fonctions de géocodage et de calcul de distance fournies par Geopy sont essentielles pour les applications impliquant des données géographiques.