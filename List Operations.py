numbers_list = [20, 60, 10, 80, 30, 70]

if len(numbers_list) == 0:
    print("The list is empty.")
else:
    largest = numbers_list[0]
   
    for number in numbers_list:
        if number > largest:
            largest = number
            
    print(f"The largest number in the list is: {largest}")
