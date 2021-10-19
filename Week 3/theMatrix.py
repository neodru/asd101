#Project: Discusion 3, Exploring Conditions
#The Matrix Resserecution Scence 4

pill = (input("""Morpheus gave you two options,
the red pill or the blue pill.
Did you take the red pill?
Please type 'yes' or 'no'

"""))

if pill  == "yes": 
    catchyLine = "...You just may be the chosen one."

elif pill == "no":
    catchyLine = "...Have fun being machine food, I'm out"

else:
    catchyLine = "...I think there's a glitch in the Matrix"

response = (f"Neo{catchyLine}. ")

print(response)

