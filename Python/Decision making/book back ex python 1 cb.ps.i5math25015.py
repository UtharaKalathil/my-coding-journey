#1
m= int(input("enter the digit: "))
if m>0:
      print("positive")
elif m<0:
    print("negative")
elif m==0:
    print("zero")
if m%2==0:
    print("even")
else:
    print("odd")

#2
l=int(input("enter the length of rectangle 1: "))
w=int(input("enter the width of rectangle 1: "))
L=int(input("enter the length of rectangle 2: "))
W=int(input("enter the width of rectangle 2 : "))
a=l*w
A=L*W
if a>A:
  print("rectangle 1 has greater area")
elif A>a:
    print("rectangle 2 has greater area")
else: print("both rectangle 1 and 2 has  same area")

#3
m=int(input("enter a month's number:" ))
if 1<=m<=3:
    print("month is 1st quarter")
elif 4<=m<=6:
    print("2nd quarter")
elif 7<=m<=9:
    print("3rd quarter")
elif 10<=m<=12:
    print("4th quarter")
else:
    print("error")

#4
n=int(input("enter a number: " ))

if n==1:
  print("I")
elif n==2:
    print("II")
elif n==3:
    print("III")

elif n==4:
    print("IV")
elif n==5:
    print("V")
elif n==6:
    print("VI")
elif n==7:
    print("VII")
elif n==8:
    print("VIII")
elif n==9:
    print("IX")

elif n==10:
    print("X")
else:
    print("error")


#5 Mass and Weight
mass=float(input("Enter the Mass of the object in Kgs: "))
weight=mass*9.8
print("Weight of the object: ", weight)
if weight>500:
 print("Object is too Heavy")
if weight<100:
 print("Object is too Light")
    

#6
m=int(input("enter a months number: "))
d=int(input("enter a day in month: "))
y=int(input("enter the years last 2 digit: "))
if m*d==y:
    print("the date is magic")
else:
    print("the date is not magic")

#7
a=int(input("enter score for 1st test: "))
b=int(input("enter score for 2nd test: "))
c=int(input("enter score for main test: "))
t=a+b+c
if t>50 or c<25:
        print("fail")
elif t>80:
        print("disjunction")
elif t>=60:
        print("credits")
elif 59>=t>=50:
        print("pass")
else:print("error")

#8 Hot Dog Cookout
people=int(input("Enter the number of people attending the cookout : "))
hotdogs=int(input("Enter the number of hot dogs each person will be given : "))
total_hotdogs=people*hotdogs
if total_hotdogs % 10 == 0:
 hotdog_packs = total_hotdogs // 10
else:
 hotdog_packs = total_hotdogs // 10 + 1
hotdogs_leftover = hotdog_packs * 10 - total_hotdogs
if total_hotdogs % 8 == 0:
 bun_packs = total_hotdogs // 8
else:
 bun_packs = total_hotdogs // 8 + 1
buns_leftover = bun_packs * 8 - total_hotdogs

print("Minimum number of hot dog packs required:", hotdog_packs)
print("Minimum number of bun packs required:", bun_packs)
print("Hot dogs left over:", hotdogs_leftover)
print("Buns left over:", buns_leftover)

#9 

#roulette wheel colors
p=int(input("enter no of packets"))
if p ==0:
      print("green")
elif 1>=p>=10:
    if p%2==0:
        print("black")
    else:
        print("red")
elif 11>=p>=18:
    if p%2==0:
        print("red")
    else:
        print("black")
elif 19>=p>=28:
    if p%2!=0:
        print("black")
    else:
        print("red")
elif p>=29 and p>36:
    if p%2==0:
        print("red")
    else:
        print("black")
else:print("no pocket")


#10

p=int(input("enter the no of pennies: "))
n=int(input("enter the no of nickels: "))
d=int(input("enter the no of dimes: "))
q=int(input("enter the no of quaeters: "))
t=p*0.01+n*0.05+d*0.10+q*0.25
if t==1:
   print("congrats you won")
