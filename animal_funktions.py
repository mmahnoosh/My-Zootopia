import json


def save_animals(animals):
    """
    Gets all your animals as an argument and saves them to the html file.
    """
    try:
        with open("animals.json", "w", encoding="utf-8") as file:
            json.dump(animals, file, indent=4)
        print("Animal successfully saved!")
    except IOError:
        print("Error: Unable to save the animal.")

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animals_data():
    return load_data('animals_data.json')

def serialize_animal(animal):
    locations = ", ".join(animal['locations'])
    animal_type = animal['characteristics'].get('type', '-')
    return f"""
          <li class="cards__item">
              <div class="card__title">{animal['name']}</div>
              <p class="card__text">
                  <strong>Diet:</strong> {animal['characteristics']['diet']}<br/>
                  <strong>Location:</strong> {locations}<br/>
                  <strong>Type:</strong> {animal_type}<br/>
              </p>
          </li>
      """