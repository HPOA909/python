#10.2.2: Multiple exception types in a single exception handler

user_input = input("enter divisor: ")
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        # Possible ZeroDivisionError
        print(60 // divisor) # Truncates to an integer
    except ValueError:
        print('v')
    except ZeroDivisionError:
        print('z')
    user_input = input()
print('OK')