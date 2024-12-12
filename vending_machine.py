

# set-up Item class 
# class holds information pertaining to each items name, price, amount and item code
class Item: 
  def __init__(self, name, price, amount, item_code):
    self.name = name
    self.price = price
    self.amount = amount
    self.item_code = item_code

# this function will be used to display items name and item code to user
  def __repr__(self):  
    return "% s   % s " % (self.item_code, self.name) 


# create items 
lays = Item("Lays", 1.39, 10, "C1")
doritos = Item("Doritos", 1.39, 10, "C2")
pringles = Item("Pringles", 1.39, 10, "C3")
sour_patch = Item("Sour Patch Kids", 2.150, 10, "D1")
snickers = Item("Snickers", 2.15, 10, "D2")
twix = Item("Twix", 2.15, 10, "D3")





# greet user
print("Hello, welcome to Kristy's vending machine!")



#offer selection
print()
print ("Below is our current selection:")
print()
print (lays)
print (doritos)
print (pringles)
print (sour_patch)
print (snickers)
print (twix)


# ask user for their selection
print()
selection = input("Please enter the code for the item you'd like: ")
print()



# take user selection and display price of the item 

if selection == 'C1' or selection == 'c1' :
  print(f"You have selected {lays.name}. Please insert ${lays.price}.")

elif selection == 'C2' or selection == 'c2' :
  print(f"You have selected {doritos.name}. Please insert ${doritos.price}.")

elif selection == 'C3' or selection == 'c3' :
  print(f"You have selected {pringles.name}. Please insert ${pringles.price}.")

elif selection == 'D1' or selection == 'd1' :
  print(f"You have selected {sour_patch.name}. Please insert ${sour_patch.price}.")

elif selection == 'D2' or selection == 'd2' :
  print(f"You have selected {snickers.name}. Please insert ${snickers.price}.")

elif selection == 'D3' or selection == 'd3' :
  print(f"You have selected {twix.name}. Please insert ${twix.price}.")

else: 
  print("Please enter a valid selection." )



#get user input for amount of money they are inserting

amount = float(input("Please enter the amount of money you'd like to insert: $"))




# compare user amount inserted to item price and respond accordingly 

if selection == 'C1' or selection == 'c1' and amount == lays.price :
  print("Thank you for your purchase. Please take your item.")
elif selection == 'C1' or selection == 'c1' and amount > lays.price :
  print("Thank you for your purchase. Please take your item and your change.")
elif selection == 'C1' or selection == 'c1' and amount < lays.price :
  print("You have not inserted enough money. Please insert the correct amount.")

elif selection == 'C2' or selection == 'c2' and amount == doritos.price :
  print("Thank you for your purchase. Please take your item.")  
elif selection == 'C2' or selection == 'c2' and amount > doritos.price : 
  print("Thank you for your purchase. Please take your item and your change.")
elif selection == 'C2' or selection == 'c2' and amount < doritos.price :
  print("You have not inserted enough money. Please insert the correct amount.")

elif selection == 'C3' or selection == 'c3' and amount == pringles.price :
  print("Thank you for your purchase. Please take your item.")
elif selection == 'C3' or selection == 'c3' and amount > pringles.price :
  print("Thank you for your purchase. Please take your item and your change.")
elif selection == 'C3' or selection == 'c3' and amount < pringles.price :
  print("You have not inserted enough money. Please insert the correct amount.")

elif selection == 'D1' or selection == 'd1' and amount == sour_patch.price :
  print("Thank you for your purchase. Please take your item.")
elif selection == 'D1' or selection == 'd1' and amount > sour_patch.price :
  print("Thank you for your purchase. Please take your item and your change.")
elif selection == 'D1' or selection == 'd1' and amount < sour_patch.price :
  print("You have not inserted enough money. Please insert the correct amount.")

elif selection == 'D2' or selection == 'd2' and amount == snickers.price :
  print("Thank you for your purchase. Please take your item.")
elif selection == 'D2' or selection == 'd2' and amount > snickers.price :
  print("Thank you for your purchase. Please take your item and your change.")
elif selection == 'D2' or selection == 'd2' and amount < snickers.price :
  print("You have not inserted enough money. Please insert the correct amount.")

elif selection == 'D3' or selection == 'd3' and amount == twix.price :
  print("Thank you for your purchase. Please take your item.")
elif selection == 'D3' or selection == 'd3' and amount > twix.price :
  print("Thank you for your purchase. Please take your item and your change.")
elif selection == 'D3' or selection == 'd3' and amount < twix.price :
  print("You have not inserted enough money. Please insert the correct amount.")

else : 
  print("Please enter a valid amount.")
  