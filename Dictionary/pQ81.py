"""
costruct a dictionary containing four product names and their prices.
prompt the user to enter a product name. use "in" keyword to check if it exists; 
if so display its price.Otherwise, inform the user "Product not found."
"""
prod = input("Enter a product name: ")
product = {
    "facewash": 550,
    "jacket": 1500,
    "laptop": 150000,
    "watch": 6000
}
if prod in product:
    print(product[prod])
else:
    print("Product not found")
