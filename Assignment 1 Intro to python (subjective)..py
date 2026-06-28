               #PROBLEM STATEMENT.
#Ask the user for their name and store it in a variable.
#Ask the user for their age (in years) and store it as an integer.
#Ask the user for their height (in cm) and store it as a float.
#Calculate how many months old the user is (age × 12).
#Convert the user’s height from centimeters to meters (divide by 100).
#Display all the information in a formatted output.


#take user input
name= input("Enter your name:") #string
age= int(input("Enter your age in years:")) #integer
height_cm= float(input("Enter your height in cm:")) #float

#calculations
age_in_months= age*12 #for converting age in months multipy it by 12, as we know in 1 year there are 12 months.
height_in_meter= height_cm/100 #for converting height from cm to meter we use standard formula m=cm/100

#display output

print("Your Information")
print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months)")
print(f"Height: {height_cm} cm ({height_in_meter} meters)")
