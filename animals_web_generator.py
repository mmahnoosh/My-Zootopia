import colorama
from colorama import init, Fore, Back, Style
import animal_funktions


def get_user_input():
    while True:
        choice = input(
            Fore.GREEN + 'Do you want to see all animals or filter them? ("a" for all or "f" for filter): '
            + Style.RESET_ALL).strip().lower()

        if choice == "a":
            animal_funktions.show_animals()
            exit()

        elif choice == "f":
            skin_types = animal_funktions.show_skin_type()
            filter_value = input(
                f"{Fore.LIGHTMAGENTA_EX}Which skin type would you like to see? "
                f"{Fore.LIGHTYELLOW_EX}{skin_types}"
            ).strip().capitalize()
            if filter_value in skin_types:
                animal_funktions.filter_list(filter_value)
                exit()

            else:
                print(Fore.RED + "Invalid skin type. Please try again." + Style.RESET_ALL)

        else:
            print(Fore.RED + "Invalid input. Please enter 'a' or 'f'." + Style.RESET_ALL)


def main():
    """
        Generates the final HTML page by:
        - Loading animal data from a JSON file
        - Converting each animal into an HTML block
        - Replacing a placeholder in the HTML template
        - Saving the result to a new HTML file
        """

    autoreset = True
    get_user_input()


if __name__ == "__main__":
    main()
