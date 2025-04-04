
import animal_funktions


def main():
    animals_dataset = animal_funktions.get_animals_data()
    animal_entries = []

    for animal in animals_dataset:
        animal_entries.append(animal_funktions.serialize_animal(animal))
    animals_html = "\n".join(animal_entries)
    with open('animals_template.html', 'r', encoding='utf-8') as f:
        html_template = f.read()

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open('animals.html', 'w', encoding='utf-8') as f:
        f.write(final_html)


if __name__ == "__main__":
    main()
