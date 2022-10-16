"""
The Credit Card Simulator Project
Student: Qixian Aiden Wang, Gary Z
Date: Oct. 16, 2022
"""

# You should modify initialize()
def initialize():
    global owing_list
    global prev_day, prev_month
    global prev_country1, prev_country2
    global disable_flag, prev_country_flag

    owing_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    prev_day = 0
    prev_month = 0
    prev_country1 = None
    prev_country2 = None
    disable_flag = False
    prev_country_flag = 1 

def date_same_or_later(day1, month1, day2, month2):
    if month1 > month2:
        return True
    elif month1 == month2:
        if day1 >= day2:
            return True
        else:
            return False
    else:
        return False
    
def all_three_different(c1, c2, c3):
    if c1 != c2 and c2 != c3 and c1 != c3:
        return True
    else:
        return False
        
def purchase(amount, day, month, country):
    if disable_flag:
        return "error"
    
    if not date_same_or_later(day, month, prev_day, prev_month):
        disable_flag = True
        return "error"
    
    if not all_three_different(country, prev_country1, prev_country2):
        disable_flag = True
        return "error"
  
    if prev_country_flag == 1:
        prev_country1 = country
        prev_country_flag = 2
    else:
        prev_country2 = country
        prev_country_flag = 1

    prev_day = day
    prev_month = month

    owing_list[month-1] = amount
    
def amount_owed(day, month):
    owned = 0
    for i in range(month):
        month_diff = month - (i + 1)
        if month_diff < 2:
            owned += owing_list[i]
        else:
            owned += owing_list[i] * ((1.05)**(month_diff-1))
    
def pay_bill(amount, day, month):
    pass
        

# Initialize all global variables outside the main block.
initialize()		
    
if __name__ == '__main__':
    # Describe your testing strategy and implement it below.
    # What you see here is just the simulation from the handout, which
    # doesn't work yet.
    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0                              (Test1)
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)                 (Test2)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)               (Test3)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)               (Test4)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)               (Test5)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05) (Test6)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375                          (Test7)
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in    (Test8)
                                                #          a row)
                                                
    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase     (Test9)
                                                #           declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)          (Test10)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375                        (Test11)
                                                # (43.65375*1.05+40)
                                            
                                            
    
