import requests

api_key = 'hnNcTlcp3tb9JCJ1LUds2A==dIgyWDQFfYNycVcO'

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    return response.json()