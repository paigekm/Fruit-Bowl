def get_validated_integer(M, min, max):
    while True:
        try:
            integer_entry = int(input(M))
        except ValueError:
            print("This is not a valid entry. A whole number is needed")
            continue
        if integer_entry < min:
            print("Your entry value is too small")
        elif integer_entry > max:
            print("Your entry value is too large")
        else:
            return integer_entry



if __name__ == "__main__":
    test_num = get_validated_integer("PLease enter a number: ->", 0, 5)
    print(test_num)