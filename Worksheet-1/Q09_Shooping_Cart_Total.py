def calculate_total(prices, discount_percent=0):
    subtotal = sum(prices)
    discount_amount = (subtotal * discount_percent) / 100
    final_total = subtotal - discount_amount
    return {"subtotal": subtotal,"discount_amount": discount_amount,"final_total": final_total}

n = int(input("Enter size of list: "))
prices = []
for i in range(n):
    prices.append(int(input("Enter price: ")))
discount = float(input("Enter discount percentage: "))
print(calculate_total(prices, discount))
