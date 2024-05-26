# Fonctions et Méthodes de la Librairie Requests utilisées

La librairie Requests est un outil Python puissant qui simplifie les requêtes HTTP. Elle offre une interface conviviale pour envoyer des requêtes telles que GET, POST, PUT, DELETE, etc., et récupérer les réponses correspondantes.

## 1. `requests.get(url, params=None, **kwargs)`

Cette fonction envoie une requête GET à l'URL spécifiée et retourne un objet `Response`. Voici une explication détaillée de ses arguments :

- **url** : L'URL à laquelle vous souhaitez envoyer la requête GET. C'est une chaîne de caractères représentant l'adresse de la ressource à récupérer.
  
- **params (facultatif)** : Les paramètres de requête à inclure dans l'URL. Ces paramètres sont généralement des données envoyées avec la requête GET, souvent utilisées pour filtrer ou paginer les résultats. Les paramètres peuvent être spécifiés sous forme d'un dictionnaire ou d'une liste de tuples `(clé, valeur)`.

- **kwargs (facultatif)** : Des paramètres supplémentaires transmis à la méthode `requests.Request()`. Cela peut inclure des en-têtes HTTP personnalisés, des cookies, des certificats SSL, des délais d'attente, etc. Les valeurs de ces paramètres sont spécifiées sous forme de clés et de valeurs dans un dictionnaire.

## 2. `requests.exceptions.RequestException`

Classe d'exception de base pour les erreurs de requête. Toutes les exceptions générées par des erreurs de requête sont des sous-classes de cette classe.

## 3. `Response.raise_for_status()`

Méthode de la classe `Response` utilisée pour vérifier si la requête a réussi ou non et lever une exception en cas d'échec.
