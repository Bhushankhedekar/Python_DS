# Exception handling
# Exception is an error that occurs during the execution of a program.
#  When an exception occurs, the normal flaw of the program is interrupted 
# and the program terminates. To handle exceptions, we can use the try-except block.
# try
# except
# else
# finally 
# raise

# print("Start code")
# try:
#     num1 = int(input("Enter a number:"))
#     print(78/num1)
# # except Exception as e:
# #     print("An error occured:",e)
# except ValueError:
#     print("Entera valid number:")
# except ZeroDivisionError:
#     print("Number cannot be zero:")
# else :
#     print("No exception occured")
# finally:
#     print("End code")

# Homework
# Create exception for 
# Accept age from user for licence
# 1.AgeTooLow error
# 2.AgeTooHigh error
class AgeTooLowError(Exception):
    """Raised when age is below the minimum allowed (18)."""
    pass

class AgeTooHighError(Exception):
    """Raised when age is above the maximum allowed (120)."""
    pass

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise AgeTooLowError("Age must be at least 18.")
    elif age > 120:
        raise AgeTooHighError("Age cannot exceed 120.")
    else:
        print("Valid age. License application approved.")

except ValueError:
    print("Please enter a valid number.")
except AgeTooLowError as e:
    print(f"Error: {e}")
except AgeTooHighError as e:
    print(f"Error: {e}")   