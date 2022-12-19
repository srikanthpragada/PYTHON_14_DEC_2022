
qty = int(input("Enter qty : "))
price = int(input("Enter price : "))

amount = qty * price
if qty > 3:
    discount = amount * 0.30
elif qty > 2:
    discount = amount * 0.20
else:
    discount = amount * 0.10

net_amount = amount - discount
if net_amount > 10000:
    net_amount *= 0.90   # 10 % discount

print('Net Amount ', net_amount)

