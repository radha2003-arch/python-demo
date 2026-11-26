# Product details
product_name = "Notebook"
product_code = "NB-001"
stock = 25
low_stock_limit = 5

# Ask for the product code and clean it (remove spaces, make uppercase)
code = input("Enter product code: ").strip().upper()

# Ask for the quantity
quantity = int(input("Enter quantity: "))

print(f"Product code: {code}")

# Check the product code and the requested quantity
if code != product_code:
    print("Product not found.")
elif quantity <= 0:
    print("Quantity must be more than 0.")
elif quantity <= stock:
    print(f"{product_name}: {quantity} units can be ordered.")
else:
    print(f"{product_name}: only {stock} units available.")

# Display the stock status
if stock == 0:
    print("Stock status: Empty")
elif stock <= low_stock_limit:
    print(f"Stock status: Low ({stock} units)")
else:
    print(f"Stock status: Available ({stock} units)")
