import datetime
import os

FILE_NAME = "my_expenses.txt"

def show_menu():
    print("\n--- SMART BILL SPLITTER & TRACKER ---")
    print("1. Split a Bill (with friends)")
    print("2. Add a Personal Expense (just for me)")
    print("3. View My Expense History")
    print("4. Exit")
    print("-------------------------------------------")

def save_to_file(desc, amount):
    today = datetime.date.today()
    
    # FIX: Added encoding="utf-8" to handle the Rupee symbol (₹)
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{today} | {desc} | ₹{amount}\n")
    
    print(f"--> Saved '₹{amount}' for '{desc}' to your history!")

def view_history():
    print("\n--- MY EXPENSE HISTORY ---")
    
    if not os.path.exists(FILE_NAME):
        print("No history found yet! Go spend some money first.")
        return

    # FIX: Added encoding="utf-8" to read the symbol correctly
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        content = f.read()
        if content == "":
            print("File is empty.")
        else:
            print(content)

def split_bill():
    print("\n--- BILL SPLITTER ---")
    
    total_bill = float(input("Enter the total bill amount: ₹"))
    tip_percent = float(input("Enter tip/tax percentage (e.g. 5 for 5%): "))
    
    total_with_tip = total_bill + (total_bill * (tip_percent / 100))
    print(f"Total to pay (including {tip_percent}% tax/tip): ₹{total_with_tip:.2f}")

    num_people = int(input("How many people are splitting? "))
    
    print("\nHow do you want to split?")
    print("1. Equally (Everyone pays the same)")
    print("2. By Item (Everyone pays for what they ate)")
    choice = input("Enter choice (1 or 2): ")

    my_share = 0

    if choice == '1':
        share = total_with_tip / num_people
        print(f"\nEveryone needs to pay: ₹{share:.2f}")
        my_share = share

    elif choice == '2':
        print("\n--- Enter amount for each person (before tax) ---")
        current_total = 0
        
        for i in range(num_people):
            person_amt = float(input(f"Person {i+1} amount: ₹"))
            person_final = person_amt + (person_amt * (tip_percent / 100))
            print(f"   -> Person {i+1} owes: ₹{person_final:.2f}")
            
            if i == 0:
                my_share = person_final
            
            current_total += person_final
        
        print(f"\n(Check: Total collected is ₹{current_total:.2f})")

    else:
        print("Invalid choice! Taking you back to menu...")
        return

    print(f"\nYour share is: ₹{my_share:.2f}")
    save_ask = input("Do you want to save YOUR share to your personal expenses? (y/n): ")
    
    if save_ask.lower() == 'y':
        desc = input("Enter a note for this (e.g. 'Pizza with Rahul'): ")
        save_to_file(desc, my_share)

def add_personal_expense():
    print("\n--- ADD PERSONAL EXPENSE ---")
    desc = input("What did you buy? (e.g. Bus Ticket): ")
    amt = float(input("How much was it? ₹"))
    save_to_file(desc, amt)

while True:
    show_menu()
    user_choice = input("Choose an option (1-4): ")

    if user_choice == '1':
        split_bill()
    elif user_choice == '2':
        add_personal_expense()
    elif user_choice == '3':
        view_history()
    elif user_choice == '4':
        print("\nSee ya later!")
        break
    else:
        print("Oops! Please type 1, 2, 3, or 4.")