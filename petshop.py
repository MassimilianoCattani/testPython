# Shopping cart.

# We have an item list from where the user can select a specific item.
# We are going to build a program able to create user list, to sum up a total but, as well, able to subtract value from total and removing item from user list.

"""
Pseudo code.

- Create a variable list of available items.
- Declare variables:
    - A user cart list just for display.
    - A user cart name list to deal with names.
    - A user cart price list to deal with prices.
    - Initialise total var to 0.
    - Initialize boolean flag and set to False.
    
- Display Shop name.
- Display list of action (1: add item, 2: remove item, 3: check cart and total, 4: checkout).
- User input action variable to select one of the displayed actions. 

- Start loop. We can exit the loop only if boolean flag change to True. 

    - if user input == 1:
    
        - Display list of available items with related ids.
        - User input item selection via id( only 1 per time).
        - Format user input item and append it to user cart list.
        - Name and price get appended to the respective cart list at the same subscript.
        - Update total.
        
        - Display list of action (1: add item, 2: remove item, 3: check cart and total, 4: checkout).
        - User input action variable to select one of the displayed actions. 
        
    - Else if user input == 2
    
        - Display user cart list with re-assigned ids.
        - Input user, item to remove.
        - Update cart list.
        - Update total.
        
        - Display list of action (1: add item, 2: remove item, 3: check cart and total, 4: checkout).
        - User input action variable to select one of the displayed actions. 
        
    - Else if user input == 3:

        - Display cart list and total.
        
        - Display list of action (1: add item, 2: remove item, 3: check cart and total, 4: checkout).
        - User input action variable to select one of the displayed actions. 
    
    - Else if user input == 4:
    
        - Display "Checkout"
        - Display cart list and total.
        - flag = True
        
        
        
    
"""

# Dictionary to hold the item key value pairs.
item_arr = {
    "collar" : {
        "id" : 1, 
        "name" : "Dog collar",
        "price": 15
    },
    "dog_bed" : {
        "id" : 2, 
        "name" : "Dog bed",
        "price" : 50
    },
    "dog_food" : {
        "id" : 3, 
        "name" : "Doggy food",
        "price" : 7
    },
    "cat_bed" : {
        "id" : 4, 
        "name" : "Cat bed",
        "price" : 45
    },
    "cat_food" : {
        "id" : 5, 
        "name" :"Katty food",
        "price" : 7
    },
    "shampoo" : {
        "id" : 6, 
        "name" : "Pet shampoo",
        "price" : 15
    },
    "brushes" : {
        "id" : 7,
        "name" : "Pet brushes",
        "price" : 12
    }
}
user_cart =[]
user_cart_names = []
user_cart_prices = []
total = 0

print("-----------------------------------------------------------------------------------------")
print("Welcome to Paws n Cart")
print("-----------------------------------------------------------------------------------------")

flag = False
print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
user_action_sele = int(input("---> Enter number of the option you want to select: "))

while flag == False:

    if user_action_sele == 1:
        
        print("Select from our products:")
        
        for i in item_arr:
            print(f"Item: {item_arr[i]['id']}\t {item_arr[i]['name'].ljust(15)}: £ {item_arr[i]['price']}")

        user_item_sele = int(input("---> Select number of desired item: "))
        
        for ele in item_arr:
            if item_arr[ele]["id"] == user_item_sele:
                user_item = f". {item_arr[ele]['name'].ljust(20)}: £ {item_arr[ele]['price']}"
                user_cart.append(user_item)
                user_cart_names.append(item_arr[ele]["name"])     
                user_cart_prices.append(item_arr[ele]["price"]) 
                total += item_arr[ele]["price"]
        
        print("-----------------------------------------------------------------------------------------")
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: "))  
        print("=========================================================================================") 
            
    elif user_action_sele == 2:

        num_id_item = 0     # These var work only within this elif statement. 
        arr_ids = []

        for item in user_cart:
            num_id_item += 1
            arr_ids.append(num_id_item)
            print(f"{num_id_item} {item}") 
            
        user_remove = int(input("---> Enter the number of the item you want to remove: "))
       
        for checker in range(len(arr_ids)):
            if user_remove == arr_ids[checker]:
                user_cart.remove(user_cart[user_remove - 1])
                total = total - user_cart_prices[user_remove - 1]
                user_cart_prices.remove(user_cart_prices[user_remove - 1])
    
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: "))   
        print("=========================================================================================")  
            
    elif user_action_sele == 3:
        
        print("Cart list:")

        for counter in user_cart:
            print(counter)
            
        print("-----------------------------------------------------------------------------------------")
        print("Total".ljust(22)+": £", total) 
        print("-----------------------------------------------------------------------------------------")
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: ")) 
        print("=========================================================================================")  
           
    elif user_action_sele == 4:
        
        print("Checkout:")

        for j in user_cart:
            print(j)
        
        flag = True
        print("-----------------------------------------------------------------------------------------")
        print("Total".ljust(22)+": £", total) 
        print("-----------------------------------------------------------------------------------------")
        print("=========================================================================================")  
        
    else:
        print('Please, insert correct digit')
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: ")) 
        print("=========================================================================================")     