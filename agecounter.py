def check_age():
    age_input = input('enter your age')
    try:
        age = int(age_input)
        if age <= 0 or age > 150:
            print('Error invalid age')
            return
    except ValueError:
        print('Error Age has to be a number.')
        return
    if age % 2 == 0:
        print(f'Age is even')
    else:
        print(f'Age is odd.')
check_age()