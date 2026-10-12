def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None, "Error: Division by 0 is not allowed!" #Replaced zero by 0
    return a / b, None

def check_even_odd(num):
    return "Even" if int(num) % 2 == 0 else "Odd"

def calculate_percentage(a, b):
    if b == 0:
        return None, "Error: Division by 0 is not allowed!" #Replaced zero by 0
    return (a / b) * 100, None


def calculator():
    while True:
        print("\n----- Calculator -----")
        print("1. Addition (+)") #Added Signs 
        print("2. Subtraction (-)") #Added Signs
        print("3. Multiplication (*)") #Added Signs
        print("4. Division (/)") #Added Signs
        print("5. Check Even/Odd")
        print("6. Percentage (%)") #Added Signs
        print("7. Exit")
        
        try:
            option = int(input("Enter Your Choice (1-7): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        if option == 7:
            print("Exiting program. ") #Changed the string
            break

        if option < 1 or option > 7:
            print("Invalid Option! Please choose between 1 and 7.")
            continue

        try:
            a = float(input("Enter First Number: "))
            b = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if option == 1:
            print(f"Result (Addition): {add(a, b)}")
            
        elif option == 2:
            print(f"Result (Subtraction): {subtract(a, b)}")
            
        elif option == 3:
            print(f"Result (Multiplication): {multiply(a, b)}")
            
        elif option == 4:
            result, error = divide(a, b)
            if error:
                print(error)
            else:
                print(f"Result (Division): {result}")
                
        elif option == 5:
            print(f"Number {a} is {check_even_odd(a)}")
            print(f"Number {b} is {check_even_odd(b)}")
            
        elif option == 6:
            result, error = calculate_percentage(a, b)
            if error:
                print(error)
            else:
                print(f"Percentage: {result}%")

if __name__ == "__main__":
    calculator()