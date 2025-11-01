#1
w=float(input("Enter the weight in kg "))
h=float(input("enterbheight in meters"))
bmi=w/h**2
if bmi <=18.5 :
 	print("underweight")
elif 18.5<=bmi<=24.9:
 	print("normal")
elif 25<=bmi<=29.9:
 	print("over")
else:
     if 30<=bmi<=34.9:
        print("obese(1)")
     elif 35<=bmi<=39.9:
           print("(2)")
     else:
      	print("(3)")
      	

#2
light = input("Enter traffic light color (red, yellow, green): ")
pedestrians = input("Are there pedestrians? (yes/no): ")

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Prepare to stop")
elif light == "green":
    if pedestrians == "yes":
        print("Wait for pedestrians to cross")
    else:
        print("Go")
	   	
#3
n=int(input("age : "))
m=input("Are you an lomg term : ")
if n<12:
	print("50%")
elif 12<n<18:
	print("30")
elif n>60:
    if m=="yes":
    	print("40%")
    else:
    	print("20%")
else:
	print("no")
	
#4
usage = float(input("Enter your data usage in GB: "))
videos = input("Do you stream a lot of videos? (yes/no): ")

if usage < 1:
    print("Basic Plan")
elif 1 <= usage <= 5:
    print("Standard Plan")
else:
    if videos == "yes":
        print("Unlimited Plan with HD streaming")
    else:
        print("Unlimited Plan")


		
#5
exercise = int(input("How many times do you exercise per week? "))
strength = input("Do you include strength training? (yes/no): ")

if exercise < 1:
    print("Inactive")
elif 1 <= exercise <= 3:
    print("Moderately active")
elif 4 <= exercise <= 6:
    print("Active")
else:
    if strength == "yes":
        print("Very Active")
    else:
        print("Active")

#6
bill = float(input("Enter bill amount: "))
service = input("Service quality (excellent, good, average, poor): ")

if service == "excellent":
    tip = 0.20 * bill
elif service == "good":
    tip = 0.15 * bill
elif service == "average":
    tip = 0.10 * bill
elif service == "poor":
    leave_tip = input("Do you still want to leave a tip? (yes/no): ")
    if leave_tip == "yes":
        tip = 0.05 * bill
    else:
        tip = 0
else:
    tip = 0

if tip > 0:
    print("Tip:", tip)
else:
    print("No tip")

#7
temp = int(input("Enter the temperature (°C): "))
rain = input("Is it raining? (yes/no): ")

if temp < 10:
    print("Wear a coat")
elif 10 <= temp <= 20:
    if rain == "yes":
        print("Wear a jacket and carry an umbrella")
    else:
        print("Wear a jacket")
else:
    if rain == "yes":
        print("Wear light clothes and carry an umbrella")
    else:
        print("Wear light clothes")

#8
a=int(input("enter your age: "))
t=int(input("enter movies time(24 hour): "))
if a<12 or a>60:
   if t<18:
      print("ticket price is 7$")
   else:
        print("ticket price is 9$: ")
else:
     if t<18:
       print("ticket price is $10")
     else:
        print(" ticket price is $12")

#9
balance = float(input("Enter your current balance: $"))
action = input("Do you want to deposit or withdraw? ")
amount = float(input("Enter the amount: $"))
if action == "withdraw":
   if amount > balance:
      print("Insufficient funds.")
   else:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance:.2f}")
elif action == "deposit":
      balance += amount
      print(f"Deposit successful. New balance: ${balance:.2f}")
else:
 print("Invalid action entered. Please choose deposit or withdraw.")

#10
n=input("Enter the vehicle type car/bike/truck: ")
a=int(input("Enter the age of the driver: "))
if n=="car":
   if 18<=a<25:
       print("The Premium is $500.")
   elif a>=25:
       print("The Premium is $300.")
   else:
        print("Driver is Under Age.")
elif n=="bike":
     if 18<=a<25:
        print("The Premium is $400.")
     elif a>=25:
        print("The Premium is $200.")
     else:
         print("Driver is Under Age.")
elif n=="truck":
      if 18<=a<25:
          print("The Premium is $600.")
      elif a>=25:
          print("The Premium is $400")
else:
 print("Driver is Under Age.")

#11
 
choice = input("Do you want to convert from Celsius to Fahrenheit or Fahrenheit to Celsius? (C/F): ")
if choice == "c":
   celsius = float(input("Enter temperature in Celsius: "))
   fahrenheit = (9/5) * celsius + 32
   print(f"{celsius}°C = {fahrenheit:.2f}°F")
