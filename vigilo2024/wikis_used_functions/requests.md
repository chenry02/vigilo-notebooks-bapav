# Fonction utilisée de la librairie Requests

La bibliothèque Requests est une librairie Python populaire qui facilite l'envoi de requêtes HTTP et la gestion des réponses. Elle offre une interface simple et conviviale pour interagir avec des API Web, récupérer des données à partir d'URL et effectuer d'autres opérations liées aux requêtes HTTP.

## get
Cette fonction envoie une requête HTTP GET à l'URL spécifiée. Il est possible de spécifier des paramètres de requête. Cette fonction permet de récupérer des données à partir d'une ressource en ligne identifiée par l'URL.

### Arguments utilisés :
- `url` (str): L'URL à laquelle la requête est envoyée.
- `params` (dict): Les paramètres de requête à ajouter à l'URL.

**Exemple :**
```python
# Exemple d'utilisation avec des paramètres de requête pour récupérer des données
full_query = "valeur_de_la_requete"  # Exemple de valeur de la requête
response = requests.get(url, params={'data': full_query})
resp.raise_for_status()  # Vérifie si la requête a réussi ou lève une exception
```
