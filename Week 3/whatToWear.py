#Project: What to Wear

#Condition 1: Temp is >= 80 (wear shorts and pack sun glasses. 
#Condition 2: Temp between 60 and 79 degrees (wear a light jacket)
#condition 3: Temp <= 59 (wear a coat in addition to a hat, gloves, and scarf)

temperature = int(input("What is the current temperture? "))

if temperature >= 80:
    outfit = "shorts and pack your sunglasses"

elif temperature <= 79 and temperature >= 60:
    outfit = "a light jacket"

else:
    outfit = "a coat in addition to a hat, gloves, and scarf."

advice = (f"Today you should wear {outfit}.")

print(advice)
