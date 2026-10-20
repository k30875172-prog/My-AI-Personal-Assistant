import datetime 

("================================")
print("   MY AI PERSONAL ASSISTANT")
print("================print================")

name = input("Enter your name:")

print("Hello", name, "!")
print("I am your personal assistant.")
print("How can i help you today?")
now = datetime.datetime.now()
print("Current time:",
now.strftime("%I:%M:%p"))
print("Current date:",
datetime.datetime.now().
strftime("%d-%m-%y"))
today = datetime.date.today()
print("Today's date", today)
hour = datetime.datetime.now().hour

if hour < 12:
    print("Good Morning!")
elif hour < 17:
    print("Good Afternoon!")
else:
    print("Good Evening!")

print ("\n=====SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter your second numbner: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose operation (1-4): ")

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
elif choice == "3":
    print("Result:", num1 * num2)
elif choice == "4":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid choice!")
