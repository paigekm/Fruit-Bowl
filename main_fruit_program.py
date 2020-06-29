"""A program to manage a fruit bowl."""

from validations import get_validated_integer, get_validated_string
import math


def single_loop_print(l):
    """Print the list.

    :param l: list
    :return: None

    Print the list in a nice format and only once.
    """
    for i in range(0, len(l)):
        output = "{:10} --- {:^10}".format(l[i][0], l[i][1])
        print(output)


def print_with_indexes(l):
    """Print the user's list with indexes.

    :param l: list
    :return: None
    """
    for i in range(0, len(l)):
        output = "{:3} : {:10} {:10} ".format(i, l[i][0], l[i][1])
        print(output)


def fill_fruitbowl(l):
    """Add new fruit and quantity to the list.

    :param l: list
    :return: None

    The required list must be two-dimensional,
    and the sub list must be of the form [str, int],
    requests user input for index and quantity,
    prints confirmation.
    """
    type_of_fruit = get_validated_string("What fruit would you "
                                         "like to add to the bowl?", 3, 20)
    quantity_of_fruit = get_validated_integer("How many of that fruit would "
                                              "you like to add?", 0, math.inf)
    temporary_list = [type_of_fruit, quantity_of_fruit]
    l.append(temporary_list)
    print("." * 60)
    print("You have entered {} {}s in the fruit bow"
          "l!".format(quantity_of_fruit, type_of_fruit))
    print("." * 60)


def update_fruitbowl(l):
    """Take away or add fruit to the fruit bowl.

    :param l: list
    :return: None

    the required updated list is two-dimensional,
    and the sub list must be of the form [str, int],
    prints list of fruit with indexes,
    requests user input for index and new quantity,
    requests user input for either add or subtract function to run
    changes quantity for that fruit
    prints confirmation.
    """
    # test that the list has something in it.
    if len(l) == 0:
        print("There is nothing in your fruit bowl")
        return None
    print_with_indexes(l)
    my_index = get_validated_integer("Please choose the index "
                                     "number of the fruit you would "
                                     "like to change?", 0, len(l) - 1)
    add_or_subtract = get_validated_string("Enter 'A' to add, or any other "
                                           "key to subtract fruit: "
                                           "-> ", 1, 1).upper()
    if add_or_subtract == "A":
        amount_fruit_added = get_validated_integer("How "
                                                   "many {}s do you want "
                                                   "to add?".format
                                                   (l[my_index][0]), 1, 50)
        l[my_index][1] += amount_fruit_added
        print("." * 60)
        add_confirmation = "You have now added {} {}s to your fruit " \
                           "bowl!".format(amount_fruit_added, l[my_index][0])
        print(add_confirmation)
    else:
        amount_fruit_subtracted = get_validated_integer("How many {}s do you "
                                                        "want to take "
                                                        "away?".format
                                                        (l[my_index][0]),
                                                        1, l[my_index][1])
        l[my_index][1] -= amount_fruit_subtracted
        print("." * 60)
        sub_confirmation = "You have now removed {} {}s from your fruit bowl" \
                           "!".format(amount_fruit_subtracted, l[my_index][0])
        print(sub_confirmation)


# prints out the numbers of fruit.
def total_fruit(l):
    """Calculate total amount of fruit in the bowl.

    :param l: list
    :return: None

    calculates orginal sum as 0,
    updates this sum each time with amount of each fruit,
    prints a confirmation message for total fruit bowl contents.
    """
    # before the summing begins.
    total_sum = 0
    for i in range(0, len(l)):
        total_sum = total_sum + l[i][1]
    print("You have {} fruit items in your fruit bowl".format(total_sum))


def menu():
    """Print menu options.

    :return: None

    requests user menu choice,
    calls different functions depending on which menu option was chosen.
    """
    # fruitbowl_list = []
    full_bowl = [
        ["Orange", 10],
        ["Pear", 4],
        ["Carrot", 12]
    ]
    fruitbowl_list = full_bowl

    my_menu = [
        ["A", "Add fruit items"],
        ["R", "Review the contents of your fruit bowl"],
        ["C", "Change quantity of a fruit you have in the bowl"],
        ["T", "Find the total number of fruit in the bowl"],
        ["Q", "Quit"],
    ]

    run = True
    while run is True:
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = get_validated_string("Please choose an "
                                      "option: -> ", 1, 1).upper()
        print("." * 60)
        if option == "R":
            single_loop_print(fruitbowl_list)
            print("." * 60)
        elif option == "C":
            update_fruitbowl(fruitbowl_list)
            print("." * 60)
        elif option == "A":
            fill_fruitbowl(fruitbowl_list)
        elif option == "T":
            total_fruit(full_bowl)
        elif option == "Q":
            print("Quitting...")
            run = False
        else:
            print("Invalid Entry")


if __name__ == "__main__":
    menu()
