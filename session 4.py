#Loops

#while loop
#print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i=i+1

#print number from 5 to 1: reverse order.
i=5
while i>=1:
    print(i)
    i=i-1

#for loop
for i in range(0,10):
    print(i)

#print numbers from 2-10:
for i in range(2,11):
       print(i)

#default start from 0:
for i in range(11):
     print(i)

#steps: difference between two consecutive.
for i in range(0,10,2):
    print(i)

#print odd no. from 1-20
for i in range(1,20,2):
     print(i)

#print hello world 10 times:
for i in range(10):
     print("hello world")

#break statement.
i=1
while i<=10:
     if(i>4):
          break
     print(i)
     i=i+1

#run a loop from 1-10 and use break when i will be greater then 5.
i=1
while i<=10:
     if(i>5):
       break
     print(i)
     i=i+1

#continue statement: 
for i in range(0,11):
     if i==6:
          continue
     print(i)

#with while loop
i=1
while i<=10:
     if i==8:
          i=i+1
          continue
     print(i)
     i=i+1

#Ques:loop through numbers from 1-100 if number is divisble by 3 fizz
# and if divisble by 5 buzz and if both by 3 and 5 as well print fizz buzz and if not otherwise print numbers.

for i in range(1,101):
     if i % 3 == 0 and i % 5 == 0:
          print("fizzbuzz")
     elif i % 3 == 0:
          print("fizz")
     elif i % 5 == 0:
          print("buzz")
     else:
          print(i)