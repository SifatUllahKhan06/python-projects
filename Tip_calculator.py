print("Welcome to the tip calculator!")
Total_bill = input("What was the total bill? $")
No_Of_People = input("Number of People bill will be divided : ")
Final_pay = (float(Total_bill)/int(No_Of_People))*1.15
Final_pay = round(Final_pay,2)
print(f"Each person should pay: {Final_pay}" )
