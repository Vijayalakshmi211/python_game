print("Thank you for choosing Python pizza deliveries!")
size = input("What size pizza do you want to have? s, m, l")
add_pepperoni = input("Do you want extra pepperoni? y or n")
extra_cheese = input("Do you want extra cheese? y or n")
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni =="y":
    if size == "s":
        bill += 2
    else:
        bill += 3
    if extra_cheese == "y":
        bill += 1
    
print(f"Your final bill is :${bill}")