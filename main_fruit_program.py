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


def menu():

    my_menu = [
        ["R", "Review"],
        ["Q", "Quit"]
    ]

    base_list = [
        ["Orange", "10"],
        ["Apple","6"],
        ["Mango","16"],
        ["Blueberry packets","3"]
    ]

    run = True
    while run == True:
        for i in range(0, len(my_menu)):
            print("{:3} : {}".format(my_menu[i][0], my_menu[i][1]))
        option = get_string("Please choose option: -> ")
        print("." * 60)
        if option == "R":
            single_loop_print(base_list)
            print("." *60)
        elif option == "Q":
            print("Quitting...")
            run = False
        else:
            print("Invalid Entry")


if __name__ == "__main__":
    menu()
