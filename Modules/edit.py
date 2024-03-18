import pandas as pd
data = pd.read_csv("data.csv")

def edit_personal_details():
    an = int(input("Enter Application Number:"))
    ui = input("What do you want to edit:\n"
               "1. Name\n"
               "2. Contact_number\n"
               "3. Email\n"
               "4. Current_address\n"
               "5. Permanent_address\n"
               "6. DOB\n"
               "7. Gender\n"
               "8. No_of_dependents\n"
               "9. Education\n"
               "10. Occupation\n"
               "11. Occupation_address\n"
               "12. Net_income\n"
               "13. No_of_2_wheeler\n"
               "14. No_of_4_wheeler\n"
               "15. Present_liability\n"
               "16. Total_assets\n"
               "17. Total_liability\n"
               "18. Bank Account Details\n"
               "19. Reference_1_Details\n"
               "20. Reference_2_Details\n"
                    "Enter Here:")
    if ui == "1":
        df = pd.read_csv("data.csv")
        index = an - 127000
        name = df.loc[index,"Name"]
        print("Current Name: ",name)
        f_nameu = input("Enter First Name:").strip()
        s_nameu = input("Enter Middle Name:").strip()
        l_nameu = input("Enter Last Name:").strip()
        nameu = f_nameu + " " + s_nameu + " " + l_nameu
        name_u = nameu.title()
        df.loc[index, "Name"] = name_u
        df.to_csv("data.csv",index=False)

    elif ui == "2":
        df = pd.read_csv("data.csv")
        index = an - 127000
        phone_number__ = df.loc[index, "Contact_number"]
        print("Current contact number:",phone_number__)
        phone_number1 = input("Enter Phone number:")
        while not len(phone_number1) == 10 or not phone_number1.isnumeric():
            print("Please enter valid phone number")
            phone_number1 = input("Enter Phone number:")
        df.loc[index,"Contact_number"] = int(phone_number1)
        df.to_csv("data.csv", index=False)

    elif ui == "3":
        df = pd.read_csv("data.csv")
        index = an - 127000
        email__ = df.loc[index,"Email"]
        print("Current Email id:",email__)
        e_mail_id_u = input("Enter email id:")
        while not "@" in e_mail_id_u or not "." in e_mail_id_u:
            print("Invali!, Enter Valid id")
            e_mail_id_u = input("Enter email id:")
        df.loc[index, "Email"] = e_mail_id_u
        df.to_csv("data.csv", index=False)

    elif ui == "4":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index,"Current_address"]
        print("Current Address: ",c_a)
        print ("Enter Current Address")
        street_no_u = input("Flat, House no.:").strip()
        society_u = input("Building, Company, Apartment:").strip()
        area_u = input("Area, Street, Sector village:").strip()
        landmark_u = input("Landmark:").strip()
        city_u = input("City:").strip()
        state_u = input("state:").strip()
        pin_u = input("Pin code:")
        while not pin_u.isnumeric() or not len(pin_u) == 6:
            print("Invalid, please enter valid pin code")
            pin = input("Pin code:")
        current_address_u = street_no_u + ", " + society_u + ", " + area_u + ", " + landmark_u + ", " + city_u + ", " + state_u + ", " + pin_u
        df.loc[index, "Current_address"] = current_address_u
        df.to_csv("data.csv", index=False)

    elif ui == "5":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Permanent_address"]
        print("Current Permanent Address: ", c_a)
        print("Enter Permanent Address")
        street_no_u = input("Flat, House no.:").strip()
        society_u = input("Building, Company, Apartment:").strip()
        area_u = input("Area, Street, Sector village:").strip()
        landmark_u = input("Landmark:").strip()
        city_u = input("City:").strip()
        state_u = input("state:").strip()
        pin_u = input("Pin code:")
        while not pin_u.isnumeric() or not len(pin_u) == 6:
            print("Invalid, please enter valid pin code")
            pin_u = input("Pin code:")
        current_address_u = street_no_u + ", " + society_u + ", " + area_u + ", " + landmark_u + ", " + city_u + ", " + state_u + ", " + pin_u
        df.loc[index, "Current_address"] = current_address_u
        df.to_csv("data.csv", index=False)

    elif ui == "6":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "DOB"]
        print("Current DOB:",c_a)
        dob_u = input("Enter date of birth(dd/mm/yyyy):")
        while not dob_u[0:2].isnumeric() or dob_u[2] != "/" or not dob_u[3:5].isnumeric() or dob_u[5] != "/" or not dob_u[6:].isnumeric():
            print("Invalid")
            dob_u = input("dob:")
        df.loc[index,"DOB"] = dob_u
        df.to_csv("data.csv", index=False)

    elif ui == "7":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Gender"]
        print("Current Gender:", c_a)
        gender = ""
        gender_ = input("Gender: 1. Male\n2. Female\n3. other\nSelect option:")
        if gender_ == "1":
            gender = "Male"
        elif gender_ == "2":
            gender = "Female"
        else:
            gender = "Other"
        df.loc[index, "Gender"] = gender
        df.to_csv("data.csv", index=False)

    elif ui == "8":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "No_of_dependents"]
        print("Current No_of_dependents:", c_a)
        dependent = int(input("Number of dependents:"))
        df.loc[index,"No_of_dependents"] = int(dependent)
        df.to_csv("data.csv", index=False)

    elif ui == "9":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Education"]
        print("Current Education:", c_a)
        education = input("Education:")
        df.loc[index, "Education"] = education
        df.to_csv("data.csv", index=False)

    elif ui == "10":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Occupation"]
        print("Current Occupation:", c_a)
        c_aa = df.loc[index, "Occupation_address"]
        print("Current Occupation_address:", c_aa)
        # occupation = ""
        occupation_address = ""
        occupation1 = input("1. Self Employed\n2. Salaried\n3. other")
        if occupation1 == "1":
            occupation = "Self Employed"
            df.loc[index, "Occupation"] = occupation
            df.to_csv("data.csv", index=False)
            print("Enter Office address")
            street_no = input("Block/ office no:").strip()
            building = input("Building, Company,:").strip()
            area = input("Area, Street, Sector:").strip()
            landmark = input("Landmark:").strip()
            city = input("City:").strip()
            state = input("state:").strip()
            pin = input("Pin code:").strip()
            while not pin.isnumeric() or not len(pin) == 6:
                print("Invalid, please enter valid pin code")
                pin = input("Pin code:")
            office_address = street_no + ", " + building + ", " + area + ", " + landmark + ", " + city + ", " + state + ", " + pin
            occupation_address = office_address
            df.loc[index, "Occupation_address"] = occupation_address
            df.to_csv("data.csv", index=False)
        elif occupation1 == "2":
            occupation = "Salaried"
            df.loc[index, "Occupation"] = occupation
            df.to_csv("data.csv", index=False)
            print("Enter Company address")
            street_no = input("Block/ office no:").strip()
            building = input("Building, Company,:").strip()
            area = input("Area, Street, Sector:").strip()
            landmark = input("Landmark:").strip()
            city = input("City:").strip()
            state = input("state:").strip()
            pin = input("Pin code:")
            while not pin.isnumeric() or not len(pin) == 6:
                print("Invalid, please enter valid pin code")
                pin = input("Pin code:")
            company_address = street_no + ", " + building + ", " + area + ", " + landmark + ", " + city + ", " + state + ", " + pin
            occupation_address = company_address
            df.loc[index, "Occupation_address"] = occupation_address
            df.to_csv("data.csv", index=False)

        else:
            occupation = "Other"
            df.loc[index, "Occupation"] = occupation
            df.to_csv("data.csv", index=False)
            occupation_address = "Null"
            df.loc[index, "Occupation_address"] = occupation_address
            df.to_csv("data.csv", index=False)

    elif ui == "12":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Net_income"]
        print("Current Net income:", c_a)
        net_income = int(input("Net income:"))
        df.loc[index, "Net_income"] = int(net_income)
        df.to_csv("data.csv", index=False)

    elif ui == "13":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "No_of_2_wheeler"]
        print("Current No_of_2_wheeler:", c_a)
        vehicle_2 = int(input("No. of 2 wheel vehicle:"))
        df.loc[index, "No_of_2_wheeler"] = int(vehicle_2)
        df.to_csv("data.csv", index=False)

    elif ui == "14":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "No_of_4_wheeler"]
        print("Current No_of_4_wheeler:", c_a)
        vehicle_4 = int(input("No. of 4 wheel vehicle:"))
        df.loc[index, "No_of_4_wheeler"] = int(vehicle_4)
        df.to_csv("data.csv", index=False)

    elif ui == "15":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Present_liability"]
        print("Current Present_liability:", c_a)
        present_liability = int(input("Present Liability:"))
        df.loc[index, "Present_liability"] = int(present_liability)
        df.to_csv("data.csv", index=False)

    elif ui == "16":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Total_assets"]
        print("Current Total_assets:", c_a)
        property = int(input("Properties (other than House (Rs):"))
        others = int(input(
            "Bank/Post Office Deposits, NSC's, LIC Policy, Gold, Shares, Debentures, Units of UTI /Mutual Funds: "))
        others_1 = int(input("Other Properties:"))
        total_assets = property + others + others_1
        print("Total Assets =", total_assets)
        df.loc[index, "Present_liability"] = int(total_assets)
        df.to_csv("data.csv", index=False)

    elif ui == "17":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Total_liability"]
        print("Current Total_liability:", c_a)
        print("Enter Your Liabilities")
        frnds = int(input("Friends and Relatives: Rs:"))
        banks = int(input("Banks:"))
        other_2 = int(input("Others:"))
        total_liabilities = frnds + banks + other_2
        print("Total Liabilities = ", total_liabilities)
        df.loc[index, "Present_liability"] = int(total_liabilities)
        df.to_csv("data.csv", index=False)

    elif ui == "18":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Account_number"]
        print("Current Account Number:", c_a)
        c_a1 = df.loc[index,"ifsc_code"]
        print("Current IFSC Code:", c_a1)
        c_a2 = df.loc[index,"Type_of_account"]
        print("Current Type of Account:",c_a2)
        c_a3 = df.loc[index,"Year_of_opening"]
        print("Current Year of Opening:", c_a3)
        account_number = input("Account Number:")
        IFSC_code = input("IFSC Code:")
        type_of_account = input("Type of Account")
        year_of_opening = input("Account Opening Date:")
        df.loc[index, "Account_number"] = int(account_number)
        df.to_csv("data.csv", index=False)
        df.loc[index, "ifsc_code"] = IFSC_code
        df.to_csv("data.csv", index=False)
        df.loc[index, "Year_of_opening"] = type_of_account
        df.to_csv("data.csv", index=False)
        df.loc[index, "Year_of_opening"] = int(year_of_opening)
        df.to_csv("data.csv", index=False)

    elif ui == "19":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Reference_1_name"]
        c_a1 = df.loc[index, "Reference_1_number"]
        c_a2 = df.loc[index, "Reference_1_address"]
        print("Current Reference 1 Name:", c_a)
        print("Current Reference 1 Number:", c_a1)
        print("Current Reference 1 Address:", c_a2)

        print("Enter First Person Details")
        f1_name = input("First Name:").strip()
        l1_name = input("Last Name:").strip()
        name1 = f1_name + " " + l1_name

        mo_number1 = input("Enter Mobile no:")
        while not len(mo_number1) == 10 or not mo_number1.isnumeric():
            print("Please enter valid phone number")
            mo_number1 = input("Enter Phone number:")

        print("Enter Address")
        street_no1 = input("Flat, House no.:").strip()
        society1 = input("Building, Company, Apartment:").strip()
        area1 = input("Area, Street, Sector village:").strip()
        landmark1 = input("Landmark:").strip()
        city1 = input("City:").strip()
        state1 = input("state:").strip()
        pin1 = input("Pin code:").strip()
        while not pin1.isnumeric() or not len(pin1) == 6:
            print("Invalid, please enter valid pin code")
            pin1 = input("Pin code:")
        permanent_address1 = street_no1 + ", " + society1 + ", " + area1 + ", " + landmark1 + ", " + city1 + ", " + state1 + ", " + pin1

        df.loc[index, "Reference_1_name"] = name1
        df.to_csv("data.csv", index=False)
        df.loc[index, "Reference_1_number"] = int(mo_number1)
        df.to_csv("data.csv", index=False)
        df.loc[index, "Reference_1_address"] = permanent_address1
        df.to_csv("data.csv", index=False)

    elif ui == "20":
        df = pd.read_csv("data.csv")
        index = an - 127000
        c_a = df.loc[index, "Reference_2_name"]
        c_a1 = df.loc[index, "Reference_2_number"]
        c_a2 = df.loc[index, "Reference_2_address"]
        print("Current Reference 2 Name:", c_a)
        print("Current Reference 2 Number:", c_a1)
        print("Current Reference 2 Address:", c_a2)

        print("Enter Second Person Details")
        f1_name = input("First Name:").strip()
        l1_name = input("Last Name:").strip()
        name1 = f1_name + " " + l1_name

        mo_number1 = input("Enter Mobile no:")
        while not len(mo_number1) == 10 or not mo_number1.isnumeric():
            print("Please enter valid phone number")
            mo_number1 = input("Enter Phone number:")

        print("Enter Address")
        street_no1 = input("Flat, House no.:").strip()
        society1 = input("Building, Company, Apartment:").strip()
        area1 = input("Area, Street, Sector village:").strip()
        landmark1 = input("Landmark:").strip()
        city1 = input("City:").strip()
        state1 = input("state:").strip()
        pin1 = input("Pin code:").strip()
        while not pin1.isnumeric() or not len(pin1) == 6:
            print("Invalid, please enter valid pin code")
            pin1 = input("Pin code:")
        permanent_address1 = street_no1 + ", " + society1 + ", " + area1 + ", " + landmark1 + ", " + city1 + ", " + state1 + ", " + pin1

        df.loc[index, "Reference_2_name"] = name1
        df.to_csv("data.csv", index=False)
        df.loc[index, "Reference_2_number"] = int(mo_number1)
        df.to_csv("data.csv", index=False)
        df.loc[index, "Reference_2_address"] = permanent_address1
        df.to_csv("data.csv", index=False)

def payment_details():
    data = pd.read_csv("data.csv")
    selected_columns = ["Application_number", "Name"]
    selected_data = data[selected_columns]
    print("Customer List")
    print(selected_data)
    an = int(input("Enter Application Number:"))
    df = pd.read_csv("data.csv")
    index = an - 127000
    py = df.loc[index,"Remaining_amount"]
    emi = df.loc[index,"Monthly_emi"]
    print("Current Remaining Amount to Pay:",py)
    print("Monthly EMI:",emi)
    a = int(input("Received Amount:"))
    df.loc[index, "Remaining_amount"] = df.loc[index,"Remaining_amount"] - a
    df.to_csv("data.csv", index=False)
    py1 = df.loc[index, "Remaining_amount"]
    print("Current Remaining Amount to Pay:", py1)