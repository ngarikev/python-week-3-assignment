
def calculate_discount(price, discount_percent):
  if discount_percent >= 0.2 :
    print(f"New price: {price - (price * discount_percent)}")

  else: print(f"Original price: {price}")
  
price = int(input("Enter price: "))
discount_percent = float(input("Enter percentage discount: "))

calculate_discount(price, discount_percent)