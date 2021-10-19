#Week 4 Lab 3
hot = "Hot"
aww = "You're it!"
not_it = "Potatoe"
tag = "Darn!"
 $
x = input("""Pick a number from 1 -20
""")
x = int(x)
for x in range(1,21):
    if x <=20:
        print(hot + " " + not_it)
        if x ==15:
            print(aww + " " + tag)
            break
