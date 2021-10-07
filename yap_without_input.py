import sys
import math

age = 5.2
gender = "F"
sourse_of_income = "собственный бизнес"
last_year_income = 1
credit_rating = 2
requested_amount = 2
maturity = 7
aim = "Автокредит"



if age < 0:
     sys.exit("Некорректный возраст")

gender_list = ["m", "f"]
if gender.lower() not in gender_list:
     sys.exit("Некорректный пол")

sourse_of_income_list = ["пассивный доход", "наёмный работник", "собственный бизнес", "безработный"]
if sourse_of_income.lower() not in sourse_of_income_list:
     sys.exit("Некорректный источник дохода")

if last_year_income < 0:
    sys.exit("Некорректный доход")

if not -2 <= credit_rating <= 2:
     sys.exit("Некорректный кредитный рейтинг")

if not 0.1 <= requested_amount <= 10:
    sys.exit("Некорректная запрошенная сумма")

if not 1 <= maturity <= 20:
    sys.exit("Некорректный срок погашения")

aim_list = ["ипотека", "развитие бизнеса", "автокредит", "потребительский"]
if aim.lower() not in aim_list:
     sys.exit("Некорректныая цель")


base_rate = 0.1

if gender.lower() == "f":
    retirement_age = 60
else:
    retirement_age = 65

# calculate sum
if sourse_of_income.lower() == "пассивный доход":
    max_sum_income = 1
elif sourse_of_income.lower() == "наёмный работник":
    max_sum_income = 5
else:
    max_sum_income = 10

if credit_rating == -1:
    max_sum_rating = 1
elif credit_rating == 0:
    max_sum_rating = 5
else:
    max_sum_rating = 10

agreed_sum = min(max_sum_income, max_sum_rating)

credit_sum = min(requested_amount, agreed_sum)

# calculate modifier
if aim.lower() == "ипотека":
    modifier_aim = -0.002
elif aim.lower() == "развитие бизнеса":
    modifier_aim = -0.005
elif aim.lower() == "потребительский":
    modifier_aim = 0.0015
else:
    modifier_aim = 0

if credit_rating == -1:
    modifier_rating = 0.0015
elif credit_rating == 0:
    modifier_rating = 0
elif credit_rating == 1:
    modifier_rating = -0.0025
else:
    modifier_rating = -0.0075

modifier_sum = -0.001 * math.log10(credit_sum)


if sourse_of_income.lower() == "пассивный доход":
    modifier_work = 0.005
elif sourse_of_income.lower() == "наёмный работник":
    modifier_work = -0.0025
else:
    modifier_work = 0.0025

modifier = modifier_aim + modifier_rating + modifier_sum + modifier_work


rate = base_rate + modifier

#calculate annual payment
annual_payment = (credit_sum * (1 + maturity * (base_rate + modifier))) / maturity



# decision
if age < retirement_age and last_year_income / 3 > requested_amount / maturity and credit_rating != -2 and sourse_of_income.lower() != "безработный" and last_year_income / 2 > annual_payment:
    decision = "YES"
else:
    decision = "NO"

if decision == "YES":
    print("Кредит выдается.\nГодовой платеж по кредиту:", round(annual_payment * 1000000) , "рублей")
else:
    print("Кредит не выдается")
