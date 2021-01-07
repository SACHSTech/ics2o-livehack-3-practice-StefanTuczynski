"""
Name: practice1.py
Purpose: To convert the Canadian dollar - US dollar exchange rate on certain varibles
of numbers. 

Author: Tuczynski.S 

Date: 6/1/2021
"""

#inputs user data given to the system
exchange_rate = float(input("What is the Canadian to US dollar exhange rate? "))
starting_value = int(input("Enter the starting value: "))
end_value = int(input("Enter the end value: "))

#tells user what the conversion rate is and uses an example
print("Using the conversion rate, 1 Canadian dollar equals",1 * exchange_rate,"US dollars")

#computes the user data into a for loop
for ca_dollars in range (starting_value, end_value+1, 10):
  us_dollars = ca_dollars * exchange_rate
  print(ca_dollars,"Canadian dollars equals",us_dollars,"US dollars")
  
