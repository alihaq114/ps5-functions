print("Enter quantity")
q = int(input())
print("enter Price")
p = int(input())
total = q * p
if total >= 100000:
    d = total * 0.1
print("Your guantity is = " + str(q) + " your number per item is = " + str(p) + " your Total is = " + str(total))