elif t>1:
    print("the amount is more than 1$")
else: print("amount is less than 1 $")
    
#11


b= int(input("Enter number of books purchased: "))
if b== 0:
    print("you earned 0 points")
elif b== 2:
    print("you earned 5 points")
elif b== 4:
    print("you earned 15 points")
elif b == 6:
    print("you earned 30 points")
elif b >= 8:
    print("you earned 60 points")
else:print("0 points earned")

# 12 Software sales
price_per_package = 99
quantity = int(input("Enter the number of packages purchased: "))
if quantity >= 100:
 discount_rate = 0.40
elif quantity >= 50:
 discount_rate = 0.30
elif quantity >= 20:
 discount_rate = 0.20
elif quantity >= 10:
 discount_rate = 0.10
else:
 discount_rate = 0.0
total_before_discount = quantity * price_per_package
discount_amount = total_before_discount * discount_rate
total_after_discount = total_before_discount - discount_amount
# Output
print(f"Discount rate: {discount_rate*100}%")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Total after discount: ${total_after_discount:.2f}")

# 13 Shipping Charges
weight=float(input("Enter Weight of the package in pounds : "))
if 0<weight<=2:
 print("Shipping Charges Are : $1.50")
elif 2<weight<=6:
 print("Shipping Charges Are : $3.00")
elif 6<weight<=10:
 print("Shipping Charges Are : $4.00")
elif weight>10:
 print("Shipping Charges Are : $4:47")
else:
 print("Print valid Weight!!")

# 14 Body Mass Index
weight=float(input("Enter Your Weight in pounds : "))
height=float(input("Enter Your height in incs : "))
bmi=weight*(703/(height**2))
print("The body mass index is : ",bmi)
if 18.5<=bmi<=25:
 print("OPTIMAL WEIGHT!!!")
if bmi<18.5:
 print("UNDERWEIGHT")
if bmi>25:
 print("OVERWEIGHT")
 
# 15 Time Calculator
sec = int(input("Enter a number of seconds: "))
if sec >= 86400:
 days = sec // 86400
 sec = sec % 86400
 hours = sec // 3600
 sec = sec % 3600
 minutes = sec // 60
 seconds = sec % 60
 print("Time is:", days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
elif sec >= 3600:
 hours = sec // 3600
 sec = sec % 3600
 minutes = sec // 60
 seconds = sec % 60
 print("Time is:", hours, "hours", minutes, "minutes", seconds, "seconds")
elif sec >= 60:
 minutes = sec // 60
 seconds = sec % 60
 print("Time is:", minutes, "minutes", seconds, "seconds")
else:
 print("Time is:", sec, "seconds")
 
# 16 Feburary Days
y=int(input("enter the year :"))
if y %100 == 0 and y %400 == 0:
  print("it is a leap year")
elif y % 100 != 0 and y%4 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")



# 17 WifiDignostics Tree
n=input("reboot the computer and try to conect? (yes/no):")
if n == "yes" :
   print("problem sloved")
elif n == "no":
    print("reboot the router and try to connect")
elif n == "yes":
     print("problem solved")
elif n == "no":
     print("make sure the cables between the router and modem are plugged in firmly")
elif n == "yes":
    print("problem solved")
elif n == "no":
    print("get a new router")
else:
      print("unknown")



#20

p=float(input("Enter the purchase amount in $ : "))
ls=input("Enter the loyalty status (regular-1, silver-2, gold-3) : ")
if ls=="1":
    if p>100:
        print("Discount of 5% applied!!")
        print("Price after Discount : ",p-(p*0.05))
    if p<=100:
        print("No discount")
if ls=="2":
    if p>100:
        print("Discount of 10% applied!!")
        print("Price after Discount : ",p-(p*0.1))
    if p<=100:
        print("Discount of 5% applied!!")
        print("Price after Discount : ",p-(p*0.05))
if ls=="3":
    print("Discount of 15% applied!!")
    print("Price after Discount : ",p-(p*0.15))






    



    
