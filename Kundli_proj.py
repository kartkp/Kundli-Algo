#BHOG
def subtract_time(input_time):
    try:
       
        hours, minutes = map(int, input_time.split(':'))

      
        result_hours =  59 - hours
        result_minutes = 60 - minutes

       
        if result_minutes < 0:
            result_hours -= 1
            result_minutes += 60

        
        result_time = f"{result_hours:02d}:{result_minutes:02d}"
        return result_time
    except ValueError:
        return "Invalid input. Please enter time in hr:min format."

user_input = input("Enter BHOG INPUT (e.g., 12:30): ")

a = subtract_time(user_input)

print(f"The Result Of BHOG INPUT {user_input} is: {a}")
print()

#ESTKAAL
def compare_dates(time1, time2):
    global pi
    
    try:
        hr1, min1 = map(int, time1.split(':'))
        hr2, min2 = map(int, time2.split(':'))

        jk1 = hr1*60 + min1
        jk2 = hr2*60 + min2

        if jk1 > jk2:
            try:
                if min1 < min2:
                    min1 += 60
                    hr1 -= 1
                    mins = min1 - min2
                    hrs = hr1 - hr2
                else:
                    mins = min1 - min2
                    hrs = hr1 - hr2
                pi = f"{hrs}:{mins}"

            except ValueError:
                return "Invalid date format. Please use the format day-month-year."
        
        elif jk1 < jk2:
            min_12= 00
            hr_12= 12
            if min2 > min_12:
                min_12 += 60
                hr_12 -= 1
                hr_sun = hr_12 - hr2
                min_sun = min_12 - min2
            else:
                hr_sun = hr_12 - hr2
                min_sun = min_12 - min2
            hrs= hr_sun + 12 + hr1
            mins= min_sun + min1
            if mins >= 60:
                mins -= 60
                hrs += 1
                
            pi = f"{hrs}:{mins}"
            
    except ValueError:
        return "Invalid date format. Please use the format day-month-year."

    return pi
from datetime import datetime, timedelta

def get_time_input():
    while True:
        time1 = input("Enter The TIME OF BIRTH in hr:min Format : ")
        time2 = input("Enter The SURYODAY in hr:min Format : ")
        time_input = compare_dates(time1, time2)
        print(time_input)
        try:
            hours, minutes = map(int, time_input.split(':'))
            if 0 <= hours  and 0 <= minutes < 60:
                return timedelta(hours=hours, minutes=minutes)
            else:
                print("Invalid input. Please enter a valid time.")
        except ValueError:
            print("Invalid input. Please enter the time in the correct format.")

def multiply_time_by_constant(time, constant):
    multiplied_time = time * constant
    return multiplied_time

def main():
    global b
    time_input = get_time_input()

    constant = 2.5

    result_timedelta = multiply_time_by_constant(time_input, constant)


    days = result_timedelta.days
    hours, remainder = divmod(result_timedelta.seconds, 3600)
    minutes = remainder // 60

    total_hours = (days * 24) + hours
    print(f"\nThe Result Of ESTKAAL {constant} is: {total_hours:02d}:{minutes:02d}")
    b = (f"{total_hours:02d}:{minutes:02d}")


main()
print()

#BHAYAAT
def add_times(a, b):
    global c
    try:
        hours1, minutes1 = map(int, a.split(':'))
        hours2, minutes2 = map(int, b.split(':'))

        total_hours = hours1 + hours2
        total_minutes = minutes1 + minutes2

        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60

        result_time = f"{total_hours:02d}:{total_minutes:02d}"

        if total_hours > 60:
            total_hours -= 60

        print (f"The Result Of BHAYAAT OF {a} and {b} is: {total_hours:02d}:{total_minutes:02d}")
        c = (f"{total_hours:02d}:{total_minutes:02d}")
    except ValueError:
        return "Invalid input. Please enter times in the correct format (hr:min)."
result = add_times(a, b)

print(result)
print()

#BHAYAAT PALIKRITT
bp = (int(c.split(':')[0]) * 60) + int(c.split(':')[1])
print (f"The Result Of BHAYAAT PALIKRITT is: {bp}")
print()

#BHABHOG
def add_times(a, additional_time_str):
    global d
    try:
        hours1, minutes1 = map(int, a.split(':'))
 
        additional_hours, additional_minutes = map(int, additional_time_str.split(':'))

        total_hours = hours1 + additional_hours
        total_minutes = minutes1 + additional_minutes

        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60

        if total_hours > 66:
            total_hours -= 60

        result_time = f"{total_hours:02d}:{total_minutes:02d}"
        print (f"The Result Of BHABHOG Of {a} and {additional_time_str} is: {result_time}")
        d= (f"{result_time}")
    except ValueError:
        return "Invalid input. Please enter times in the correct format (hr:min)."




additional_time_str = input("Enter The BHABHOG INPUT (e.g., 02:15): ")

result = add_times(a, additional_time_str)

print(result)
print()

#BHABHOG PALIKRITT
bgp = (int(d.split(':')[0]) * 60) + int(d.split(':')[1])
print (f"The Result Of BHABHOG PALIKRITT is: {bgp}")
print()

