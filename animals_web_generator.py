import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """ Serializes a list of animals """
    output = ""
    output += '<li class="cards__item">'
    output += '<div class="card__title">'f"{animal_obj['name']}</div>"
    output += '<p class="card__text">'
    output += '<strong>Scientific Name: </strong>'f"{animal_obj["taxonomy"]['scientific_name']}<br/>\n"
    output += '<strong>Diet: </strong>'f"{animal_obj["characteristics"]["diet"]}<br/>\n"
    output += '<strong>Location: </strong>'f"{animal_obj["locations"][0]}<br/>\n"
    if "type" in animal_obj["characteristics"]:
        output += '<strong>Type: </strong>'f"{animal_obj["characteristics"]["type"]}<br/>\n"
        output += '</p>'
    output += "</li>"
    return output


def generate_html(animal_data, template_path, output_path):
    """Creates html document wiith template and animal data"""
    serialized_animals = ''.join(serialize_animal(animal) for animal in animal_data)

    with open(template_path, "r") as template:
        html_content = template.read()

    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", serialized_animals)

    with open(output_path, "w") as new_file:
        new_file.write(new_html_content)


def main():
    animals_data = load_data("animals_data.json")
    generate_html(animals_data, "animals_template.html", "animals.html")


if __name__ == "__main__":
    main()
