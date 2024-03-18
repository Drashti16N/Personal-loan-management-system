import pandas as pd
data = pd.read_csv("data.csv")
def add():
    last_application_number = data["Application_number"].iloc[-1]
    id = last_application_number + 1
    print("Application number:", id)

    # NAME
    f_name = input("Enter First Name:").replace(" ", "")
    s_name = input("Enter Middle Name:").replace(" ", "")
    l_name = input("Enter Last Name:").replace(" ", "")
    name = f_name + " " + s_name + " " + l_name
    name_t = name.title()


    # PHONE NUMBER
    phone_number = input("Enter Phone number:")
    while not len(phone_number) == 10 or not phone_number.isnumeric():
        print("Please enter valid phone number")
        phone_number = input("Enter Phone number:")


    # E MAIL
    e_mail_id = input("Enter email id:").replace(" ", "").lower()
    while not "@" in e_mail_id or not "." in e_mail_id:
        print("Invali!, Enter Valid id")
        e_mail_id = input("Enter email id:")


    # ADDRESS
    print("Enter Current Address")
    street_no = input("Flat, House no.:").strip()
    society = input("Building, Company, Apartment:").strip()
    area = input("Area, Street, Sector village:").replace(" ", "")
    landmark = input("Landmark:").strip()
    city = input("City:").replace(" ", "")
    state = input("state:").replace(" ", "")
    pin = input("Pin code:")
    while not pin.isnumeric() or not len(pin) == 6:
        print("Invalid, please enter valid pin code")
        pin = input("Pin code:")
    current_address = street_no + ", " + society + ", " + area + ", " + landmark + ", " + city + ", " + state + ", " + pin


    permanent_address = ""
    print("Permanent Address")
    a = input("1. same as current address\n 2. add new address\nSelect option:")
    if a == "1":
        permanent_address = current_address

    elif a == "2":
        print("Enter Permanent Address")
        street_no1 = input("Flat, House no.:").strip()
        society1 = input("Building, Company, Apartment:").strip()
        area1 = input("Area, Street, Sector village:").replace(" ", "")
        landmark1 = input("Landmark:").strip()
        city1 = input("City:").replace(" ", "")
        state1 = input("state:").replace(" ", "")
        pin1 = input("Pin code:")
        while not pin.isnumeric() or not len(pin) == 6:
            print("Invalid, please enter valid pin code")
            pin = input("Pin code:")
        permanent_address = street_no1 + ", " + society1 + ", " + area1 + ", " + landmark1 + ", " + city1 + ", " + state1 + ", " + pin1


    # DOB

    dob = input("Enter date of birth(dd/mm/yyyy):")
    while not dob[0:2].isnumeric() or dob[2] != "/" or not dob[3:5].isnumeric() or dob[5] != "/" or not dob[
                                                                                                        6:].isnumeric():
        print("Invalid")
        dob = input("dob:")


    # Gender
    gender = ""
    gender_ = input("Gender: 1. Male\n2. Female\n3. other\nSelect option:")
    if gender_ == "1":

        gender = "Male"
    elif gender_ == "2":

        gender = "Female"
    else:

        gender = "Other"

    # NUMBER OF DEPENDENTS
    dependent = int(input("Number of dependents:"))


    # Education
    education = input("Education:")


    # Occupation Details
    occupation = ""
    occupation_address = ""
    occupation1 = input("1. Self Employed\n2. Salaried\n3. other")
    if occupation1 == "1":

        occupation = "Self Employed"
        print("Enter Office address")
        street_no = input("Block/ office no:").strip()
        building = input("Building, Company,:").strip()
        area = input("Area, Street, Sector:").replace(" ", "")
        landmark = input("Landmark:").strip()
        city = input("City:").replace(" ", "")
        state = input("state:").replace(" ", "")
        pin = input("Pin code:").strip()
        while not pin.isnumeric() or not len(pin) == 6:
            print("Invalid, please enter valid pin code")
            pin = input("Pin code:")
        office_address = street_no + ", " + building + ", " + area + ", " + landmark + ", " + city + ", " + state + ", " + pin
        occupation_address = office_address

    elif occupation1 == "2":

        occupation = "Salaried"
        print("Enter Company address")
        street_no = input("Block/ office no:").strip()
        building = input("Building, Company,:").strip()
        area = input("Area, Street, Sector:").replace(" ", "")
        landmark = input("Landmark:").strip()
        city = input("City:").replace(" ", "")
        state = input("state:").replace(" ", "")
        pin = input("Pin code:")
        while not pin.isnumeric() or not len(pin) == 6:
            print("Invalid, please enter valid pin code")
            pin = input("Pin code:")
        company_address = street_no + ", " + building + ", " + area + ", " + landmark + ", " + city + ", " + state + ", " + pin
        occupation_address = company_address

    else:

        occupation = "Other"

        occupation_address = "Null"

    # MONTHLY/ANNUAL INCOME
    net_income = input("Net income:")
    while not net_income.isnumeric():
        print("Invalid, please enter Income in numeric form")
        net_income = int(net_income)

    # Vehicle
    vehicle_2 = input("Enter no. of 2 wheel vehicle:")
    while not vehicle_2.isnumeric():
        print("Invalid, please enter Number of Vehicle in numeric form")
        vehicle_2 = input("Enter no. of 2 wheel vehicle:")
    vehicle_4 = input("Enter no. of 4 wheel vehicle:")
    while not vehicle_4.isnumeric():
        print("Invalid, please enter Number of Vehicle in numeric form")
        vehicle_4 = input("Enter no. of 4 wheel vehicle:")


    # Present Liability
    present_liability = input("Present Liability:")
    while not present_liability.isnumeric():
        print("Invalid, please enter Liabilities in numeric form")
    present_liability = int(present_liability)


    # Other Assets owned by : Self

    property = input("Properties (other than House (Rs):")
    while not property.isnumeric():
        print("Invalid, please enter properties in numeric form")
        property = input("Properties (other than House (Rs):")
    others = input(
        "Bank/Post Office Deposits, NSC's, LIC Policy, Gold, Shares, Debentures, Units of UTI /Mutual Funds: ")
    while not others.isnumeric():
        print("Invalid, please enter properties in numeric form")
        others = input("Properties (other than House (Rs):")
    others_1 = input("Other Properties:")
    while not others_1.isnumeric():
        print("Invalid, please enter properties in numeric form")
        others_1 = input("Properties (other than House (Rs):")
    property = int(property)
    others = int(others)
    others_1 = int(others_1)
    total_assets = property + others + others_1
    print("Total Assets =", total_assets)

    # Other Liabilities in Brief:
    print("Enter Your Liabilities")
    frnds = input("Friends and Relatives: Rs:")
    while not frnds.isnumeric():
        print("Invalid, please enter Liabilities in numeric form")
        frnds = input("Friends and Relatives: Rs:")
    banks = input("Banks:")
    while not banks.isnumeric():
        print("Invalid, please enter Liabilities in numeric form")
        banks = input("Banks:")
    other_2 = input("Others:")
    while not banks.isnumeric():
        print("Invalid, please enter Liabilities in numeric form")
        other_2 = input("Others:")
    frnds = int(frnds)
    banks = int(banks)
    other_2 = int(other_2)
    total_liabilities = frnds + banks + other_2
    print("Total Liabilities = ", total_liabilities)


    # LOAN AMOUNT

    loan_amount = input("Loan amount:")
    while not loan_amount.isnumeric():
        print("Invalid, please enter Loan amount in numeric form")
        loan_amount = input("Loan amount:")
    interest_rate = input("interest rate:")
    while not loan_amount.isnumeric():
        print("Invalid, please enter Interest Rate in numeric form")
        interest_rate = input("interest rate:")
    loan_amount = int(loan_amount)
    interest_rate = int(interest_rate)
    yearly_tenure = float(input("proposed Yearly repayment:"))

    monthly_interest_rate = interest_rate / 12 / 100

    # Calculate the number of monthly installments
    num_installments = yearly_tenure * 12

    # Calculate EMI using the formula
    emi = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** num_installments
    emi /= ((1 + monthly_interest_rate) ** num_installments - 1)
    emi = round(emi)
    repayment_amount = emi * num_installments

    print("Monthly EMI = ", emi)
    print("Total Repayable Amount = ", repayment_amount)

    # Details of Bank Account

    account_number = input("Account Number:")
    while not len(account_number) >= 11 or not account_number.isnumeric() or not len(account_number) <= 17:
        print("Invalid,Please enter valid Account number")
        account_number = input("Account Number:")
    IFSC_code = input("IFSC Code:")
    while not len(IFSC_code) == 11 or not IFSC_code[0:4].isalpha():
        print("Invalid,Please enter valid IFSC Code")
        IFSC_code = input("IFSC Code:")
    IFSC_code = IFSC_code[0:4].upper() + IFSC_code[4:]
    print(IFSC_code)
    type_of_account = input("Type of Account:")
    Date_of_opening = input("Account Opening Date:")
    while not Date_of_opening[0:2].isnumeric() or Date_of_opening[2] != "/" or not Date_of_opening[3:5].isnumeric() or \
            Date_of_opening[5] != "/" or not Date_of_opening[6:].isnumeric():
        print("Invalid, Please enter valid date")
        Date_of_opening = input("Account Opening Date:")


    # Two Personal Reference

    print("Enter First Person Details")
    f1_name = input("First Name:").replace(" ", "")
    l1_name = input("Last Name:").replace(" ", "")
    name1 = f1_name + " " + l1_name


    mo_number1 = input("Enter Mobile no:")
    while not len(mo_number1) == 10 or not mo_number1.isnumeric():
        print("Please enter valid phone number")
        mo_number1 = input("Enter Phone number:")


    print("Enter Address")
    street_no1 = input("Flat, House no.:").strip()
    society1 = input("Building, Company, Apartment:").strip()
    area1 = input("Area, Street, Sector village:").replace(" ", "")
    landmark1 = input("Landmark:").strip()
    city1 = input("City:").replace(" ", "")
    state1 = input("state:").replace(" ", "")
    pin1 = input("Pin code:").strip()
    while not pin1.isnumeric() or not len(pin1) == 6:
        print("Invalid, please enter valid pin code")
        pin = input("Pin code:")
    permanent_address1 = street_no1 + ", " + society1 + ", " + area1 + ", " + landmark1 + ", " + city1 + ", " + state1 + ", " + pin1


    print("Enter Second Person Details")
    f2_name = input("First Name:").replace(" ", "")
    l2_name = input("Last Name:").replace(" ", "")
    name2 = f2_name + " " + l2_name


    mo_number2 = input("Enter Mobile no:")
    while not len(mo_number2) == 10 or not mo_number2.isnumeric():
        print("Please enter valid phone number")
        mo_number2 = input("Enter Phone number:")


    print("Enter Address")
    street_no2 = input("Flat, House no.:").strip()
    society2 = input("Building, Company, Apartment:").strip()
    area2 = input("Area, Street, Sector village:").replace(" ", "")
    landmark2 = input("Landmark:").strip()
    city2 = input("City:").replace(" ", "")
    state2 = input("state:").replace(" ", "")
    pin2 = input("Pin code:")
    while not pin.isnumeric() or not len(pin) == 6:
        print("Invalid, please enter valid pin code")
        pin = input("Pin code:")
    permanent_address2 = street_no2 + ", " + society2 + ", " + area2 + ", " + landmark2 + ", " + city2 + ", " + state2 + ", " + pin2


    # List_of_inputs
    id_ = [id]
    name_ = [name_t]
    phone_number_ = [phone_number]
    e_mail_id_ = [e_mail_id]
    current_address_ = [current_address]
    permanent_address_ = [permanent_address]
    dob_ = [dob]
    gender_ = [gender]
    dependent_ = [dependent]
    education_ = [education]
    occupation_ = [occupation]
    occupation_address_ = [occupation_address]
    net_income_ = [net_income]
    vehicle_2_ = [vehicle_2]
    vehicle_4_ = [vehicle_4]
    present_liability_ = [present_liability]
    total_assets_ = [total_assets]
    total_liabilities_ = [total_liabilities]
    loan_amount_ = [loan_amount]
    interest_rate_ = [interest_rate]
    num_installments_ = [num_installments]
    emi_ = [emi]
    repayment_amount_ = [repayment_amount]
    account_number_ = [account_number]
    IFSC_code_ = [IFSC_code]
    type_of_account_ = [type_of_account]
    year_of_opening_ = [Date_of_opening]
    name1_ = [name1]
    mo_number1_ = [mo_number1]
    permanent_address1_ = [permanent_address1]
    name2_ = [name2]
    mo_number2_ = [mo_number2]
    permanent_address2_ = [permanent_address2]

    # Dictionary of data
    dict_ = {"Application_number": id_,
             "Name": name_,
             "Contact_number": phone_number_,
             "Email": e_mail_id_,
             "Current_address": current_address_,
             "Permanent_address": permanent_address_,
             "DOB": dob_,
             "Gender": gender_,
             "No_of_dependents": dependent_,
             "Education": education_,
             "Occupation": occupation_,
             "Occupation_address": occupation_address_,
             "Net_income": net_income_,
             "No_of_2_wheeler": vehicle_2_,
             "No_of_4_wheeler": vehicle_4_,
             "Present_liability": present_liability_,
             "Total_assets": total_assets_,
             "Total_liability": total_liabilities_,
             "Principal_amount": loan_amount_,
             "Interest_rate": interest_rate_,
             "No_of_installments": num_installments_,
             "Monthly_emi": emi_,
             "Remaining_amount": repayment_amount_,
             "Account_number": account_number_,
             "ifsc_code": IFSC_code_,
             "Type_of_account": type_of_account_,
             "Year_of_opening": year_of_opening_,
             "Reference_1_name": name1_,
             "Reference_1_number": mo_number1_,
             "Reference_1_address": permanent_address1_,
             "Reference_2_name": name2_,
             "Reference_2_number": mo_number2_,
             "Reference_2_address": permanent_address2_,
             }

    df = pd.DataFrame(dict_)
    df.to_csv("data.csv", index=False, header=False, mode="a")