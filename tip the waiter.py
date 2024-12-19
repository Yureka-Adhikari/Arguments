def totalCalc(bill, tip):
    total = bill * (1 + (0.01 * tip))
    return total

billamt= int(input("enter the bill : "))
tipamt= int(input("enter the tip : "))

res = totalCalc(billamt, tipamt)

print(f"Bill : {billamt}")
print(f"Tip : {tipamt}%")
print(f"Total : {res}")