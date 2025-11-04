import random
import psycopg2
from psycopg2 import sql, errors

def cust_detail():
    name=input("Enter your name: ")
    address=input("Enter your address: ")
    mobile=input("Enter your mobile number: ")
    email=input("Enter your email: ")

    Customer_Detail = f"""
    Name: {name}
    Address: {address}
    Mobile: {mobile}
    Email: {email}
    """
    return(Customer_Detail)


def gen_voucher():
    base=random.choice(['W1','W2','W3','W4','W5','W7'])
    voucher=base+str(random.randint(1000000,9999999))
    return(voucher)

def voucher_calc():
    clothes_synthetic=float(input("Enter the weight of Synthetic clothes(kg): "))
    value_clothes_synthetic=clothes_synthetic*20
    clothes_cotton=float(input("Enter the weight of Cotton clothes(kg): "))
    value_clothes_cotton=clothes_cotton*30
    tapestry=float(input("Enter the weight of tapestry(kg): "))
    value_tapestry=tapestry*25
    total_value=value_clothes_synthetic+value_clothes_cotton+value_tapestry
    return(total_value)

def voucher_print():
    print(f"Voucher Number: {gen_voucher()}")
    print(f"Customer Detail: {cust_detail()}")
    print(f"Voucher Value: {voucher_calc()}")

voucher_print()

def get_db_connection():
    return psycopg2.connect(
        dbname="voucher",
        user="postgres",
        password="228900",  # Ensure this is the correct password
        host="localhost"
    )

