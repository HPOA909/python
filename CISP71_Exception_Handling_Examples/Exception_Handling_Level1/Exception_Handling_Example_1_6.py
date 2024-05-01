#Reference https://www.journaldev.com/14454/python-custom-exception
#Raising an Exception
#Your can raise an existing exception by using raise keyword. So, you just simply write raise keyword and then the name of the exception.

def input_age(age):
    try:
        if(int(age) <=18):
            raise ZeroDivisionError
    except ValueError:
       return 'ValueError: Cannot convert into int'
    else:
       return 'Age is saved successfully'


print(input_age('23'))  # This will execute properly
print(input_age('18'))  # This will not execute properly 