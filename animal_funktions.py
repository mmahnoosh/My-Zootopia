import json

from animals_web_generator import animals_data


def save_animals(animals):
    """
    Gets all your animals as an argument and saves them to the html file.
    """
    try:
        with open("animals.json", "w", encoding="utf-8") as file:
            json.dump(animals_data, file, indent=4)
        print("Animal successfully saved!")
    except IOError:
        print("Error: Unable to save the animal.")

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def create_html():
    animals_dataset = load_data('animals_data.json')
    html_template = load_data('animals_template.html')
    output = []
    animal_entries = []
    for animal in animals_dataset:
        animal_entries.append(f"""
            <li class="cards__item">
                <div class="card__title">{animal['name']}</div>
                <p class="card__text">
                    <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>
                    <strong>Location:</strong> {animal['characteristics']['location']}<br/>
                    <strong>Type:</strong> {animal['characteristics']['type']}<br/>
                </p>
            </li>
        """)
    animals_html = "\n".join(output)
    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
