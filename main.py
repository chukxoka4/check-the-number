def accept_user_input():
    user_input = input("Enter a number you are thinking about: ")
    process_user_input(user_input)
    process_user_stopper()

def process_user_input(user_input):
        try:
            data = int(user_input)
            if data%2 == 0:
                print(f"You entered {user_input} and it is an even number")
            else:
                print(f"You entered {user_input} and it is an odd number")
        except ValueError:
            print ("Apparently you did not enter a number!")

def process_user_stopper():
    user_stopper = input("Do you want to continue (y/n): ")
    try:
        data = str(user_stopper)
        if data.lower() == 'y' or data.lower() == 'yes':
            accept_user_input()
        if data.lower() == 'n' or data.lower() == 'no':
            print("Thank you for using this program!")
            exit()
    except ValueError:
            print ("That was not a valid option! Please try again!") 
            process_user_stopper()


if __name__ == "__main__":
    while True:
        accept_user_input()