#MAHADASHAA
def multiply_with_day_multiplier(day):
    global result
    global ex
    global day_multipliers
    
    day_multipliers = {
        1: 6,
        2: 10,
        3: 7,
        4: 17,
        5: 16,
        6: 20,
        7: 19,
        8: 18,
        9: 7
    }

    if day in day_multipliers:

        result =  bp * day_multipliers[day]
        ex = day_multipliers[day]
        print(f"The Result For Day Is: {result}")
    else:
        print("Invalid day. Please provide a day between 1 and 7.")


user_day = int(input("1:SURYA(6)\n2:CHANDRA(10)\n3:MANGAL(7)\n4:BUDHH(17)\n5:GURU(16)\n6:SHUKRA(20)\n7:SHANI(19)\n8:RAAHU(18)\n9:KETU(7)\n:- "))


multiply_with_day_multiplier(user_day)
int_bp = int(bp)
int_bgp = int(bgp)
int_result = int(result)

#DIVIDE MAHADASHAA
def divide_and_compute(int_result, int_bgp):
    global q1, q2, q3
    q1 = int_result // int_bgp
    remainder1 = int_result % int_bgp
    print(f"1st: {q1}")


    remainder2 = remainder1 * 12
    q2 = remainder2 // int_bgp
    remainder2 = remainder2 % int_bgp
    print(f"2nd: {q2}")


    remainder3 = remainder2 * 30
    q3 = remainder3 // int_bgp
    print(f"3rd: {q3}")

if int_bgp == 0:
    print("Error!!!: Division by zero!!! PAGAL HAI KYAA!!")
else:
    print(f"The bgp is: {int_bgp}")
    print(f"The result is: {int_result}")
    divide_and_compute(int_result, int_bgp)
print()
time = (f"{q1}:{q2}:{q3}")
print(time)
time2 = time
print()



# DATE CALCULATOR

def parse_time(time_str):
    try:
        year, month, day = map(int, time_str.split(':'))
        return year, month, day
    except ValueError:
        raise ValueError("Invalid input. Please enter the time in the correct format.")

def subtract_times(time1, time2):

    year1, month1, day1 = time1


    year2, month2, day2 = time2


    days_diff = day1 - day2


    if days_diff < 0:
        month1 -= 1
        days_diff += 30 

    months_diff = month1 - month2

    if months_diff < 0:
        year1 -= 1
        months_diff += 12


    years_diff = year1 - year2

    return years_diff, months_diff, days_diff

def main():
    global years_diff
    global months_diff
    global days_diff
    global ya
    print("The Time (yr:month:days format):")
    user_input1 = (f"{ex-1}:11:30")
    time1 = parse_time(user_input1)

    
    user_input2 = time
    time2 = parse_time(user_input2)


    years_diff, months_diff, days_diff = subtract_times(time1, time2)

    print(f"\nThe difference is: {years_diff} years, {months_diff} months, and {days_diff} days")
    ya= f"{days_diff}-{months_diff}-{years_diff}"


main()
yearall= ya
bp_ex = int_bp * 60
print()

#CHANDRAANSH
# Check user's choice

def chandraansh_divide(int_result, int_bgp):
    global quotient1
    global quotient2
    global quotient3
    
    quotient1 = bp_ex // int_bgp
    remainder1 = bp_ex % int_bgp
    print(f"1st: {quotient1}")


    remainder2 = remainder1 * 60
    quotient2 = remainder2 // int_bgp
    remainder2 = remainder2 % int_bgp
    print(f"2nd: {quotient2}")


    remainder3 = remainder2 * 60
    quotient3 = remainder3 // int_bgp
    print(f"3rd: {quotient3}")
    
userx_choice = input("Do you want to perform the CHANDRAANSH?? (y/n): ")
def multiply_gat(dayzz):
    global gat
    
    
    day_multipliersx = {
        1: 27,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10,
        12: 11,
        13: 12,
        14: 13,
        15: 14,
        16: 15,
        17: 16,
        18: 17,
        19: 18,
        20: 19,
        21: 20,
        22: 21,
        23: 22,
        24: 23,
        25: 24,
        26: 25,
        27: 26
    }

    if dayzz in day_multipliersx:

        gat = day_multipliersx[dayzz] * 60
    
        print(f"The gat For Day Is: {gat}")
    else:
        print("Invalid day. Please provide a day between 1 and 27 Only.")
