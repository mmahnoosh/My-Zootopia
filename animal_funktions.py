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

    This function takes an animal's data and returns a string containing HTML markup
    representing the animal's key information, formatted as a list item. It handles
    missing data gracefully by providing default values.

    Args:
        animal (dict): A dictionary containing information about an animal.
                       Expected keys include:
                         - 'name' (str)
                         - 'locations' (list of str, optional)
                         - 'characteristics' (dict), which may include:
                           - 'diet' (str)
                           - 'type' (str)
                           - 'skin_type' (str)
                           - 'top_speed' (str or number)

    Returns:
        str: A string of HTML markup representing the animal's information in list item format.
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


def load_html_template(template_path='animals_template.html'):
    """
   Loads and returns the contents of an HTML template file as a string.

   This function reads the specified HTML file (default is 'animals_template.html')
   using UTF-8 encoding and returns its content for further processing.

   :param template_path: (Optional) Path to the HTML template file.
                         Default is 'animals_template.html'.
   :return: The content of the HTML template as a string.
   """

    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_html_file(content, output_path='animals.html'):
    """
   Writes the provided HTML content to a file.

   This function saves the given content string into an HTML file using UTF-8 encoding.
   By default, it writes to 'animals.html', but a different output path can be specified.

   :param content: The HTML content to be written to the file.
   :param output_path: (Optional) The file path where the content should be saved.
                       Default is 'animals.html'.
   :return: None
   """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def generate_animal_html(user_filter="all"):
    """
        Generates an HTML file displaying animal information filtered by skin type.

        If a specific skin type is provided via user_filter, only animals with that
        skin type will be included. If 'all' is passed (default), all animals will
        be included. The function serializes the matching animals, inserts them
        into a preloaded HTML template, and writes the final result to an HTML file.

        :param user_filter: (Optional) The skin type to filter animals by (e.g., 'fur', 'scales').
                            Use "all" to include every animal. Default is "all".
        :return: None
        """
    animal_entries = []
    animals_dataset = get_animals_data()
    for animal in animals_dataset:
        skin_type = animal.get('characteristics', {}).get('skin_type')
        if skin_type == user_filter or user_filter == "all":
            animal_entries.append(serialize_animal(animal))

    animals_html = "\n".join(animal_entries)
    html_template = load_html_template()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    write_html_file(final_html)


def is_filter_valid(user_filter):
    """
   Checks if the given user_filter value exists among the 'skin_type' values
   of the animals returned by get_animals_data.

   A generator is used to iterate over each animal's 'skin_type' (if available),
   and the function returns True if user_filter matches any of them.

   :param user_filter: The skin type to validate (e.g., 'fur', 'scales', etc.)
   :return: True if the filter is valid (i.e., exists in the data), False otherwise
   """

    skin_type_template = (animal.get('characteristics', {}).get('skin_type')
                          for animal in get_animals_data()
                          if animal.get('characteristics', {}).get('skin_type'))
    return user_filter in skin_type_template
