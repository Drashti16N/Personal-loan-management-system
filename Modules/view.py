import pandas as pd
data = pd.read_csv("data.csv")

def view_details():
    app_no = int(input("Enter Application Number:"))
    view = input("What do you want to view:\n"
                "1. view mini statement\n"
                "2. view detailed information\n")

    if view == "1":
        df = pd.read_csv("data.csv")
        index = app_no - 127000
        name = df.loc[index, "Name"]
        phone_number__ = df.loc[index, "Contact_number"]
        email__ = df.loc[index, "Email"]
        py = df.loc[index, "Remaining_amount"]
        emi = df.loc[index, "Monthly_emi"]
        print("Name:",name,"\nPhone number:",phone_number__,"\nEmail id:", email__,
              "\nRemaining amount to Pay:",py,"\nEMI:",emi)


    elif view == "2":
        df = pd.read_csv("data.csv")
        index = app_no - 127000
        name = df.loc[index, "Name"]
        phone_number__ = df.loc[index, "Contact_number"]
        email__ = df.loc[index, "Email"]
        c_a = df.loc[index, "Current_address"]
        p_a = df.loc[index, "Permanent_address"]
        dob = df.loc[index, "DOB"]
        gender = df.loc[index, "Gender"]
        dependents = df.loc[index, "No_of_dependents"]
        education = df.loc[index, "Education"]
        occupation = df.loc[index, "Occupation"]
        wheeler_2 = df.loc[index, "No_of_2_wheeler"]
        wheeler_4 = df.loc[index, "No_of_4_wheeler"]
        Present_liability = df.loc[index, "Present_liability"]
        Total_assets = df.loc[index, "Total_assets"]
        Total_liability = df.loc[index, "Total_liability"]
        Account_number = df.loc[index, "Account_number"]
        ifsc_code = df.loc[index, "ifsc_code"]
        Type_of_account = df.loc[index, "Type_of_account"]
        date_of_opening = df.loc[index, "Year_of_opening"]
        Reference_1_name = df.loc[index, "Reference_1_name"]
        Reference_1_number = df.loc[index, "Reference_1_number"]
        Reference_1_address = df.loc[index, "Reference_1_address"]
        Reference_2_name = df.loc[index, "Reference_2_name"]
        Reference_2_number = df.loc[index, "Reference_2_number"]
        Reference_2_address = df.loc[index, "Reference_2_address"]
        py = df.loc[index, "Remaining_amount"]
        emi = df.loc[index, "Monthly_emi"]
        print("Name:",name,"\nPhone number:", phone_number__,"\nEmail id:", email__,
              "\nCurrent address:", c_a, "\nPermanent_address:", p_a,"\nDOB:", dob,
              "\nGender:",gender,"\nNo of dependents:",dependents,"\nEducation:",education,
              "\nOccupation:",occupation,"\nNo of 2 wheelers:",wheeler_2,"\nNo of 4 wheelers:",wheeler_4,
              "\nPresent liability:",Present_liability,"\nTotal assets:",Total_assets,"\nTotal liability:",Total_liability,
              "\nAccount number:",Account_number,"\nIFSC code:",ifsc_code,"\nType of account:",Type_of_account,
              "\nDate of opening:",date_of_opening,"\nReference 1 name:",Reference_1_name,
              "\nReference 1 number:",Reference_1_number,"\nReference 1 address:",Reference_1_address,
              "\nReference 2 name:",Reference_2_name,"\nReference 2 number:",Reference_2_number,
              "\nReference 2 address:",Reference_2_address,"\nRemaining amount:",py,"\nEMI:",emi)