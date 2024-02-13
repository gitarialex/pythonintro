# arithmetic operators
num1=int(input("Enter Number"))
num2=int(input("Enter Number"))
print(f"The sum is {num1+num2}")
print(f"The difference is {num1-num2}")
print(f"The multiple is {num1*num2}")
print(f"The quotient is {num1/num2}")
print(f"The remainder is {num1%num2}")

# comparison operators

num3=int(input("Enter First No."))
num4=int(input("Enter Second No."))
print(f"{num3} is equal to {num4} {num3==num4}")
print(f"{num3} is not equal to {num4} {num3!=num4}")
print(f"{num3} is greater than {num4} {num3>num4}")
print(f"{num3} is greater than or equals to {num4} {num3>=num4}")
print(f"{num3} is less than {num4} {num3<num4}")
print(f"{num3} is less than or equals to {num4} {num3<=num4}")

# logical operators

num5=int(input("1st Number"))
num6=int(input('2nd Number'))
print(f"both statements should be true {num5==num6 and num5>15}")
print(f"one statement should be true {num5==num6 or num5>15}")