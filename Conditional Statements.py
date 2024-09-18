
def check_num(num):
    if num > 0:
        print(f"{num} is a positive number.")
    elif num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"The number is zero.")


number = int(input("Enter a number: "))
check_num(number)
