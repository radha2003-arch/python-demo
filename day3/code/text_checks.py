# ----- Indexing and slicing -----
code = "NB-001"

print(code[0])      # N   (first character)
print(code[-1])     # 1   (last character)
print(code[0:2])    # NB  (product type)
print(code[3:])     # 001 (product number)
print(len(code))    # 6   (number of characters)

# ----- Clean text -----
messy_code = "  nb-001 "
print(messy_code.strip())           # "nb-001" (spaces removed)
print(messy_code.upper())           # "  NB-001 " (uppercase)
print(messy_code.strip().upper())   # "NB-001" (clean)

# ----- f-strings -----
product_name = "Notebook"
stock = 25
total = 37.5

print(f"{product_name} has {stock} units in stock.")
print(f"Total: Rs {total:.2f}")     # 2 decimal places

# ----- Comparisons -----
print(stock > 0)             # True
print(stock == 0)            # False
print("NB-001" == "nb-001")  # False (different case)
