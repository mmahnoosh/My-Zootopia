from colorama import Fore, Style
import animal_funktions


def get_user_input():
    """
       Handles user input to either display all animals or filter them by skin type.

       This function prompts the user to choose between viewing all animals or filtering
       them by a specific skin type. Based on the user's choice:
         - If 'a' is selected, it calls the function to display all animals and exits.
         - If 'f' is selected, it shows the available skin types, prompts for a filter value,
           and displays the filtered list if the input is valid.
         - If the user input is invalid (neither 'a' nor 'f', or an invalid skin type),
           an appropriate error message is displayed, and the prompt repeats.

       Uses color formatting via the `colorama` library for better console readability.
       """

    print(Fore.LIGHTYELLOW_EX + "=================================== Animals"
                                " ==========================================")
    while True:
        choice = input(
            f"{Fore.GREEN} Do you want to see all animals or filter them? ({Fore.LIGHTYELLOW_EX}'a'"
            f" {Fore.GREEN}for{Fore.LIGHTMAGENTA_EX} all{Fore.GREEN} or {Fore.LIGHTYELLOW_EX}'f' {Fore.GREEN}for{Fore.LIGHTMAGENTA_EX} filter{Fore.GREEN}): "
            .strip().lower())

        if choice == "a":
            animal_funktions.generate_animal_html()
            exit()

        elif choice == "f":
            while True:
                filter_value = input(
                    f"{Fore.LIGHTMAGENTA_EX}Which skin type would you like to see? ").strip().capitalize()
                if animal_funktions.is_filter_valid(filter_value):
                    animal_funktions.generate_animal_html(filter_value)
                    exit()
                print("Skin Type is not valid!")

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

    get_user_input()


if __name__ == "__main__":
    main()
