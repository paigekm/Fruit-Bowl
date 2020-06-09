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


def fill_fruitbowl(L):
    type_of_fruit = get_string("What fruit would you like to add to the bowl?")
    quantity_of_fruit = get_integer("How many of that fruit would you like to add?")
    temporary_list = [type_of_fruit, quantity_of_fruit]
    L.append(temporary_list)
    print("." * 60)
    print("You have entered {} {}s in the fruit bowl!".format(quantity_of_fruit, type_of_fruit))
    print("." * 60)


def menu():
    fruitbowl_list = []
    my_menu = [
        ["A", "Add fruit items"],
        ["R", "Review"],
        ["Q", "Quit"],
    ]

    run = True
    while run == True:
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = get_string("Please choose option: -> ").upper()
        print("." * 60)
        if option == "R":
            single_loop_print(fruitbowl_list)
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

