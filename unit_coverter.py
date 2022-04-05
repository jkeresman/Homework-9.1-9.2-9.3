def covert_km_miles(km):

    return km * 0.621371192


def kilometers_input():

    while True:
        try:
            km = float(input("Enter a number in kilometres:  "))
            break
        except ValueError:
            print("Wrong input please try again!!")
    return km


def another_conversion():
    flag = True

    while True:
        answer = input("Do you want to do another conversion [yes/no] ?  ")
        if answer.lower() == "no" or answer.lower == "yes":
            flag = False
            break
        elif answer.lower() == "yes":
            print("I'm glad to hear that, enter required parameters again!!")
            break
        else:
            print("Wrong input!!")

    return flag


print("Hello there , function of this program is to convert kilometers to miles\n")

again_flag = True

while again_flag:

    kilometers = kilometers_input()
    miles = covert_km_miles(kilometers)
    print(f"{kilometers} km -> {miles} miles")
    again_flag = another_conversion()