if userx_choice.lower() == 'y':
    
    if int_bgp == 0:
        print("Error!!!: Division by zero!!! PAGAL HAI KYAA!!")
        
    else:
        print(f"The bgp is: {int_bgp}")
        print(f"The result is: {bp_ex}")
        chandraansh_divide(bp_ex, int_bgp)
        print()
        timen = (f"{quotient1}:{quotient2}:{quotient3}")
        print(timen)
        timen2 = timen
        print()
        
        gn = int(input("1. Ashwani\n2. Bharni\n3. Kritika\n4. Rohni\n5. Mrigshira\n6. Aadra\n7. Punarvashu\n8. Pushyami\n9. Aslesha\n10. Magha\n11. Purva Falguni\n12. Uttaraa Falguni\n13. Hastt\n14. Chitraa\n15. Swati\n16. Vishakha\n17. Anuradha\n18. Jeshtha\n19. Muul\n20. Purva Aasaadh\n21. Uttara Aasaadh\n22. Shravad\n23. Dhanistha\n24. Satbhikha\n25. Purva Bhadrapad\n26. Uttar Bhadrapad\n27. Revti\nEnter The GAT NAKSHATRA : "))

        dayzz=int(gn)
        multiply_gat(dayzz)
        print()
        print(timen2)
        print()

        hr_plus_gat = (int(timen2.split(':')[0]) + gat )
        print (hr_plus_gat)
        print()
        hr_plus_gat_2 = hr_plus_gat * 2
        print(hr_plus_gat_2)
        min_2 = (int(timen2.split(':')[1]) * 2)
        print (min_2)
        sec_2 = (int(timen2.split(':')[2]) * 2)
        print(sec_2)
        yo = (f"{hr_plus_gat_2}:{min_2}:{sec_2}")
        print(yo)
        print()
        def divide_by_9():
            global quo1
            global quo2
            global quo3
    
            quo1 = hr_plus_gat_2 // 9
            remainder1 = hr_plus_gat_2 % 9
            print(f"1st: {quo1}")


            remainder2 = remainder1 * 60 + (min_2)
            quo2 = remainder2 // 9
            remainder2 = remainder2 % 9
            print(f"2nd: {quo2}")


            remainder3 = remainder2 * 60 + (sec_2)
            quo3 = remainder3 // 9
            print(f"3rd: {quo3}")

            
    
        divide_by_9()
        print()
        timenx = (f"{quo1}:{quo2}:{quo3}")
        print(timenx)
        timenx2 = timenx
        print()
    
        def quo_bruh():
            global quox1
            global remx1
            global timenx
            quox1 = quo1 // 30
            remx1 = quo1 % 30
            timenx = (f"{quox1} : {remx1} : {quo2} : {quo3}")
            print(f"YOUR CHANDRAANSH IS :-\n{timenx}")
        quo_bruh()
        print()
        print()
    
else:
    print("\nOKAY THANKS FOR DEVELOPING ME ;) XOXO...!")
    print()
#DATE ADDER
def add_dates(date1, date2):
    global ds, ms, ys
    global zzz
    
    try:
        day1, month1, year1 = map(int, date1.split('-'))
        day2, month2, year2 = map(int, date2.split('-'))

        ds = day1 + day2
        ms = month1 + month2
        ys = year1 + year2

        if ds > 30:
            ds -= 30
            ms += 1

        if ms > 12:
            ms -= 12
            ys += 1

        zzz = f"{ds}-{ms}-{ys}"
        return zzz    
        

    except ValueError:
        return "Invalid date format. Please use the format day:month:year."
        
#DATE SUBTRACTOR
zzk = ""
dp = ""
jo = 0
def subtract_dates(date1, date2):
    global zzk, dp, jo
    
    try:
        day1, month1, year1 = map(int, date1.split('-'))
        day2, month2, year2 = map(int, date2.split('-'))

        jok1 = day1 + month1 * 30 + year1 * 360
        jok2 = day2 + month2 * 30 + year2 * 360

        if jok1 > jok2 and jo == 0:
            try:
                if day1 < day2:
                    day1 += 30
                    month1 -= 1
                    ds = day1 - day2
                else:
                    ds = day1 - day2

                if month1 < month2:
                    month1 += 12
                    year1 -= 1
                    ms = month1 - month2
                else:
                    ms = month1 - month2

                ys = year1 - year2
                zzk = f"{ds}-{ms}-{ys}"
                dp = date2
            except ValueError:
                return "Invalid date format. Please use the format day-month-year."
        
        elif jok1 < jok2 and jo == 0:
            zzk = date2
            dp = date1
            jo += 1
                
        elif jo == 1:
            zzk = "0-0-0"
            dp = "0-0-0"

    except ValueError:
        return "Invalid date format. Please use the format day-month-year."

    return zzk, dp
    
#BINSHOTTARI
DOB = input("Enter The DOB in Day:Month:Year Format (eg 23:11:2007) : ")
dob1 = (int(DOB.split(':')[0])) + (int(days_diff))
dob2 = (int(DOB.split(':')[1])) + (int(months_diff))
dob3 = (int(DOB.split(':')[2])) + (int(years_diff))
bobo1= (int(DOB.split(':')[0]))
bobo2 = (int(DOB.split(':')[1]))
bobo3 = (int(DOB.split(':')[2]))
bobo= f"{bobo1}-{bobo2}-{bobo3}"
while dob1>=30:
    if dob1>= 30:
        dob2 += 1
        dob1 -= 30
print(dob1)
dob1= int(dob1)
while dob2 >= 12:    
    if dob2>= 12:
        dob3 += 1
        dob2 -= 12
