print("enter last name ")
last = input()
print("what is your credit hours")
ch = int(input())
print("what is your district code? (i or o) ")
dc = input()
if dc == "l":
    pch = 250
else:
    pch = 550
t = ch * pch
print(last + "Your tuition owned is = " + str(t))
