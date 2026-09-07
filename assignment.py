while True:
    try:
        age= int(input("Enter your age:"))
        print("your age is:", age)
        break
    except ValueError: print ("invalid input.please enter a valid integer.")



