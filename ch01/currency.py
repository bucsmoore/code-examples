amount = input("Enter amount to exchange: ")
rate = input("Enter rate: ")

amount = float(amount)
rate = float(rate)

# amount = float(input("Enter amount to exchange: "))
# rate = float(input("Enter rate: "))

total = amount * rate
customer_total = total - 3
print("Your total is:", round(customer_total, 2))
