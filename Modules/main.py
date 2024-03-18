from add import add
from edit import edit_personal_details,payment_details
from view import view_details
from data_filter import view_status_unpaid,view_status_paid,payment_statement
from Modules.calculator import interest_calc

print("Welcome to Personal Loan Management System")
user_input = input("what do you want to do ???\n"
                       "1) Add customer:\n"
                       "2) Edit customer details:\n"
                       "3) View customer details:\n"
                       "4) Generate Reports:\n"
                       "5) Enter Received Payments:\n"
                       "6) Calculate EMI:\n"
                       "Enter Here:")
while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "5" and user_input != "6":
    print("Invalid!, Enter valid Input")
    user_input = input("what do you want to do ???\n"
                           "1) Add customer:\n"
                           "2) Edit customer details:\n"
                           "3) View customer details:\n"
                           "4) Generate Reports:\n"
                           "5) Enter Received Payments:\n"
                           "6) Calculate EMI:\n"
                           "Enter Here:")
if user_input == "1":
    add()
elif user_input == "2":
    edit_personal_details()
elif user_input == "3":
    view_details()

elif user_input == "4":
    u_i = input("1) View Closed Loans:\n"
                "2) View Active Loans:\n"
                "3) View Payment Statement:")
    while u_i != "1" and u_i != "2" and u_i != "3":
        print("Invalid!, Enter valid Input")
        u_i = int(input("1) View Closed Loans:\n"
                        "2) View Active Loans:\n"))
    if u_i == "1":
        view_status_paid()

    elif u_i == "2":
        view_status_unpaid()

    elif u_i == "3":
        payment_statement()

elif user_input == "5":
    payment_details()

elif user_input == "6":
    interest_calc()

