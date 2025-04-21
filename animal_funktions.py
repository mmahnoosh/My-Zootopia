import json


def load_data(file_path):
    """ Loads a JSON file
        Args:
            file_path (str): The path to the JSON file to be loaded.
        Returns:
            dict or list: The parsed JSON content, depending on the structure of the file.
    """
    with open(file_path, "r", encoding='utf-8') as handle:
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
        animal (dict): A dictionary containing information about an animal.
                       Expected keys include:
                         - 'name' (str)
                         - 'locations' (list of str, optional)
                         - 'characteristics' (dict) with keys like 'diet', 'type',
                           'skin_type', and 'top_speed'.

    Returns:
        str: A string of HTML markup representing the animal's information as a list item.
    """
    locations_list = animal.get('locations', [])
    locations = ", ".join(locations_list) if isinstance(locations_list, list) else 'Unknown'
    characteristics = animal.get('characteristics', {})
    return f"""
          <li class="cards__item">
              <div class="card__title">{animal['name']}</div>
              <div class="card__text">
                  <ul>
                      <li><strong>Diet:</strong> {characteristics.get('diet', ' - ')}</li>
                      <li><strong>Location:</strong> {locations}</li>
                      <li><strong>Type:</strong> {characteristics.get('type', ' - ')}</li>
                      <li><strong>Skin type:</strong> {characteristics.get('skin_type', ' - ')}</li>
                      <li><strong>Top speed:</strong> {characteristics.get('top_speed', 'Unknown')}</li>

                  </ul>    
              </div>
          </li>
      """


def filter_list(user_filter):
    """
    Filters a list of animals based on a given skin type and generates an HTML file.

    This function loads a dataset of animals and filters those whose skin type matches
    the provided `user_filter`. It converts the filtered animals into HTML entries,
    replaces a placeholder in an HTML template with these entries, and writes the
    final content to a file named 'animals.html'.

    Parameters:
        user_filter (str): The desired skin type to filter by (e.g., 'fur', 'scales', 'skin').
                           If set to 'all', no filtering is applied and all animals are included.

    """
    animal_entries = []
    animals_dataset = get_animals_data()
    for animal in animals_dataset:
        skin_type = animal.get('characteristics', {}).get('skin_type')
        if skin_type == user_filter or user_filter == "all":
            animal_entries.append(serialize_animal(animal))

    animals_html = "\n".join(animal_entries)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)


def generate_animal_html(user_filter="all"):
    animal_entries = []
    animals_dataset = get_animals_data()
    for animal in animals_dataset:
        skin_type = animal.get('characteristics', {}).get('skin_type')
        if skin_type == user_filter or user_filter == "all":
            animal_entries.append(serialize_animal(animal))

    animals_html = "\n".join(animal_entries)
    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)