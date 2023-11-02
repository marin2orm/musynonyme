# Programme de substitution de synonymes

Ce programme est conçu pour prendre en entrée des paroles de chanson et les transformer en utilisant des synonymes pour chaque mot. Il utilise la bibliothèque Python `requests` pour effectuer des requêtes HTTP et `BeautifulSoup` pour extraire les données HTML des pages web.

## Instructions

1. Assurez-vous d'avoir Python installé. Si ce n'est pas le cas, vous pouvez le télécharger sur [le site officiel de Python](https://www.python.org/downloads/).
2. Installez les bibliothèques nécessaires en exécutant la commande suivante :
  - pip install requests
  - pip install beautifulsoup4

3. Exécutez le programme `main.py`.

## Utilisation

Le programme fonctionne comme suit :

- Il vous demande d'entrer les paroles de la chanson.
- Il sépare les mots de la chanson en utilisant des espaces comme délimiteurs.
- Pour chaque mot de plus de trois caractères, le programme recherche un synonyme en utilisant le site [synonymo.fr](https://www.synonymo.fr/).
- Les synonymes sont ensuite intégrés dans le texte des paroles.
- Le texte modifié avec les synonymes est imprimé.

## Avertissement

Veuillez noter que ce programme dépend de la disponibilité du site [synonymo.fr](https://www.synonymo.fr/). Si le site n'est pas accessible ou s'il subit des modifications, le programme pourrait ne pas fonctionner correctement.
