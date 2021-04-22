'''WAPP to find the MAX of three numbers'''

num = int(input("Enter any number: "))
num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))

if num > num1 and num > num2:
    print(f"{num} is the greatest number.")

elif num1 > num and num1 > num2:
    print(f"{num1} is the greatest number.")

elif num == num1 == num2:
    print("All the valuesa are equal.")

elif num == num1:
    print("First and Second values are same.")

elif num == num2:
    print("First and Third values are same.")

elif num1 == num2:
    print("Second and Third values are same.")

else:
    print(f"{num2} is the greatest nubmer.")

