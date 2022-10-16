"""
The Credit Card Simulator Project
Student: Qixian Aiden Wang, Zhiquan Yang (Gary)
Date: Oct. 16, 2022
"""

# You should modify initialize()
def initialize():
    global owed_list, month_owed_interest_list
    global last_update_month
    global prev_day, prev_month
    global prev_country1, prev_country2
    global disable_flag, prev_country_flag
    global purchase_count

    owed_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    month_owed_interest_list = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    last_update_month = 1
    prev_day = 0
    prev_month = 0
    prev_country1 = None
    prev_country2 = None
    purchase_count = 0
    disable_flag = False
    prev_country_flag = 1 

def update_owed(month):
    global owed_list, month_owed_interest_list
    global last_update_month
    global prev_day, prev_month
    global prev_country1, prev_country2
    global disable_flag, prev_country_flag

    for i in range(1, month+1):
        if i > last_update_month:
            month_owed_interest_list[i] += month-i
        else:
            month_owed_interest_list[i] += month-last_update_month

    last_update_month = month
    
    return

def date_same_or_later(day1, month1, day2, month2):
    if month1 > month2:
        return True
    elif month1 == month2:
        if day1 >= day2:
            return True
    else:
        return False
    
def all_three_different(c1, c2, c3):
    if c1 != c2 and c2 != c3 and c1 != c3:
        return True
    else:
        return False
        
def purchase(amount, day, month, country):
    global owed_list, month_owed_interest_list
    global last_update_month
    global prev_day, prev_month
    global prev_country1, prev_country2
    global disable_flag, prev_country_flag
    global purchase_count
    

    if disable_flag:
        return "error"
    
    if not date_same_or_later(day, month, prev_day, prev_month):
        disable_flag = True
        return "error"
    
    purchase_count += 1
    if purchase_count >= 3:
        if all_three_different(country, prev_country1, prev_country2):
            disable_flag = True
            return "error"
  
    

    if prev_country_flag == 1:
        prev_country1 = country
        prev_country_flag = 2
    else:
        prev_country2 = country
        prev_country_flag = 1

    owed_list[month] += amount    

    update_owed(month)

    prev_day = day
    prev_month = month 
    
def amount_owed(day, month):
    global owed_list, month_owed_interest_list
    global last_update_month
    global prev_day, prev_month
    global prev_country1, prev_country2
    global disable_flag, prev_country_flag

    if not date_same_or_later(day, month, prev_day, prev_month):
        disable_flag = True
        return "error"

    update_owed(month)

    prev_day = day
    prev_month = month

    total_owed = 0
    for i in range(1, month + 1):
        if month_owed_interest_list[i] <= 0:
            total_owed += owed_list[i]
        else:
            total_owed += \
                owed_list[i] * ((1.05)**(month_owed_interest_list[i]))
    return total_owed
    
def pay_bill(amount, day, month):
    global owed_list, month_owed_interest_list
    global last_update_month
    global prev_day, prev_month
    global prev_country1, prev_country2
    global disable_flag, prev_country_flag

    if not date_same_or_later(day, month, prev_day, prev_month):
        disable_flag = True
        return "error"

    update_owed(month)

    prev_day = day
    prev_month = month

    month_counter = 1
    while amount != 0:
        if month_counter > 12:
            return "error"

        if month_owed_interest_list[month_counter] > 0:
            owed_list[month_counter] = owed_list[month_counter] \
                * ((1.05)**(month_owed_interest_list[month_counter]))
        

        if amount <= owed_list[month_counter]:
            owed_list[month_counter] -= amount
            if month_owed_interest_list[month_counter] > 0:
                month_owed_interest_list[month_counter] = 0
            amount = 0
        else:
            amount -= owed_list[month_counter]
            owed_list[month_counter] = 0
            month_counter += 1

# Initialize all global variables outside the main block.
initialize()		
    
