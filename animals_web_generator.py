import requests

def load_data(animal_name):
    """Loads data from API for the specified animal"""
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': 'hnNcTlcp3tb9JCJ1LUds2A==dIgyWDQFfYNycVcO'}
    response = requests.get(url, headers=headers)
    return response.json()


def serialize_animal(animal_obj):
    """Serializes an animal object into HTML"""
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj["name"]}</div>'
    output += '<p class="card__text">'
    output += f'<strong>Scientific Name: </strong>{animal_obj["taxonomy"]["scientific_name"]}<br/>\n'
    output += f'<strong>Diet: </strong>{animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location: </strong>{animal_obj["locations"][0]}<br/>\n'
    if "type" in animal_obj["characteristics"]:
        output += f'<strong>Type: </strong>{animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>'
    output += '</li>'
    return output


def generate_html(animal_data, template_path, output_path, animal_name):
    """Creates HTML document with either animal data or an error message"""
    if not animal_data:
        serialized_animals = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        serialized_animals = ''.join(serialize_animal(animal) for animal in animal_data)

    with open(template_path, "r") as template:
        html_content = template.read()

    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", serialized_animals)

    with open(output_path, "w") as new_file:
        new_file.write(new_html_content)


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    if not animal_name:
        print("You must enter a name.")
        return

    animals_data = load_data(animal_name)
    generate_html(animals_data, "animals_template.html", "animals.html", animal_name)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
