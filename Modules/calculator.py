def interest_calc():
    loan_amount = int(input("Loan amount:"))
    interest_rate = int(input("Interest rate:"))
    yearly_tenure = float(input("Proposed Yearly repayment:"))

    monthly_interest_rate = interest_rate / 12 / 100

    # Calculate the number of monthly installments
    num_installments = yearly_tenure * 12

    # Calculate EMI using the formula
    emi = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** num_installments
    emi /= ((1 + monthly_interest_rate) ** num_installments - 1)
    emi = round(emi)
    repayment_amount = emi*num_installments
    print("Principal Amount =", loan_amount)
    print("Interest Rate =", interest_rate)
    print("Tenure =",num_installments,"Months")
    print("Monthly EMI =", emi)
    print("Total Repayable Amount =", repayment_amount)