if __name__ == '__main__':

    initialize()
    print("Prof's Test Case")
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in
                                                #          a row)

    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase
                                                #           declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375

                                                # (43.65375*1.05+40)
    #Test Case 1  (general case)
    print("Test Case 1")
    initialize()
    purchase(20, 3, 1, "Canada")
    print("Now owing:", amount_owed(3, 1))      # 20.0
    pay_bill(10, 4, 5)
    print("Now owing:", amount_owed(4, 5))      # 13.1525   (20*1.05*1.05*1.05-10)


    #Test Case 2  (general case)
    print("Test Case 2")
    initialize()
    purchase(30, 2, 1, "Canada")
    print("Now owing:", amount_owed(2, 1))      # 30.0
    purchase(40, 4, 1, "United States")
    print("Now owing:", amount_owed(4, 1))      # 70.0
    purchase(60, 5, 4, "United States")
    print("Now owing:", amount_owed(5, 4))      # 137.175 (30*1.05^2+40*1.05^2+60)
    pay_bill(50, 5, 5)
    print("Now owing:", amount_owed(5, 5))      # 91.03375 ((30+40)*1.05^3+60-50)


    #Test Case 3 (The money paid is greater than the interest but not paid in full)
    print("Test Case 3")
    initialize()
    purchase(40, 3, 5, "Canada")
    print("Now owing:", amount_owed(3, 5))      # 40.0
    purchase(50, 4, 8, "United States")
    print("Now owing:", amount_owed(4, 8))      # 94.1       (40*1.05^2+50)
    purchase(30, 4, 10, "Canada")
    print("Now owing:", amount_owed(4, 10))     # 131.12025  (40*1.05^4+50*1.05+30)
    pay_bill(110, 5, 10)
    print("Now owing:", amount_owed(5, 10))     # 21.12025
    purchase(20, 14, 12, "Canada")
    print("Now owing:", amount_owed(14, 12))    # 42.1762625 (21.12025*1.05+20)

    #Test case 4 (The money paid smaller than the insterest)
    print("Test Case 4")
    initialize()
    purchase(30, 4, 1, "Canada")
    print("Now owing:", amount_owed(4, 1))     # 30.0
    purchase(60, 3, 3, "Japan")
    print("Now owing:", amount_owed(3, 3))     # 91.5 (30*1.05+60)
    pay_bill(10, 4, 3)
    print("Now owing:", amount_owed(4, 3))     # 81.5 (30*1.05-10+60)
    purchase(30, 6, 5, "Japan")
    print("Now owing:", amount_owed(6, 5))     # 116.70375


    #Test case 5 (general case cover 1-12 months)
    print("Test Case 5")
    initialize()
    purchase(10, 2, 1, "China")
    print("Now owing:", amount_owed(2, 1))      # 10.0
    purchase(20, 4, 2, "Canada")
    print("Now owing:", amount_owed(4, 2))      # 30.0
    purchase(30, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 60.5
    pay_bill(15, 9, 4)
    print("Now owing:", amount_owed(9, 4))      # 47.025
    purchase(30, 14, 5, "United States")
    print("Now owing:", amount_owed(14, 5))     # 79.37625
    pay_bill(20, 21, 6)
    print("Now owing:", amount_owed(21, 6))     # 61.8450625
    purchase(60, 1, 7, "United States")
    print("Now owing:", amount_owed(1, 7))      # 124.937315625
    purchase(10, 24, 8, "United States")
    print("Now owing:", amount_owed(24, 8))     # 138.18418140625
    pay_bill(20, 2, 9)
    print("Now owing:", amount_owed(2, 9))      # 124.59339047656252
    purchase(40, 5, 10, "Canada")
    print("Now owing:", amount_owed(5, 10))     # 170.82306000039063
    pay_bill(100, 7, 11)
    print("Now owing:", amount_owed(7, 11))     # 77.36421300041019
    purchase(10, 12, 12, "France")              # error


    print("Now owing:", amount_owed(12, 12))    # 81.2324236504307

    #Test Case 6 (Month error)
    print("Test Case 6")
    initialize()
    purchase(20, 3, 1, "Germany")
    print("Now owing:", amount_owed(3, 1))      # 20.0
    purchase(30, 4, 3, "United States")
    print("Now owing:", amount_owed(4, 3))      # 51.0
    purchase(10, 4, 2, "United States")
    print("Now owing:", amount_owed(4, 2))      # Error

    #Test Case 7 (Day goes wrong)
    initialize()
    print("Test Case 7")
    purchase(10, 6, 1, "Germany")
    print("Now owing:", amount_owed(6, 1))      # 10.0
    purchase(30, 4, 3, "United States")
    print("Now owing:", amount_owed(4, 3))      # 40.5
    purchase(10, 1, 3, "United States")
    print("Now owing:", amount_owed(1, 3))      # Error