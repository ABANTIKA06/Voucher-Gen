import random
import psycopg2
from psycopg2 import sql, errors


def get_db_connection():
    return psycopg2.connect(
        dbname="coupons",
        user="postgres",
        password="271800",  # Ensure this is the correct password
        host="localhost"
    )

def calculator():
    NP = float(input("Newspaper wt(kg): "))
    NP_value = NP * 10
    Clothes = float(input("Enter the weight of clothes(kg): ")) 
    Cloth_value = Clothes * 15 
    total_value = NP_value + Cloth_value

    print(f"""
           Newspaper Value: {NP_value}
           Clothes Value: {Cloth_value}
           Total Value: {total_value}
           """)
    return NP, Clothes, total_value

def Customer():
    name = input("Enter your name: ")
    while True:
        Mob = int(input("Enter your mobile number: "))
        if len(str(Mob)) == 10:
            break
        else:
            print("Invalid mobile number. Please enter a 10-digit number.")
    while True:
        Email = input("Enter your email: ")
        if "@" in Email and "." in Email:
            break
        else:
            print("Invalid email. Please include an '@' and a '.' in the email address.")
    
    base = random.choice(["W" + str(i) for i in range(1, 100)])
    Random_Coupon_No = base + "-" + str(random.randint(100000, 999999))
    
    # Print the generated coupon code
    print(f"""
          Name:{name}
          Mobile:{Mob}
          Email:{Email}
          Coupon:{Random_Coupon_No}""")
    
    return name, Mob, Email, Random_Coupon_No

def insert_coupon(name, Mob, Email, NP, Clothes, total_value, Coupon_No):
    conn = get_db_connection()
    cur = conn.cursor()                     #connecting cursor library in python for database
    try:
        cur.execute(
            "INSERT INTO mar_coupon (name, mobile, email, newspaper_wt, clothes_wt, total_val, coupon_code) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, Mob, Email, NP, Clothes, total_value, Coupon_No)
        )
        conn.commit()
        print("Coupon inserted successfully")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cur.close()
        conn.close()

# Example usage
NP, Clothes, total_value = calculator()
name, Mob, Email, Coupon_No = Customer()
insert_coupon(name, Mob, Email, NP, Clothes, total_value, Coupon_No)