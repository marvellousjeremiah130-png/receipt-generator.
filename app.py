#Supermarket receipt program:
Items = {
    "soap": 500,
    "cream": 500,
    "perfume": 400,
    "pads": 550,
    "oats": 5000,
    "cookies": 600
}
cart = [] # things added to cart


total = 0 #for total 

#To display items
print("__Available items__")
for key, value in Items.items():
    print(f"{key:10}: #{value:.2f}")
print("_____________________")

while True:
    choice = input("Choose item(q to quit):  ").lower()
    
    if choice == "q":
        break # escape while loop.
        
    elif Items.get(choice) is not None:
        cart.append(choice)


for choice in cart:
    price = Items.get(choice)
    total += price
    print(f"{choice:10} : {price}")
    
print("______total_______")

print(f"Total : {total:10}")

    
