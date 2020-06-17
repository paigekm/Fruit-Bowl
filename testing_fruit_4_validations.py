from validations import get_validated_integer

def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(message):
    my_integer = int(input(message))
    return my_integer


def review_fruit():
    print("review fruit function")
    return None


def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{:10} --- {:^10}".format(L[i][0], L[i][1])
        print(output)


def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{:3} : {:10} {:10} ".format(i,L[i][0], L[i][1])
        print(output)


def fill_fruitbowl(L):
    type_of_fruit = get_string("What fruit would you like to add to the bowl?")
    quantity_of_fruit = get_validated_integer("How many of that fruit would you like to add?",0,200)
    temporary_list = [type_of_fruit, quantity_of_fruit]
    L.append(temporary_list)
    print("." * 60)
    print("You have entered {} {}s in the fruit bowl!".format(quantity_of_fruit, type_of_fruit))
    print("." * 60)


def update_fruitbowl(L):
    #test that the list has something in it.
    if len(L)==0:
        print("There is nothing in your fruit bowl")
        return None
    print_with_indexes(L)
    my_index = get_integer("Please choose the index number of the fruit you would like to change?")
    add_or_subtract = get_string("Enter 'A' to add, or any other key to subtract fruit: -> ").upper()
    if add_or_subtract == "A":
        amount_fruit_added = get_integer("How many {}s do you want to add?".format(L[my_index][0]))
        L[my_index][1] += amount_fruit_added
        print("." * 60)
        add_confirmation = "You have now added {} {}s to your fruit bowl!".format(amount_fruit_added, L[my_index][0])
        print(add_confirmation)
    else:
        amount_fruit_subtracted = get_integer("How many {}s do you want to take away?".format(L[my_index][0]))
        L[my_index][1] -= amount_fruit_subtracted
        print("." * 60)
        sub_confirmation = "You have now removed {} {}s from your fruit bowl!".format(amount_fruit_subtracted, L[my_index][0])
        print(sub_confirmation)



def menu():
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
        option = get_string("Please choose an option: -> ").upper()
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