def let_user_pick(options):
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None


options = [ "Option 1", "Option 2", "Option3"]
res = let_user_pick(options)

print(options[res])




def let_user_pick(options):
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None


options = [Receivers]
res = let_user_pick(options)

print(options[res])