#Fruit Joke
guess = input(""""In my bag I have an apple, a banana,
a cherry, and anorange.
Pick the right and the fruit is yours.
""")
guess.lower()
fruits = ["apple", "banana", "cherry", "orange"]
for guess in fruits[::]:
    if guess != fruits[:4:]:
        print("Nope")
    else:
        guess == fruit[4]
        print("Orange you happy?")
        
        
