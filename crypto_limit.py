#######################################################################
#Program to see the profit of a day , max limit - min limit
######################################################################


def take_inp():
    lower = float(input("Enter the lower limit of your Currency "))
    upper = float(input("Enter the upper limit of your currency "))
    inv = float(input("Enter the amount you want to invest : "))
    return(lower,upper,inv)

def calc_prof(li):
    crypto_low_amt = li[2] / li[0]
    return li[1]*crypto_low_amt - li[2]

li = list(take_inp())
print("If you are buying your crypto with the min price of {} and when the price reaches {} you will get the profit of {} with the investment of {} ".format(li[0],li[1],calc_prof(li),li[2]))

i = True
while i is True:
    try:
        new_amt = float(input("Do you wanna try with different investment amount , Press 0 to quit else  enter new investment amount"))
    except:
        print("Have a good profit!!")
        new_amt = 0.0
    if  bool(new_amt) == True:
    
        li[2] = new_amt
        print("Profit will be {} with the investment of {}".format(calc_prof(li),li[2]))
    else:
        i = False




    



