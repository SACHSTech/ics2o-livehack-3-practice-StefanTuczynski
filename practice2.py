"""
Name: practice2.py
Purpose: To determine whether your import goods are less or above the value amount allowed by the
government, and if you are over, determine how much duty fees you need to pay

Author: Tuczynski.S

Date: 6/1/2021
"""

#predetermined variables
total = 0
days = 0
done = False

#inputs user data and calculates total days spent and total amount
while not done:
  daily_amount = float(input("Enter a daily spent amount (-1 to stop) "))

  if daily_amount == -1:
    done = True
  else:
    total = total + daily_amount
    days = days + 1

#outputs total amount spent and days abroad
print("You have spent a total of $"+str(total),"abroad")
print("You have spent a total of",str(days),"abroad")

#checks if they are above and computes the fees nessisary if above
limit = 250 * days
if total > limit:
  fee = total * 0.13
  print("You owe $"+str(fee))
else:
  print("You do not owe a fee")