dob2= int(dob2)    
print(dob2)
dob3= int(dob3)
print(dob3)  
print()
print("BINSHOTTARI:-")
print()
if user_day == 1:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} SURYA\n{dob1}-{dob2}-{dob3+10}    10 CHANDRA\n{dob1}-{dob2}-{dob3+7+10}    07 MANGAL\n{dob1}-{dob2}-{dob3+7+10+18}    18 RAAHU\n{dob1}-{dob2}-{dob3+7+10+18+16}    16 GURU\n{dob1}-{dob2}-{dob3+7+10+18+16+19}    19 SHANI\n{dob1}-{dob2}-{dob3+7+10+18+16+19+17}    17 BUDHH\n{dob1}-{dob2}-{dob3+7+10+18+16+19+17+7}    07 KETU\n{dob1}-{dob2}-{dob3+7+10+18+16+19+17+7+20}    20 SHUKRA")
    print()
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    yearall_1, shukra = subtract_dates(yearall, shukrai)
    yearall_2, ketu = subtract_dates(yearall_1, ketui)
    yearall_3, budhh = subtract_dates(yearall_2, budhhi)
    yearall_4, shani = subtract_dates(yearall_3, shanii)
    yearall_5, guru = subtract_dates(yearall_4, gurui)
    yearall_6, raahu = subtract_dates(yearall_5, raahui)
    yearall_7, mangal = subtract_dates(yearall_6, mangali)
    yearall_8, chandra = subtract_dates(yearall_7, chandrai)
    yearall_9, surya = subtract_dates(yearall_8, suryai)
    surya_t = add_dates(bobo, surya)
    chandra_t = add_dates(surya_t, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    guru_t = add_dates(raahu_t, guru)
    shani_t = add_dates(guru_t, shani)
    budhh_t = add_dates(shani_t, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketui        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print (f"{mangal_t}        {mangali}  mangal        ")
    print (f"{raahu_t}        {raahui}  raahu        ")
    print (f"{guru_t}        {gurui}  guru        ")
    print (f"{shani_t}        {shanii}  shani        ")
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print (f"{ketu_t}        {ketui}  ketui        ")
    print (f"{shukra_t}        {shukrai}  shukra        )")
    print (f"{surya_t}        {suryai}  surya        ")
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}        {mangali}  mangal        ")
    print (f"{raahu_t}        {raahui}  raahu        ")
    print (f"{guru_t}        {gurui}  guru        ")
    print (f"{shani_t}        {shanii}  shani        ")
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print (f"{ketu_t}        {ketui}  ketui        ")
    print (f"{shukra_t}        {shukrai}  shukra        ")
    print (f"{surya_t}        {suryai}  surya        ")
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print ("\n")  
    print()
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}        {raahui}  raahu        ")
    print (f"{guru_t}        {gurui}  guru        ")
    print (f"{shani_t}        {shanii}  shani        ")
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print (f"{ketu_t}        {ketui}  ketui        ")
    print (f"{shukra_t}        {shukrai}  shukra        ")
    print (f"{surya_t}        {suryai}  surya        ")
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print (f"{mangal_t}        {mangali}  mangal        ")
    print ("\n")
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}        {gurui}  guru        ")
    print (f"{shani_t}        {shanii}  shani        ")
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print (f"{ketu_t}        {ketui}  ketui        ")
    print (f"{shukra_t}        {shukrai}  shukra        ")
    print (f"{surya_t}        {suryai}  surya        ")
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print (f"{mangal_t}        {mangali}  mangal        ")
    print (f"{raahu_t}        {raahui}  raahu        ")
    print ("\n") 
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}        {shanii}  shani        ")
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print (f"{ketu_t}        {ketui}  ketui        ")
    print (f"{shukra_t}        {shukrai}  shukra        ")
    print (f"{surya_t}        {suryai}  surya        ")
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print (f"{mangal_t}        {mangali}  mangal        ")
    print (f"{raahu_t}        {raahui}  raahu        ")
    print (f"{guru_t}        {gurui}  guru        ")
    print ("\n")
    print("BUDHH:-")
    jo= 0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print (f"{ketu_t}        {ketui}  ketu        ")
    print (f"{shukra_t}        {shukrai}  shukra        ")
    print (f"{surya_t}        {suryai}  surya        ")
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print (f"{mangal_t}        {mangali}  mangal        ")
    print (f"{raahu_t}        {raahui}  raahu        ")
    print (f"{guru_t}        {gurui}  guru        ")
    print (f"{shani_t}        {shanii}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}        {ketui}  ketu        ")
    print (f"{shukra_t}        {shukrai}  shukra        ")
    print (f"{surya_t}        {suryai}  surya        ")
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print (f"{mangal_t}        {mangali}  mangal        ")
    print (f"{raahu_t}        {raahui}  raahu        ")
    print (f"{guru_t}        {gurui}  guru        ")
    print (f"{shani_t}        {shanii}  shani        ")
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}        {shukrai}  shukra        ")
    print (f"{surya_t}        {suryai}  surya        ")
    print (f"{chandra_t}        {chandrai}  chandra        ")
    print (f"{mangal_t}        {mangali}  mangal        ")
    print (f"{raahu_t}        {raahui}  raahu        ")
    print (f"{guru_t}        {gurui}  guru        ")
    print (f"{shani_t}        {shanii}  shani        ")
    print (f"{budhh_t}        {budhhi}  budhh        ")
    print (f"{ketu_t}        {ketui}  ketu        ")
    print ("\n")
