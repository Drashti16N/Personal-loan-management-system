import pandas as pd
def view_status_paid():
    data = pd.read_csv("data.csv")

    condition = data["Remaining_amount"] == 0

    d = data.loc[condition, ["Application_number", "Name"]]

    print("These are closed loans")
    print(d)
    ui = input("1. To Download File\n"
                   "Any key For exit:")
    if ui == "1":
        ip = input("Give File Name:")
        d.to_csv(f'Downloaded_Reports/{ip}.csv', index=False)
    else:
        pass

def view_status_unpaid():
    data = pd.read_csv("data.csv")

    condition = data["Remaining_amount"] != 0

    d = data.loc[condition, ["Application_number", "Name", "Remaining_amount"]]

    print("These are Unpaid loans")
    print(d)
    ui = input("1. To Download File\n"
               "Any key For exit:")
    if ui == "1":
        ip = input("Give File Name:")
        d.to_csv(f'Downloaded_Reports/{ip}.csv', index=False)

def payment_statement():
    data = pd.read_csv("data.csv")
    remaining_amount_ = data["Remaining_amount"].tolist()
    remaining_amount = sum(remaining_amount_)

    emi = data["Monthly_emi"].tolist()
    no_of_installments = data["No_of_installments"].tolist()
    total = 0
    for i,j in zip(emi,no_of_installments):
        total += i*j
    a = total-remaining_amount
    print("Total Receivable Amount:",total)
    print("Total Received Amount:",a)
    print("Total Remaining Amount",remaining_amount)


