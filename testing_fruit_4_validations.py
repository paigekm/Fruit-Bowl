from validations import get_validated_integer, get_validated_string
import math


def single_loop_print(L):
    """
    prints the list that the user has filled
    prints the list in a better format and only once

    :param L: list
    :return: None
    """
    for i in range(0, len(L)):
        output = "{:10} --- {:^10}".format(L[i][0], L[i][1])
        print(output)


def print_with_indexes(L):
    """
    prints the user's list with indexes

    :param L: list
    :return: None
    """
    for i in range(0, len(L)):
        output = "{:3} : {:10} {:10} ".format(i,L[i][0], L[i][1])
        print(output)


def fill_fruitbowl(L):
    """
    the required list is two-dimensional, and the sub list must be of the form [str, int],
    requests user input for index and quantity,
    adds new fruit and quantity to the list,
    prints confirmation

    :param L: list
    :return: None
    """
    type_of_fruit = get_validated_string("What fruit would you like to add to the bowl?",3,20)
    quantity_of_fruit = get_validated_integer("How many of that fruit would you like to add?",0, math.inf)
    temporary_list = [type_of_fruit, quantity_of_fruit]
    L.append(temporary_list)
    print("." * 60)
    print("You have entered {} {}s in the fruit bowl!".format(quantity_of_fruit, type_of_fruit))
    print("." * 60)


def update_fruitbowl(L):
    """
    the required updated list is two-dimensional, and the sub list must be of the form [str, int],
    prints list of fruit with indexes,
    requests user input for index and new quantity,
    requests user input for either add or subtract function to run
    changes quantity for that fruit
    prints confirmation

    :param L:
    :return: None
    """
    #test that the list has something in it.
    if len(L)==0:
        print("There is nothing in your fruit bowl")
        return None
    print_with_indexes(L)
    my_index = get_validated_integer("Please choose the index number of the fruit you would like to change?",0,len(L)-1)
    add_or_subtract = get_validated_string("Enter 'A' to add, or any other key to subtract fruit: -> ", 1,1).upper()
    if add_or_subtract == "A":
        amount_fruit_added = get_validated_integer("How many {}s do you want to add?".format(L[my_index][0]),1,50)
        L[my_index][1] += amount_fruit_added
        print("." * 60)
        add_confirmation = "You have now added {} {}s to your fruit bowl!".format(amount_fruit_added, L[my_index][0])
        print(add_confirmation)
    else:
        amount_fruit_subtracted = get_validated_integer("How many {}s do you want to take away?".format(L[my_index][0]),1,L[my_index][1])
        L[my_index][1] -= amount_fruit_subtracted
        print("." * 60)
        sub_confirmation = "You have now removed {} {}s from your fruit bowl!".format(amount_fruit_subtracted, L[my_index][0])
        print(sub_confirmation)


def menu():
    """
    prints menu options
    requests user menu choice
    calls different functions depending on which menu option was chosen

    :return: None
    """

    #fruitbowl_list = []
    full_bowl = [
        ["Orange",10],
        ["Pear", 4],
        ["Carrot", 12]
    ]
    fruitbowl_list = full_bowl

    my_menu = [
        ["A", "Add fruit items"],
        ["R", "Review the contents of your fruit bowl"],
        ["C", "Change quantity of a fruit you have in the bowl"],
        ["Q", "Quit"],
    ]

    run = True
    while run == True:
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = get_validated_string("Please choose an option: -> ",1,1).upper()
        print("." * 60)
        if option == "R":
            single_loop_print(fruitbowl_list)
            print("." * 60)
        elif option == "C":
            update_fruitbowl(fruitbowl_list)
            print("." * 60)
        elif option == "A":
            fill_fruitbowl(fruitbowl_list)
        elif option == "Q":
            print("Quitting...")
            run = False
        else:
            print("Invalid Entry")


if __name__ == "__main__":
    menu()