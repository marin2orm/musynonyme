import requests
from bs4 import BeautifulSoup

def synonyme(mot):
    url = "http://www.synonymo.fr/synonyme/"
    urlComp = url + mot

    response = requests.get(urlComp)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        ul_synos = soup.find('ul', {'class': 'synos'})
        if ul_synos:
            premier_li = ul_synos.find('li')
            if premier_li:
                premier_mot = premier_li.find('a').text
                print(premier_mot)
                return premier_mot
            else:
                print("Pas de synonyme trouvé")
                return ""  # Renvoyez une chaîne vide si aucun synonyme n'est trouvé
    return ""  # Renvoyez une chaîne vide si la requête n'est pas OK
