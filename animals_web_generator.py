import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_dataset = load_data('animals_data.json')

animal_entries = []
for animal in animals_dataset:
    locations = ", ".join(animal['locations'])
    animal_type = animal['characteristics'].get('type', '-')
    animal_entries.append(f"""
            <li class="cards__item">
                <div class="card__title">{animal['name']}</div>
                <p class="card__text">
                    <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>
                    <strong>Location:</strong> {locations}<br/>
                    <strong>Type:</strong> {animal_type}<br/>
                </p>
            </li>
        """)
animals_html = "\n".join(animal_entries)
with open('animals_template.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)
with open('animals.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

"""
animal_funktions.create_html()

animals_data = load_data('animals_data.json')
output = ""
for animal in animals_data:
    output += '<li class="cards__item"><br/>'
    if "name" in animal:
        output += f"Name: {animal['name']}<br/>"

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}<br/>"

    if "locations" in animal and animal["locations"]:
        output += f"First Location: {animal['locations'][0]}<br/>"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}<br/>"
    else:
        output += "-<br/>"
    output += '</li>   '

with open('animals_template.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
with open('animals.html', 'w', encoding='utf-8') as f:
    f.write(final_html)"""