if user_day == 2:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} CHANDRA\n{dob1}-{dob2}-{dob3+7}    07 MANGAL\n{dob1}-{dob2}-{dob3+7+18}    18 RAAHU\n{dob1}-{dob2}-{dob3+7+18+16}    16 GURU\n{dob1}-{dob2}-{dob3+7+18+16+19}    19 SHANI\n{dob1}-{dob2}-{dob3+7+18+16+19+17}    17 BUDHH\n{dob1}-{dob2}-{dob3+7+18+16+19+17+7}    07 KETU\n{dob1}-{dob2}-{dob3+7+18+16+19+17+7+20}    20 SHUKRA\n{dob1}-{dob2}-{dob3+7+18+16+19+17+7+20+6}    06 SURYA\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    yearall_1, surya = subtract_dates(yearall, suryai)
    yearall_2, shukra = subtract_dates(yearall_1, shukrai)
    yearall_3, ketu = subtract_dates(yearall_2, ketui)
    yearall_4, budhh = subtract_dates(yearall_3, budhhi)
    yearall_5, shani = subtract_dates(yearall_4, shanii)
    yearall_6, guru = subtract_dates(yearall_5, gurui)
    yearall_7, raahu = subtract_dates(yearall_6, raahui)
    yearall_8, mangal = subtract_dates(yearall_7, mangali)
    yearall_9, chandra = subtract_dates(yearall_8, chandrai)
    chandra_t = add_dates(bobo, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    guru_t = add_dates(raahu_t, guru)
    shani_t = add_dates(guru_t, shani)
    budhh_t = add_dates(shani_t, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    surya_t = add_dates(shukra_t, surya)
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketui        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print ("\n")
    print()
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print ("\n") 
    print()
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print ("\n")
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print ("\n")
    print("BUDHH:-")
    jo= 0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
if user_day == 3:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} MANGAL\n{dob1}-{dob2}-{dob3+18}    18 RAAHU\n{dob1}-{dob2}-{dob3+18+16}    16 GURU\n{dob1}-{dob2}-{dob3+18+16+19}    19 SHANI\n{dob1}-{dob2}-{dob3+18+16+19+17}    17 BUDHH\n{dob1}-{dob2}-{dob3+18+16+19+17+7}    07 KETU\n{dob1}-{dob2}-{dob3+18+16+19+17+7+20}    20 SHUKRA\n{dob1}-{dob2}-{dob3+18+16+19+17+7+20+6}    06 SURYA\n{dob1}-{dob2}-{dob3+18+16+19+17+7+20+6+10}    10 CHANDRA")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    yearall_1, chandra = subtract_dates(yearall, chandrai)
    yearall_2, surya = subtract_dates(yearall_1, suryai)
    yearall_3, shukra = subtract_dates(yearall_2, shukrai)
    yearall_4, ketu = subtract_dates(yearall_3, ketui)
    yearall_5, budhh = subtract_dates(yearall_4, budhhi)
    yearall_6, shani = subtract_dates(yearall_5, shanii)
    yearall_7, guru = subtract_dates(yearall_6, gurui)
    yearall_8, raahu = subtract_dates(yearall_7, raahui)
    yearall_9, mangal = subtract_dates(yearall_8, mangali)
    mangal_t = add_dates(bobo, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    guru_t = add_dates(raahu_t, guru)
    shani_t = add_dates(guru_t, shani)
    budhh_t = add_dates(shani_t, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    surya_t = add_dates(shukra_t, surya)  
    chandra_t = add_dates(surya_t, chandra)
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketui        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print ("\n")
    print()
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print ("\n") 
    print()
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print ("\n") 
    print()
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print ("\n")
    print("BUDHH:-")
    jo= 0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print ("\n")
    print()
if user_day == 8:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} RAAHU\n{dob1}-{dob2}-{dob3+16}    16 GURU\n{dob1}-{dob2}-{dob3+16+19}    19 SHANI\n{dob1}-{dob2}-{dob3+16+19+17}    17 BUDHH\n{dob1}-{dob2}-{dob3+16+19+17+7}    07 KETU\n{dob1}-{dob2}-{dob3+16+19+17+7+20}    20 SHUKRA\n{dob1}-{dob2}-{dob3+16+19+17+7+20+6}    06 SURYA\n{dob1}-{dob2}-{dob3+16+19+17+7+20+6+10}    10 CHANDRA\n{dob1}-{dob2}-{dob3+16+19+17+7+20+6+10+7}    07 MANGAL")
    print ("\n")
    print()
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    yearall_1, mangal = subtract_dates(yearall, mangali)
    yearall_2, chandra = subtract_dates(yearall_1, chandrai)
    yearall_3, surya = subtract_dates(yearall_2, suryai)
    yearall_4, shukra = subtract_dates(yearall_3, shukrai)
    yearall_5, ketu = subtract_dates(yearall_4, ketui)
    yearall_6, budhh = subtract_dates(yearall_5, budhhi)
    yearall_7, shani = subtract_dates(yearall_6, shanii)
    yearall_8, guru = subtract_dates(yearall_7, gurui)
    yearall_9, raahu = subtract_dates(yearall_8, raahui)
    raahu_t = add_dates(bobo, raahu)
    guru_t = add_dates(raahu_t, guru)
    shani_t = add_dates(guru_t, shani)
    budhh_t = add_dates(shani_t, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    surya_t = add_dates(shukra_t, surya)  
    chandra_t = add_dates(surya_t, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketui        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print ("\n") 
    print()
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print ("\n") 
    print()
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print ("\n")
    print ()
    print("BUDHH:-")
    jo= 0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print ("\n")  
    print()
if user_day == 5:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} GURU\n{dob1}-{dob2}-{dob3+19}    19 SHANI\n{dob1}-{dob2}-{dob3+19+17}    17 BUDHH\n{dob1}-{dob2}-{dob3+19+17+7}    07 KETU\n{dob1}-{dob2}-{dob3+19+17+7+20}    20 SHUKRA\n{dob1}-{dob2}-{dob3+19+17+7+20+6}    06 SURYA\n{dob1}-{dob2}-{dob3+19+17+7+20+6+10}    10 CHANDRA\n{dob1}-{dob2}-{dob3+19+17+7+20+6+10+7}    07 MANGAL\n{dob1}-{dob2}-{dob3+19+17+7+20+6+10+7+18}    18 RAAHU")
    print()
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    yearall_1, raahu = subtract_dates(yearall, raahui)
    yearall_2, mangal = subtract_dates(yearall_1, mangali)
    yearall_3, chandra = subtract_dates(yearall_2, chandrai)
    yearall_4, surya = subtract_dates(yearall_3, suryai)
    yearall_5, shukra = subtract_dates(yearall_4, shukrai)
    yearall_6, ketu = subtract_dates(yearall_5, ketui)
    yearall_7, budhh = subtract_dates(yearall_6, budhhi)
    yearall_8, shani = subtract_dates(yearall_7, shanii)
    yearall_9, guru = subtract_dates(yearall_8, gurui)
    guru_t = add_dates(bobo, guru)
    shani_t = add_dates(guru_t, shani)
    budhh_t = add_dates(shani_t, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    surya_t = add_dates(shukra_t, surya)  
    chandra_t = add_dates(surya_t, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketui        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print ("\n")
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print ("\n") 
    print ()
    print("BUDHH:-")
    jo=0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print ("\n")
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print ("\n")
if user_day == 7:
    print(f"\n{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} SHANI\n{dob1}-{dob2}-{dob3+17}    17 BUDHH\n{dob1}-{dob2}-{dob3+17+7}    07 KETU\n{dob1}-{dob2}-{dob3+17+7+20}    20 SHUKRA\n{dob1}-{dob2}-{dob3+17+7+20+6}    06 SURYA\n{dob1}-{dob2}-{dob3+17+7+20+6+10}    10 CHANDRA\n{dob1}-{dob2}-{dob3+17+7+20+6+10+7}    07 MANGAL\n{dob1}-{dob2}-{dob3+17+7+20+6+10+7+18}    18 RAAHU\n{dob1}-{dob2}-{dob3+17+7+20+6+10+7+18+16}    16 GURU")
    print()
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    yearall_1, guru = subtract_dates(yearall, gurui)
    yearall_2, raahu = subtract_dates(yearall_1, raahui)
    yearall_3, mangal = subtract_dates(yearall_2, mangali)
    yearall_4, chandra = subtract_dates(yearall_3, chandrai)
    yearall_5, surya = subtract_dates(yearall_4, suryai)
    yearall_6, shukra = subtract_dates(yearall_5, shukrai)
    yearall_7, ketu = subtract_dates(yearall_6, ketui)
    yearall_8, budhh = subtract_dates(yearall_7, budhhi)
    yearall_9, shani = subtract_dates(yearall_8, shanii)
    shani_t = add_dates(bobo, shani)
    budhh_t = add_dates(shani_t, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    surya_t = add_dates(shukra_t, surya)  
    chandra_t = add_dates(surya_t, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    guru_t = add_dates(raahu_t, guru)
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketui        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print ("\n") 
    print ()
    print("BUDHH:-")
    jo=0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print ("\n")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print ("\n")
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print ("\n")
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print ("\n")
if user_day == 4:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} BUDHH\n{dob1}-{dob2}-{dob3+7}    07 KETU\n{dob1}-{dob2}-{dob3+7+20}    20 SHUKRA\n{dob1}-{dob2}-{dob3+7+20+6}    06 SURYA\n{dob1}-{dob2}-{dob3+7+20+6+10}    10 CHANDRA\n{dob1}-{dob2}-{dob3+7+20+6+10+7}    07 MANGAL\n{dob1}-{dob2}-{dob3+7+20+6+10+7+18}    18 RAAHU\n{dob1}-{dob2}-{dob3+7+20+6+10+7+18+16}    16 GURU\n{dob1}-{dob2}-{dob3+7+20+6+10+7+18+16+19}    19 SHANI") 
    print ()
    print("BUDHH:-")
    jo = 0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    yearall_1, shani = subtract_dates(yearall, shanii)
    yearall_2, guru = subtract_dates(yearall_1, gurui)
    yearall_3, raahu = subtract_dates(yearall_2, raahui)
    yearall_4, mangal = subtract_dates(yearall_3, mangali)
    yearall_5, chandra = subtract_dates(yearall_4, chandrai)
    yearall_6, surya = subtract_dates(yearall_5, suryai)
    yearall_7, shukra = subtract_dates(yearall_6, shukrai)
    yearall_8, ketu = subtract_dates(yearall_7, ketui)
    yearall_9, budhh = subtract_dates(yearall_8, budhhi)
    budhh_t = add_dates(bobo, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    guru_t = add_dates(raahu_t, guru)
    shani_t = add_dates(guru_t, shani)
    print()
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketu        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print ("\n")
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print ("\n")
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print ("\n")
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print ("\n")
if user_day == 9:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} KETU\n{dob1}-{dob2}-{dob3+20}    20 SHUKRA\n{dob1}-{dob2}-{dob3+20+6}    06 SURYA\n{dob1}-{dob2}-{dob3+20+6+10}    10 CHANDRA\n{dob1}-{dob2}-{dob3+20+6+10+7}    07 MANGAL\n{dob1}-{dob2}-{dob3+20+6+10+7+18}    18 RAAHU\n{dob1}-{dob2}-{dob3+20+6+10+7+18+16}    16 GURU\n{dob1}-{dob2}-{dob3+20+6+10+7+18+16+19}    19 SHANI\n{dob1}-{dob2}-{dob3+20+6+10+7+18+16+19+17}    17 BUDHH")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    yearall_1, budhh = subtract_dates(yearall, budhhi)
    yearall_2, shani = subtract_dates(yearall_1, shanii)
    yearall_3, guru = subtract_dates(yearall_2, gurui)
    yearall_4, raahu = subtract_dates(yearall_3, raahui)
    yearall_5, mangal = subtract_dates(yearall_4, mangali)
    yearall_6, chandra = subtract_dates(yearall_5, chandrai)
    yearall_7, surya = subtract_dates(yearall_6, suryai)
    yearall_8, shukra = subtract_dates(yearall_7, shukrai)
    yearall_9, ketu = subtract_dates(yearall_8, ketui)
    ketu_t = add_dates(bobo, ketu)
    shukra_t = add_dates(ketu_t, shukra)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    guru_t = add_dates(raahu_t, guru)
    shani_t = add_dates(guru_t, shani)
    budhh_t = add_dates(shani_t, budhh)
    print()
    print (f"{ketu_t}    {ketu}  ketu        ")
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    shukra_t = add_dates(budhh_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    print()
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ({chandrai} chandra)")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print ("\n")
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print ("\n")
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print ("\n") 
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print ("\n")
    print("BUDHH:-")
    jo= 0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print ("\n")
if user_day == 6:
    print(f"{dob1}-{dob2}-{dob3}    {days_diff}-{months_diff}-{years_diff} SHUKRA\n{dob1}-{dob2}-{dob3+6}    06 SURYA\n{dob1}-{dob2}-{dob3+6+10}    10 CHANDRA\n{dob1}-{dob2}-{dob3+6+10+7}    07 MANGAL\n{dob1}-{dob2}-{dob3+6+10+7+18}    18 RAAHU\n{dob1}-{dob2}-{dob3+6+10+7+18+16}    16 GURU\n{dob1}-{dob2}-{dob3+6+10+7+18+16+19}    19 SHANI\n{dob1}-{dob2}-{dob3+6+10+7+18+16+19+17}    17 BUDHH\n{dob1}-{dob2}-{dob3+6+10+7+18+16+19+17+7}    07 KETU")
    print ("\n")
    print("SHUKRA:-")
    jo=0
    shukrai= "0-4-3"
    suryai= "0-0-1"
    chandrai= "0-8-1"
    mangali= "0-2-1"
    raahui= "0-0-3"
    gurui= "0-8-2"
    shanii= "0-2-3"
    budhhi= "0-10-2"
    ketui= "0-2-1"
    yearall_1, ketu = subtract_dates(yearall, ketui)
    yearall_2, budhh = subtract_dates(yearall_1, budhhi)
    yearall_3, shani = subtract_dates(yearall_2, shanii)
    yearall_4, guru = subtract_dates(yearall_3, gurui)
    yearall_5, raahu = subtract_dates(yearall_4, raahui)
    yearall_6, mangal = subtract_dates(yearall_5, mangali)
    yearall_7, chandra = subtract_dates(yearall_6, chandrai)
    yearall_8, surya = subtract_dates(yearall_7, suryai)
    yearall_9, shukra = subtract_dates(yearall_8, shukrai)
    shukra_t = add_dates(bobo, shukra)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandra)
    mangal_t = add_dates(chandra_t, mangal)
    raahu_t = add_dates(mangal_t, raahu)
    guru_t = add_dates(raahu_t, guru)
    shani_t = add_dates(guru_t, shani)
    budhh_t = add_dates(shani_t, budhh)
    ketu_t = add_dates(budhh_t, ketu)
    print()
    print (f"{shukra_t}    {shukra}  shukra        ")
    print (f"{surya_t}    {surya}  surya        ")
    print (f"{chandra_t}    {chandra}  chandra        ")
    print (f"{mangal_t}    {mangal}  mangal        ")
    print (f"{raahu_t}    {raahu}  raahu        ")
    print (f"{guru_t}    {guru}  guru        ")
    print (f"{shani_t}    {shani}  shani        ")
    print (f"{budhh_t}    {budhh}  budhh        ")
    print (f"{ketu_t}    {ketu}  ketu        ")
    print ("\n")
    print("SURYA:-")
    print()
    jo=0
    suryai= "18-3-0"
    chandrai= "0-6-0"
    mangali= "6-4-0"
    raahui= "24-10-0"
    gurui= "18-9-0"
    shanii= "12-11-0"
    budhhi= "6-10-0"
    ketui= "6-4-0" 
    shukrai= "0-0-1"
    surya_t = add_dates(ketu_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print ("\n")
    print()
    print("CHANDRA:-")
    print()
    jo=0
    chandrai= "0-10-0"
    mangali= "0-7-0"
    raahui= "0-6-1"
    gurui= "0-4-1"
    shanii= "0-7-1"
    budhhi= "0-5-1"
    ketui= "0-7-0" 
    shukrai= "0-8-1"
    suryai= "0-6-0"
    chandra_t = add_dates(shukra_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print ("\n")
    print()
    print ("\n")
    print()
    print("MANGAL:-")
    print()
    jo=0
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketui= "27-4-0" 
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangal_t = add_dates(surya_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print ("\n")
    print("RAAHU:-")
    print()
    jo=0
    raahui= "12-8-2"
    gurui= "24-4-2"
    shanii= "6-10-2"
    budhhi= "18-6-2"
    ketui= "18-0-1" 
    shukrai= "0-0-3"
    suryai= "24-10-0"
    chandrai= "0-6-1"
    mangali= "18-0-1"
    raahu_t = add_dates(chandra_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print ("\n")
    print("GURU:-")
    print()
    jo=0
    gurui= "18-1-2"
    shanii= "12-6-2"
    budhhi= "6-3-2"
    ketui= "6-11-0" 
    shukrai= "0-8-2"
    suryai= "18-9-0"
    chandrai= "0-4-1"
    mangali= "6-11-0"
    raahui= "24-4-2"
    guru_t = add_dates(mangal_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print ("\n") 
    print("SHANI:-")
    print()
    jo=0
    shanii= "3-0-3"
    budhhi= "9-8-2"
    ketui= "9-1-1" 
    shukrai= "0-2-3"
    suryai= "12-11-0"
    chandrai= "0-7-1"
    mangali= "9-1-1"
    raahui= "6-10-2"
    gurui= "12-6-2"
    shani_t = add_dates(raahu_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)  
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketui        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print ("\n")
    print("BUDHH:-")
    jo= 0
    budhhi= "27-4-2"
    ketui= "27-11-0"
    shukrai= "0-10-2"
    suryai= "6-10-0"
    chandrai= "0-5-1"
    mangali= "27-11-0"
    raahui= "18-6-2"
    gurui= "6-3-2"
    shanii= "9-8-2"
    budhh_t = add_dates(guru_t, budhhi)
    ketu_t = add_dates(budhh_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, surya)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    print()
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print ("\n")
    print("KETU:-")
    jo=0
    ketui= "27-4-0"
    shukrai= "0-2-1"
    suryai= "6-4-0"
    chandrai= "0-7-0"
    mangali= "27-4-0"
    raahui= "18-0-1"
    gurui= "6-11-0"
    shanii= "9-1-1"
    budhhi= "27-11-0"
    ketu_t = add_dates(shani_t, ketui)
    shukra_t = add_dates(ketu_t, shukrai)
    surya_t = add_dates(shukra_t, suryai)
    chandra_t = add_dates(surya_t, chandrai)
    mangal_t = add_dates(chandra_t, mangali)
    raahu_t = add_dates(mangal_t, raahui)
    guru_t = add_dates(raahu_t, gurui)
    shani_t = add_dates(guru_t, shanii)
    budhh_t = add_dates(shani_t, budhhi)
    print()
    print (f"{ketu_t}    {ketui}  ketu        ")
    print (f"{shukra_t}    {shukrai}  shukra        ")
    print (f"{surya_t}    {suryai}  surya        ")
    print (f"{chandra_t}    {chandrai}  chandra        ")
    print (f"{mangal_t}    {mangali}  mangal        ")
    print (f"{raahu_t}    {raahui}  raahu        ")
    print (f"{guru_t}    {gurui}  guru        ")
    print (f"{shani_t}    {shanii}  shani        ")
    print (f"{budhh_t}    {budhhi}  budhh        ")
    print ("\n")
print()    
print("THANKS FOR MAKING ME ;0..XOXO")
    
