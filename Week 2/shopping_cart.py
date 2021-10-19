#Chapter 5 : Shopping for Science Fair Supplies
budget = float(input(How much money do you want to spend?))
flowerpot = int(input("How many flowerpots? "))
flower_seeds = int(input("How many packs of flower seeds? "))
soil = int(input("How many bags of soil? "))
#cost of items
flowerpot_price = 4.00
flower_seeds_price = 1.00
soil_price = 5.00

tax_rate = 0.06
cost_of_items = (flowerpot * flowerpot_price) + (flower_seeds * flower_seeds_price) + (soil * soil_price)
print(f"Sub Total:  + {cost_of_items}")
print(tax_rate)
tax = (cost_of_items * tax_rate)
print(f"Tax total:  + {tax}")
total_cost = (cost_of_items * tax_rate) + cost_of_items
print(f"Total Cost: + {total_cost}")

print("Thank you, sorry no refunds")
