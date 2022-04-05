def correct_range_check(num):
    return 1 < num < 100


def divisible_with_five(num):
    return num % 5 == 0


def divisible_with_three(num):
    return num % 3 == 0


def number_input(num):

    while not correct_range_check(num):
        num = number_input_check()
        if not correct_range_check(num):
            print("Wrong input. Please try again!!!")
    return num


def number_input_check():

    while True:
        try:
            num = int(input("Enter a number (1 - 100) :  "))
            break
        except ValueError:
            print("Wrong input. Please try again!!")
    return num


number = 0


for i in range(1, number_input(number)):

    if divisible_with_three(i) and divisible_with_five(i):
        print("FizzBuzz")
    elif divisible_with_five(i):
        print("Buzz")
    elif divisible_with_three(i):
        print("Fizz")
    else:
        print(i)
