#while loop

answer = "yes"
total_amount = 0

while answer == "yes" :
    name = input("enter item name")
    qty = int(input("enter item qty"))
    price = float(input("enter item price"))

    item_total = qty * price
    total_amount += item_total

    #answer = input("another item?")
    answer = input("Another item? (yes/no): ")

    print(total_amount)