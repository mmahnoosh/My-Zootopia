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
    return f"""
          <li class="cards__item">
              <div class="card__title">{animal['name']}</div>
              <div class="card__text">
                  <ul>
                      <li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>
                      <li><strong>Location:</strong> {locations}</li>
                      <li><strong>Type:</strong> {animal_type}</li>
                      <li><strong>skin_type:</strong> {animal_skin_type}</li>
                  </ul>    
              </div>
          </li>
      """