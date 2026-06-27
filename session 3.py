#Session 3 Day 3
#Conditional Statement.
#Q: take a input from user and print the number is even or odd

n=int(input("Enter the number:"))
if n%2 == 0:
  print("Number is even")

else: 
 print("Number is odd")

#SMALL PROJECT 1.
#SMART GRADING SYSTEM.
#IDEA: GIVEN MARKS ATTENDANCE AND CHEATING FLAG DECIDE THE RESULT.

marks=float(input("Enter the number"))
attendance=int(input("Enter the attendance %"))
cheating_flag=input("Cheating")

cheating_flag== "yes"
if cheating_flag:
     print("Fail")
else:
     print("Pass")
     
   
if marks >= 90:
  print("Grade A")
elif marks <= 75 < 90:
    print("Grade B")
elif marks <= 60 < 75:
      print("Grade C")
else:
      print("Fail")


if marks >= 60 and attendance >= 75:
        print("pass")
else:
        print("fail")

#PROJECT 2
#ATM WITHDRAWAL VALIDATOR
#IDEA: DECIDE WHETHER A WITHDRAW IS ALLOWED OR NOT.
#RULES:  IF ACCOUNT INACTIVE: REJECT
       # IF WITHDRAW AMOUNT > BALANCE :REJECT
       # IF WITHDRAW AMOUNT > DAILY LIMIT: REJECT
       # ELSE: ALLOW.

balance=float(input("Enter the balance amount"))
withdraw_amount=int(input("Enter the amount"))
daily_limit=int(input("Enter daily limit"))
is_account_active=input("is account active(yes or no)")
if is_account_active == "no":
     print("reject")
elif withdraw_amount > balance:
    print("reject")
elif withdraw_amount > daily_limit:
     print("reject")

else:
     print("Allow")