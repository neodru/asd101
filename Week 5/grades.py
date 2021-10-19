score = input("Enter Score: ")
try:
    score = float(score)
except:
    print("Error!")
 
    
if score >= 0.9:
    print ("A")
elif score < .9 and score >= .8:
    print ("B")
elif score < .8 and score >= .7  :
    score < .8 and score >= .7
    print("C")
elif score < .7 and score >= .6:
    print ("D")
else:
    print("F")

