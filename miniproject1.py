student_name = input("enter a name: ")
monthly_income = float(input("enter monthly income: "))
food_expense = float(input("enter food expense:"))
travell_expense = float(input("enter travell expence:"))
study_material = float(input("enter study material:"))
mobile_internet_expense = int(input("enter mobile expense:"))
other_expense = float(input("enter the other expanses:"))
total_expense = monthly_income+food_expense+travell_expense+study_material+mobile_internet_expense+other_expense
remaining_balance = monthly_income-total_expense

 
print(f"------MONTHLY BUDGET REPORT-------")
print("student name =",student_name)
print("monthly income is = ",monthly_income)
print("food expense is = ",food_expense)
print("travell expense is = ",travell_expense)
print("study material is = ",study_material)
print("mobile internet expense is = ",mobile_internet_expense)
print("other expense is = ",other_expense)
print("the total Expense is:", total_expense )
print("Remaining balance is" , remaining_balance)
if monthly_income>0: 
    saving_rate = (remaining_balance / monthly_income)*100
    print("The saving rate is:", saving_rate)
else:
    print("your monthly income is zero, pls enter write monthly income")