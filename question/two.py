''''''


def FizzBuzz(num):

    if num % 3 == 0 and num % 5 == 0 :
        return "Fizzbuzz"
    elif num % 3 == 0 :
        return "Fizz"
    elif num % 5 == 0 :
        return "Buzz"
    else:
        return num

a = int(input("Enter any number ::"))
print(FizzBuzz(a))


