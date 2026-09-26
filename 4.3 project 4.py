from datetime import datetime
import csv

print("Leajon3478 Spreadsheet Automation Menu")

#Menu options stored in a list
menuOptions = [
    "Input Data",
    "View Current Data",
    "Generate Report"
]

#For loop
print("\nMenu Options:")
for i in range(len(menuOptions)):
    print(f"{i + 1}. {menuOptions[i]}")

choice = input("\nEnter the number of your choice: ")

if choice.isdigit():
    choiceNumber = int(choice)

    if 1 <= choiceNumber <= len(menuOptions):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #The next line retrieves the inputted
        #option and stores into the variable
        #called choice.
        print(f"\nYou selected option {choiceNumber} at {timestamp}.")
    else:
        print("\nError: Invalid choice selected.")
else:
    print("\nError: Invalid choice selected.")

#InsertData function
def insertData(path, csv_string):
    try:
        with open(path, "a", newline = "") as f:
            writer = csv.writer(f)
            row = csv_string.split(",")
            writer.writerow(row)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return false

#View Data function
def viewData(path):
    print(f"\nDisplaying contents of: {path}\n")
    try:
        with open(path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"Error reading file: {e}")

#Convert data function
def convertData(value, conversion):
    if conversion == "F to C":
        return (value - 32) * 5 / 9

#Get input function
def getInput():
    entries = int(input("How many entries are being entered?"))
    
    for i in range(entries):
        date = input("Enter the date: ")
        value = float(input("Enter the value: "))

        print("1. Temperature (F)")
        print("2. View saved zoo data")

        choice = input("Enter your choice: ")

        if choice == "1":
            conversion = "F to C"
        else:
            conversion = ""
        
        #Calling the convertData function
        convertedValue = convertData(value, conversion)
        print(f"The following was saved at {datetime.now()}:")
        print(f"Date: {date}")
        print(f"Value: {value}")
        print(f"Converted value: {convertedValue}")

if choice == "1":
    getInput()
elif choice == "2":
    viewData("ZooData.csv")
else:
    print("\nError: The chosen functionality is not implemented yet.")

