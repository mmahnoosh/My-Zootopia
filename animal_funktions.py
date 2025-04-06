import json


def load_data(file_path):
    """ Loads a JSON file
        Args:
            file_path (str): The path to the JSON file to be loaded.
        Returns:
            dict or list: The parsed JSON content, depending on the structure of the file.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animals_data():
    """
        Loads animal data from the default 'animals_data.json' file.
        Returns:
            list: A list of animal dictionaries loaded from the JSON file.
    """
    return load_data('animals_data.json')


def serialize_animal(animal):
    """
        Converts a single animal dictionary into an HTML list item string.
        Args:
            animal (dict): A dictionary containing data about one animal,
                           including its name, locations, and characteristics.
        Returns:
            str: A string containing HTML markup representing the animal's information.
        """
    locations = ", ".join(animal['locations'])
    animal_type = animal['characteristics'].get('type', ' - ')
    animal_skin_type = animal['characteristics'].get('skin_type', ' - ')
    animal_top_speed = animal['characteristics'].get('top_speed', 'Unknown')
    return f"""
          <li class="cards__item">
              <div class="card__title">{animal['name']}</div>
              <div class="card__text">
                  <ul>
                      <li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>
                      <li><strong>Location:</strong> {locations}</li>
                      <li><strong>Type:</strong> {animal_type}</li>
                      <li><strong>skin_type:</strong> {animal_skin_type}</li>
                      <li><strong>Top_speed:</strong> {animal_top_speed}</li>

                  </ul>    
              </div>
          </li>
      """


def show_animals():
    animals_dataset = get_animals_data()

    # Create an empty list to store HTML entries for each animal
    animal_entries = []

    # Loop through each animal and generate the HTML using the serialize function
    for animal in animals_dataset:
        animal_entries.append(serialize_animal(animal))

    # Join all individual animal HTML entries into one big string
    animals_html = "\n".join(animal_entries)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

def filter_list(user_filter):
    print(f"User Filter: {user_filter}")
    animal_entries = []
    animals_dataset = get_animals_data()
    print(animals_dataset)
    for animal in animals_dataset:
        print(animal['characteristics']['skin_type'])
        if (animal['characteristics']['skin_type']) == user_filter:
            animal_entries.append(serialize_animal(animal))

    # Join all individual animal HTML entries into one big string
    animals_html = "\n".join(animal_entries)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

def show_skin_type():
    animal_skin_type = []
    animals_dataset = get_animals_data()
    for animal in animals_dataset:
        animal_skin_type.append(animal['characteristics']['skin_type'])
    return set(animal_skin_type)