elif choice == "f":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (5/9) * (fahrenheit - 32)
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
else:

    print("Invalid choice! Please enter 'C' or 'F'.")
 
#12
score = int(input("Enter score: "))
s= input("have you submitted the assignment?: ")
if score > 50:
    if s== "yes":
        print("Pass with full credits")
    else:
        print("Pass with reduced credits")
else:
    if s== "yes":
        print("Fail, but eligible for re-exam")
    else:
        print("Fail and not eligible for re exam")

#13
s = int(input("Enter job salary: "))
l= input("Enter location (remote/office): ")
if s> 70000:
    if l== "remote":
        print("Accept the job.")
    else:
        c= int(input("Enter commute time (minutes): "))
        if c<= 30:
            print("Accept the job.")
        else:
            print("Consider the job.")
else:
    if l == "remote":
        print("Consider the job.")
    else:
        print("Negotiate for a better offer.")


#14
gpa = float(input("Enter GPA: "))
e = input("have you Involved in extracurricular?: ")

if gpa > 3.5:
    print("Eligible for full scholarship")
elif 3.0 <= gpa <= 3.5:
    if e == "yes":
        print("Eligible for partial scholarship")
    else:
        print("Not eligible for scholarship")
else:
    print("Not eligible for scholarship")


#15
age = int(input("Enter age: "))
m = input("enter the type of membership ypu want (basic/premium/vip): ")
if age > 60:
    if m == "basic":
       print("fee = 20")
    elif m== "premium":
        print("fee = 35")
    else:
        print("fee = 50")
else:
    if m == "basic":
        print("fee = 30")
    elif m == "premium":
        print("fee = 50")
    else:
        print("fee = 70")


# 16
b = float(input("Enter balance: "))
l = input("whethher the Payment is late?: ")
if l== "yes":
    if b< 1000:
        print("interest = 0.05")
    elif b<= 5000:
        print("interest= 0.10")
    else:
        print("interest = 0.15")
else:
    if b < 1000:
        print("interest = 0.02")
    elif b<= 5000:
        print("interest= 0.05")
    else:
        print("interest= 0.08")

# 17
a= float(input("Enter order amount: "))
s = input("enter Shipping type (standard/express/overnight): ")
if a > 100:
    print("shipping charge = 0")
elif s == "standard":
    print("shipping charge= 5")
elif s == "express":
    print("shipping charge = 10")
else:
    print("shipping charge = 20")

#18
age = int(input("Enter age: "))
t = input("enter your Purchase time (early/regular): ")
if 12> age > 60:
    if t== "early":
        print("Ticket is free")
    else:
        print("50% discount")
elif 12 <= age <= 60:
    if t == "early":
        print("30% discount")
    else:
        print("No discount")
# 19
d= int(input("Enter number of days: "))
b = float(input("Enter daily budget: "))

if b< 50:
    if d < 7:
        print("Suggest a local trip")
    else:
        print("Suggest a staycation")
elif 50 <= b <= 150:
    if d< 7:
        print("Suggest a domestic trip")
    else:
        print("Suggest a nearby international trip")
else:
    if d < 7:
        print("Suggest a luxury domestic trip")
    else:
        print("Suggest an international trip")

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


# PROBLEM 21
pet=input("Enter your pet type (dog, cat, bird) : ")
age=int(input("Enter the age of your pet :"))
if pet=="dog":
 if age<2:
   print("Recommend: Puppy care and training")
 if age>=2:
   print("Recommend: Adult dog care")
if pet=="cat":
 if age<2:
    print("Recommend: Kitten care and socialization")
 if age>=2:
   print("Recommend: Adult cat care")
if pet=="bird":
 if age<1:
    print("Recommend: Baby bird care and hand-feeding")
 if age>=1:
    print("Recommend: Adult bird care and enrichment")
else:
     print("This pet care Not Available")


# PROBLEM 22
age = int(input("Enter the child's age: "))
preschool = input("Has the child completed preschool?(yes/no): ")
if age >= 5:
 if preschool == "yes":
    print("Eligible for kindergarten.")
 else:
      print("Not eligible for kindergarten.")
else:
 if age == 4:
    print("Eligible for preschool.")
 else:

     print("Too young for school.")

# PROBLEM 23
weather = input("Enter the weather (sunny, rainy, cloudy):")
preference = input("Do you prefer indoor or outdooractivities? ").lower()
if weather == "sunny":
 if preference == "outdoor":
   print("Go for a hike.")
 else:
     print("Visit a museum.")
elif weather == "rainy":
 if preference == "outdoor":
    print("Take an umbrella and go for a walk.")
 else:
     print("Watch a movie.")
