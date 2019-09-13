def return_user_business():
    age = input("Enter your age as integer: ")

    try:
        age = int(age)
    except ValueError as e:
        print("This is not an integer")
        return
    
    if age < 0:
        print("don't belive you")
    elif age >= 0 and age < 6:
        print("you should go to kindergarden")
    elif age >= 6 and age < 17:
        print("you should go to school")
    elif age >= 17 and age < 23:
        print("you should go to university")
    elif age >= 23 and age < 60:
        print("you should go to work")
    else:
        print("do whatever you want")
        
return_user_business()