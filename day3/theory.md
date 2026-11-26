# Day 3: Clean Text and Make Decisions

## Today's Topics

1. What are we building today?
2. Read parts of a string: indexing and slicing
3. Clean text: remove extra spaces, uppercase, and lowercase
4. Build readable messages with f-strings
5. Compare values
6. Make decisions with `if`, `elif`, and `else`
7. Combine conditions with `and`, `or`, and `not`
8. Important terms

---

## 1. What Are We Building Today?

**Project:** Inventory and Order Management System for a small store.

Users don't always type neatly. A product code may be typed as `"  nb-001 "` instead of `"NB-001"`.

Today, our program will:
1. **Clean** the product code the user types.
2. **Check** the quantity the customer wants.
3. **Display** whether stock is **available**, **low**, or **empty**.

---

## 2. Read Parts of a String: Indexing and Slicing

A **string** is a sequence of characters. Each character has a **position number**, called an **index**.

> ⚠️ Python starts counting from **0**, not 1.

```
 Text:    N   B   -   0   0   1
 Index:   0   1   2   3   4   5
```

### Indexing: Get One Character

```python
code = "NB-001"

print(code[0])     # N   (first character)
print(code[1])     # B
print(code[-1])    # 1   (last character)
```

- `[0]` → the **first** character
- `[-1]` → the **last** character

### Slicing: Get a Part of the String

**Format:** `text[start:end]` → from `start` up to, but **not including**, `end`.

```python
code = "NB-001"

print(code[0:2])   # NB    (positions 0 and 1)
print(code[3:6])   # 001   (positions 3, 4, 5)
print(code[:2])    # NB    (from the start)
print(code[3:])    # 001   (to the end)
```

> **Store example:** `NB` tells us the product type (Notebook), and `001` is its number.

### Length of a String

```python
print(len("NB-001"))   # 6
```

---

## 3. Clean Text

| Method | What it does | Example | Result |
|---|---|---|---|
| `.strip()` | Removes extra spaces from the start and end | `"  NB-001 ".strip()` | `"NB-001"` |
| `.upper()` | Changes to UPPERCASE | `"nb-001".upper()` | `"NB-001"` |
| `.lower()` | Changes to lowercase | `"NB-001".lower()` | `"nb-001"` |

### Clean a Product Code

```python
code = "  nb-001 "             # messy input
clean_code = code.strip().upper()
print(clean_code)              # NB-001
```

> **Why?** `"nb-001"` and `"NB-001"` look the same to us, but **different** to Python.
> Cleaning makes sure the same product is always found.

---

## 4. Build Readable Messages with f-strings

An **f-string** lets us put **variables inside text** easily.

- Put **`f`** before the quotes.
- Put variables inside **`{ }`**.

```python
product_name = "Notebook"
stock = 25

print(f"{product_name} has {stock} units in stock.")
```

**Output:**
```
Notebook has 25 units in stock.
```

### Compare: Without and With f-string

```python
print("Product:", product_name, "Stock:", stock)   # without f-string
print(f"Product: {product_name}, Stock: {stock}")  # with f-string ✅ easier to read
```

### Show a Price with 2 Decimal Places

```python
total = 37.5
print(f"Total: Rs {total:.2f}")    # Total: Rs 37.50
```

> `:.2f` means **show 2 digits after the decimal point**.

---

## 5. Compare Values

**Comparison operators** compare two values. The answer is always **`True`** or **`False`**.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `3 <= 5` | `True` |

> ⚠️ `=` **stores** a value. `==` **compares** two values.

```python
stock = 25
print(stock > 0)            # True
print("NB-001" == "nb-001") # False (different case)
```

---

## 6. Make Decisions with `if`, `elif`, and `else`

**`if`** lets the program **choose what to do** based on a condition.

```python
stock = 25

if stock > 0:
    print("In stock")
else:
    print("Out of stock")
```

| Keyword | Meaning |
|---|---|
| `if` | If this is **True**, do this |
| `elif` | Else, if **this** is True, do this (check another condition) |
| `else` | If **nothing** above is True, do this |

### Important Rules

- Put a **colon `:`** at the end of the `if`, `elif`, and `else` lines.
- The code inside must be **indented** (4 spaces).

### Stock Status Example

```python
stock = 3

if stock == 0:
    print("Empty")
elif stock <= 5:
    print("Low stock")
else:
    print("Available")
```

**Output:**
```
Low stock
```

> Python checks from **top to bottom** and runs **only the first** condition that is True.

---

## 7. Combine Conditions with `and`, `or`, and `not`

| Keyword | Meaning | True when... |
|---|---|---|
| `and` | Both must be true | **Both** conditions are True |
| `or` | At least one must be true | **Any one** condition is True |
| `not` | Opposite | Turns True into False, and False into True |

### Examples

```python
stock = 25
quantity = 3

# and: quantity must be more than 0 AND not more than stock
if quantity > 0 and quantity <= stock:
    print("Order can be placed")

# or: show a warning if stock is empty OR very low
if stock == 0 or stock < 5:
    print("Please order more stock")

# not: opposite
is_available = True
if not is_available:
    print("Product not available")
```

---

## 8. Important Terms

| Term | Simple Meaning |
|---|---|
| **Index** | The position number of a character (starts at 0) |
| **Indexing** | Getting one character, like `code[0]` |
| **Slicing** | Getting a part of a string, like `code[0:2]` |
| **`len()`** | Gives the number of characters |
| **`.strip()`** | Removes extra spaces from the start and end |
| **`.upper()` / `.lower()`** | Change text to UPPERCASE / lowercase |
| **f-string** | Text with variables inside `{ }`, like `f"Stock: {stock}"` |
| **Comparison operator** | Compares values: `==`, `!=`, `>`, `<`, `>=`, `<=` |
| **Condition** | Something that is True or False |
| **`if` / `elif` / `else`** | Choose what to do based on conditions |
| **Indentation** | Spaces at the start of a line that show which code is inside `if` |
| **`and` / `or` / `not`** | Combine or reverse conditions |

---

## Today's Hands-On

Create a program that:
1. **Cleans** a product code typed by the user.
2. **Checks** the requested quantity.
3. **Displays** whether stock is **available**, **low**, or **empty**.

Example output:
```
Enter product code:   nb-001
Enter quantity: 3
Product code: NB-001
Notebook: 3 units can be ordered.
Stock status: Available (25 units)
```

## Today's Git Task

Commit and push:
- ✅ The text checks
- ✅ The stock messages

```bash
git add .
git commit -m "Add text checks and stock messages"
git push
```

---

## Day 3 Summary

- **Indexing** gets one character; **slicing** gets a part of a string. Counting starts at **0**.
- `.strip()`, `.upper()`, and `.lower()` **clean** text.
- **f-strings** put variables inside text: `f"Stock: {stock}"`.
- **Comparison operators** give `True` or `False`.
- `if`, `elif`, and `else` let the program **make decisions**.
- `and`, `or`, and `not` **combine** conditions.