elif weather == "cloudy":
 if preference == "outdoor":
    print("Go for a bike ride.")
 else:
      print("Read a book.")
else:
     print("Sorry, I don't have suggestions for this weather.")


# PROBLEM 24
income = float(input("Enter your annual income: $"))
if income < 20000:
 tax_rate = 10
elif income <= 50000:
 tax_rate = 20
else:
 self_employed = input("Are you self-employed? (yes/no):").lower()
 if self_employed == "yes":
      tax_rate = 35
 else:
     tax_rate = 30
print(f"Your tax rate is {tax_rate}%.")


# PROBLEM 25
car_type = input("Enter the car type (economy, sedan, SUV):").lower()
days = int(input("Enter the number of rental days: "))



 # PROBLEM 26
age = int(input("Enter age: "))
a= input("Are you active? (yes/no): ")
if age < 18:
 if a == "yes":
    print("Drink 2.5 liters")
 else : print("Drink 2 liters")
else:
   if a == "yes":
       print("Drink 3 liters" )
   else :
       print("Drink 2.5 liters")
       
# PROBLEM 27
income = float(input("Enter income: "))
donate = input("Willing to donate? (yes/no): ")
if donate == "yes":
 if income < 30000:
    print("Donate $50")
 elif income <= 100000:
     print("Donate $200")
 else:
     print("Donate $500")
else:
      print("No donation suggested")
# PROBLEM 28
n=int(input("enter no of users: "))
s=input("whether they stream video?(yes/no) ?")
if 1<=n<=2:
  if s=="yes":
       print("50 mbps plan")
  else: print("25 mbps plan")
else:
    if n>3:
       if s=="yes":
          print("100 mbps plan")
       else:
        print("50 mbps plan")
  

# PROBLEM 29
h= int(input("Hours on social media daily: "))
s= input("why you use social media ?(work/entertainment): ")
if h < 1:
 print("Minimal usage")
elif 1 <= h <= 3:
 if s == "work" :
    print("Moderate usage for work")
 else:
     print("Moderate usage for entertainment")
else:
 if s == "work":
    print("Heavy usage for work" )
 else:
     print( "Heavy usage for entertainment")
# PROBLEM 30
budget = float(input("Enter your budget per person: $"))
if budget < 10:
   print("Fast food.")
elif budget <= 30:
    print("Casual dining.")
else:
 preference = input("Do you prefer fine dining or casualdining? (fine/casual): ").lower()
 if preference == "fine":
    print("Fine dining restaurant.")
 else:
     print("Upscale casual dining.")
# PROBLEM 31
age = int(input("Enter your age: "))
if age < 5:
    price = 0
elif age <= 12:
     price = 5
elif age <= 18:
     price = 7
else:
 student = input("Are you a student? (yes/no): ").lower()
 if student == "yes":
    price = 8
 else:
     price = 10
print(f"Ticket price: ${price}")
# PROBLEM 32
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight.")
elif bmi <= 24.9:
    print("Normal weight.")
elif bmi <= 29.9:
     print("Overweight.")
elif bmi <= 34.9:
     print("Obese (Class I).")
elif bmi <= 39.9:
     print("Obese (Class II).")
else:
     print("Obese (Class III).")
print(f"Your BMI is {bmi:.2f}")
# PROBLEM 33
n=int(input("enter the age"))
t=input("enter whether you are long term member (yes/no)")
p=input("enter whether you are a child,student,seniorcitizen:")
if p=="child" and n<=12:
    print("they got 0.5 discount")
elif p=="student" and 12<=n<=18:
    print("they hot 0.3 discount")
elif p=="senior citizen" and n>=60 and t=="yes":
   print("they get a 0.4 discount")
else:
     print("no match")
# PROBLEM 34
usage = float(input("Enter your monthly data usage in GB: "))
streaming = input("Do you stream a lot of videos? (yes/no):")
if usage < 1:
   print("We recommend: Basic Plan")
elif usage <= 5:
    print("We recommend: Standard Plan")
else:
       if streaming == "yes":

         print("We recommend: Unlimited Plan with HD streaming")
       else:
           print("We recommend: Unlimited Plan")
# PROBLEM 35
balance = float(input("Enter your initial balance: ₹"))
transaction = input("Do you want to 'deposit' or 'withdraw'?")
amount = float(input("Enter the amount: ₹"))
if transaction == 'withdraw':
 if amount > balance:
    print("Insufficient funds.")
 else:
     balance -= amount
     print(f"New balance: ₹{balance}")
elif transaction == 'deposit':
     balance += amount
     print(f"New balance: ₹{balance}")
else:
     print("Invalid transaction type")

