def computepay(h,r):
    if h>40:
        pay = 40*r + (h-40)* r*1.5
    else:
        pay = h*r
    return pay

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter rate:")
r=float(rate)
pay = computepay(h,r)
print("Pay ",pay)
