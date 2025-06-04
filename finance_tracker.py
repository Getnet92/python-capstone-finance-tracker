expenseDict = {} # dictionary to be used in addExpense to create dictionary to be maniputed
def addExpense():# creates a dictionary with a key of categoryName and a value(tuple) of expenseDesc and expenseAmount
    answer = "y" # initializing answer with y to start the while loop
    while answer == "y":
        try:
            expenseDesc = str(input("Enter expense description:  ")) # prompting and recieving the expense description
            if not expenseDesc.strip(): # stripping any white space to make sure the user didn't input a set of white spaces
                print("The expense description can not be empty") # message prompt if user only inputted white spaces
                continue # restarting loop 
            categoryName =  str(input("Enter category(Food, Gym, Bills, Emergency): "))
            if not categoryName.strip(): # stripping any white space to make sure the user didn't input a set of white spaces
                print("The category name can't be empty, please start over") # message prompt if user only inputted white spaces
                continue # restarting loop 
        except ValueError: # value error raised if user entered value that is not a string
            print("Non string values can't be used for expense description and expense name. Please start over") # error message if a non string varialbe is detected
        except Exception as e: # error raised if unexpected error occurs
            print("An unexpected error has occured, please start over") # message to be displayed if unexpected error occurs
            continue # restarting loop 
        else:
            try:
                    expenseAmount = float(input("Enter amount: "))
            except ValueError:
                    print("Non numeric input detected, please start over.")
            except Exception as e: # error raised if unexpected error occurs
                print("An unexpected error has occured.") # message to be displayed if unexpected error occurs
            else: # code to run if no exception was raised
                expense = (expenseDesc, expenseAmount) # creates the tuple out of expenseDesc and expenseAmoun
                if categoryName != " ": #Only runs is the categoryName is not a white space
                    expenseDict[categoryName] = expense # assigns the key categoryName to the tuple expense
                print("Expense added successfully")
                answer = str(input("Do you want to add another Expense? (y/n) "))

def view_expenses(dict): # takes in a dictionary dict and displays the key and values
    for key in dict: # loop taking the keys(category) and the value(expense - tuple of expenseDesc and expenseAmount)
        print( str(key) +" \n -"  + str(dict[key])) # displays the appropriate message formatted like the example

def view_summary(dict): # takes in a dictionary dict and displays a summary with the amount fromt the tuple expense
    print("Summary: ") 
    for key in dict: # loop designed with the iterator being keys from the dictionary dict
        tempTuple = dict[key] # assigning the expense from each iteration to a temporary tuple
        amountTuple = tempTuple[1] # assigning the second value or the expense amount to amountTuple
        print(str(key) + ": $" + str(amountTuple)) # displays the categoryName and the amountTupe at each key(CategoryName)

def menuLogic(): # creates a menue that displays the optins and receieves the asnwe to run other functions
    print("Welcome to the Personal Finace Tracker") # display welcome message
    choice = 0 # initializing choice wiht 0 to start the loop
    while choice !=4:
        try: 
            choice = int(input("What would you like to do? \n 1. Add expense \n 2. View All Expenses \n 3. vew Summary \n 4. Exit \nChoose an option: "))
        except ValueError: # checking for a variable type error
            print("Please enter an integer")
        except Exception as e: # error raised if unexpected error occurs
            print("Unexpected error, please start over") # message to be displayed if unexpected error occurs
        if (1<choice and 5<choice): # restarts loop if the choice variable isn't within 1-4 inclusive
                print("Please enter a number between (1 - 4).")
                continue # restarting loop 

        else: # runs if no exception is raised
            if choice == 1: # Based on user choice runs the appropriate function
                addExpense()
            elif choice == 2:
                if expenseDict == {}: # runs if user hasn't entered any expenses 
                    print("Your expense report doesn't exist yet. \n Please add an expense first") # message displayed to let user know they have to add expenses first
                else:
                    view_expenses(expenseDict)
            elif choice == 3:
                    if expenseDict == {}:
                        print("Your expense report doesn't exist yet. \n Please add an expense first") # message displayed to let user know they have to add expenses first
                    else:
                        view_summary(expenseDict)
            elif choice ==4: # terminates the loop after displaying message
                print("Goodbye!") # Message informing of loop termination

menuLogic() # runs the menu fucntion to start the code






