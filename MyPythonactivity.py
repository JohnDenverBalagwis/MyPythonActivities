print("-----------------------------------------------")
print("          PICK YOUR LUCKY NUMBER!")
print("-----------------------------------------------")

guess = "0"
while guess != "7":
    guess = input("Enter the lucky number: ")
    if guess == "7":
        print("YOU'VE GOT THE LUCKY NUMBER!")
    else:
        print("Try Again!")
        
print("-----------------------------------------------")
print("                THANK YOU!")
print("-----------------------------------------------")









print("-----------------------------------------------")
print("             EVEN/ODD NUMBER")
print("-----------------------------------------------")

user_input = int(input("Enter a number: "))
print("-----------------------------------------------")


even, odd= 0, 0

for i in range(user_input): 

    if i % 2 == 0: 

       odd+= 1 

    else: 

        even += 1          

print("Number of Even numbers : ", even) 

print("Number of Odd numbers : ", odd)

print("-----------------------------------------------")
print("                 THANK YOU!")
print("-----------------------------------------------")












print("-----------------------------------------------")
print("             SUM AND AVERAGE")
print("-----------------------------------------------")
print("Create a program that compute the sum and average of n integer numbers (input from the user). Input 0 to finish. ")
count = 0
sum = 0.0
number = 1

while number != 0:
    number = int(input(""))
    sum = sum + number
    count += 1

if count == 0:
    print("Input some numbers")
else:
    print(sum / (count-1),("is the Average"),sum, "is the Sum ")
    

print("-----------------------------------------------")
print("                THANK YOU!")
print("-----------------------------------------------")
