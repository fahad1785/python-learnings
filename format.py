#We cant combine string and number 
#But it can be done using (format method)
# format is

age = 23
personal_details = "my name is fahad and im {}"
print (personal_details.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#using index number 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {0} pieces of item {1} for {2} dollars."
print(myorder.format(quantity, itemno, price))