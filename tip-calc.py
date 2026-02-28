print("what is life")
#total bill =150
#how much would each like to pay  10,12,15 = 12
#how many people to split the bill 5
#each person should pay 33.6

print("welcome to tip calculator")
bill=float(input("what is total bill"))
tip=float(input("what is tip"))
people=int(input("How many people?"))
tip_as_percent=tip/100
total_bill=bill+tip_as_percent
bill_per_person=total_bill/people
final_amount= round(bill_per_person,2)
print(f"each person should pay :Ruppes{final_amount}")
