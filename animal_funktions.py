def save_animals(animals):
    """
    Gets all your animals as an argument and saves them to the html file.
    """
    try:
        with open("animals.json", "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=4)
        print("Movies successfully saved!")
    except IOError:
        print("Error: Unable to save the movies.")