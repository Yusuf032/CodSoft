def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b
    
def multi(a,b):
    return a*b
    
def divi(a,b):
    if y ==0:
        return "error divied by 0"
    return a/b
    

def main():
    print("SIMPLE CALCULATOR")
    print("Select operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Select Opertaion: ")

        if choice in ["1","2","3", "4"]:
            num1 = float(input("Enter the 1st Number: "))
            num2 = float(input("Enter the 2nd Number: "))

            if choice == '1':
                print(f"The answer of {num1} + {num2} = {add(num1,num2)}")
            elif choice == '2':
                print(f"The answer of {num1} - {num2} = {sub(num1,num2)}")
            elif choice == '3':
                print(f"The answer of {num1} * {num2} = {multi(num1,num2)}")
            elif choice == '1':
                print(f"The answer of {num1}/{num2} = {divi(num1,num2)}")

            else:
                print("Invalid input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Goodbye!")







if __name__ == "__main__":
    main()