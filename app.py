import requests

def get_joke():
    # URL de l'API pour tout types de blagues.
    url = "https://v2.jokeapi.dev/joke/Any"

    try:
        # Requête GET
        response = requests.get(url)

        # Réponse de la requête
        if response.status_code == 200:
            data = response.json()
            if 'joke' in data:
                print(f"Blague : {data['joke']}")
            else:
                print("Désolé, aucune blague n'a été trouvée.")
        else:
            print(f"Erreur : Impossible de récupérer une blague. Code : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

if __name__ == "__main__":
    get_joke()
