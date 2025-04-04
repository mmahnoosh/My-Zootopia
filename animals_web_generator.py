import animal_funktions


def main():
    """
        Generates the final HTML page by:
        - Loading animal data from a JSON file
        - Converting each animal into an HTML block
        - Replacing a placeholder in the HTML template
        - Saving the result to a new HTML file
        """

    animals_dataset = animal_funktions.get_animals_data()

    # Create an empty list to store HTML entries for each animal
    animal_entries = []

    # Loop through each animal and generate the HTML using the serialize function
    for animal in animals_dataset:
        animal_entries.append(animal_funktions.serialize_animal(animal))

    # Join all individual animal HTML entries into one big string
    animals_html = "\n".join(animal_entries)

    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)


if __name__ == "__main__":
    main()
