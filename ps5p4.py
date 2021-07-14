print("what is your last name ")
last = input()
print("what is your job code? (l) (j) or (a) ")
jc = input()
print("what is your hours worked? ")
hw = int(input())
if jc == "a":
    pr = 30
else:
    if jc == "l":
        pr = 25
    else:
        if jc == "j":
            pr = 50
        else:
            print("thank you for using this program im sorry but we are unable to do anything for you because of your job coding being invaild please try again if you think the job code you typed was wrong. ")
            pr = 0
gross = pr * hw
print("Thank you for using this program " + last + " your total gross pay is " + str(gross))
