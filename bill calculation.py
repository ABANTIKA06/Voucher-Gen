def bill_val(amount):
    if amount >=1000:
        use=amount*0.1
        remaining=amount-use
        return("you can use",str(use), "coupons . with", str(remaining),"Bill amount")
    else:
        return('you cant use coupons bellow 1000',amount)


def coupons_to_use(coupon_amt):
    bill_amt = coupon_amt*10
    return (bill_amt)

def coupon_calc(coupon_amt, bill_amt):
    coupon1=bill_amt*0.1
    if coupon_amt>coupon1:
        return("coupon remaining" str(coupon_amt-coupon1), 
               "")
def select_calc():
    print("1.bill_val::")
    print("2.coupons_to_use::")
    print("3.exit::")
    choice = int(input("enter your choice:::"))
    if choice == 1:
        amount = int(input("enter the amount of bill:::"))
        print(bill_val(amount))
    elif choice == 2:
        coupon_amt = int(input("enter the coupon amount:::"))
        print(coupons_to_use(coupon_amt))
    elif choice == 3:
        exit()
    else:
        print("invalid choice")


select_calc()



