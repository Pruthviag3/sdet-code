def decor(addition):
    def inner():
        result=addition()
        num3=float(input("Enter 3rd number:"))
        result=result+num3
        return result
    return inner

@decor
def addition():
    num1=float(input("Enter 1st number:"))
    num2=float(input("Enter 2st number:"))
    result=num1+num2
    return result

print("The sume is:",addition())

