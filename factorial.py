def factorial(n):
    if n== 0 or n == 1:
        return 1
    else:
        return n* factorial(n - 1)
    
num= int(input("Enter a number: "))

if num < 0:
    print ("Factorials don't eist for negative numbers")
 
else:
    print(f"The factorial for {num} is {factorial(num)}")